## resource_hud.rpy - Survival resource system (60 Seconds style) and top HUD
##
## All values go from 0 to 100.
## Each landing site starts with its own values (see site_resources in 02_mapa_interactivo.rpy).
## Indicators appear in the HUD the first time a crew member explains them,
## and from then on they are always shown at the top of the screen,
## except on black screens, minigames and the site-selection map.

## -------------------------------------------------------------
## Resource variables
## -------------------------------------------------------------
default res_energy = 0          # Electricity (%)
default res_water = 0           # Water
default res_food = 0            # Food
default res_oxygen = 0          # Oxygen level (%)
default res_thermal = 0         # Thermal stability (%) - game over at 20%
default res_radiation = 0       # Accumulated radiation (%) - rises over time
default res_radiation_rate = 0  # Radiation increase per month at this site (%)
default antenna_ok = True       # Antenna / telecommunications: OK or damaged

# Indicators already explained to the player (shown in the HUD)
default hud_revealed = set()
# Master switch for the HUD (turned on after the first explanation)
default hud_on = False

## -------------------------------------------------------------
## Crew needs (3 = full, 0 = empty) - shown on the tablet's Crew tab
## -------------------------------------------------------------
default crew_hunger = {"miquel": 3, "nelson": 3, "hanna": 3, "commander": 3}
default crew_thirst = {"miquel": 3, "nelson": 3, "hanna": 3, "commander": 3}

## -------------------------------------------------------------
## Balance (soft at the beginning so the player can adapt)
## -------------------------------------------------------------
define ENERGY_PER_NIGHT = 1          # energy gained every night
define FOOD_PRODUCE_GAIN = 20        # food produced...
define FOOD_PRODUCE_WATER = 10       # ...spending this much water
define FOOD_PRODUCE_ENERGY = 10      # ...and this much energy
define EASY_DAYS = 7                 # first week: cheaper rations, stable environment
default solar_efficiency = 100       # % of energy the solar panels produce (drops if a panel is misaligned)
default energy_carry = 0.0
define PASSIVE_FOOD = 15   # greenhouse food produced every period
define PASSIVE_WATER = 15  # water recovered by the ECLSS every period
default last_passive = None
default repeat_penalty_pending = None  # crew member who led two missions in a row           # fractions of energy produced, kept for the next night

define HEAT_GAIN = 15                # thermal stability recovered...
define HEAT_ENERGY = 20              # ...spending this much energy

init python:
    def ration_cost():
        """Food or water spent to give one ration to one crew member (kept low so the player can adapt)."""
        return 5

## -------------------------------------------------------------
## How each indicator works (info window)
## -------------------------------------------------------------
define RES_INFO = [
    ("icon_energy", "ENERGY", "#facc15",
     "Powers the whole base. The solar panels produce +1 every night (around +15 per month). Producing food costs 10 energy. If a solar panel is misaligned, the energy you produce is reduced by a percentage."),
    ("icon_water", "WATER", "#38bdf8",
     "Over time each crew member gets thirsty (-1 on their water bar). Giving one ration of water costs 5 water. The ECLSS recycling system recovers +15 water every period, and expeditions can find ice."),
    ("icon_food", "FOOD", "#f97316",
     "Over time each crew member gets hungry (-1 on their food bar). Feeding one crew member costs 5 food. The greenhouse produces +15 food every period on its own, and you can produce +20 more by spending 10 water and 10 energy. Sending the same person on two missions in a row makes them lose 1 extra food."),
    ("icon_oxygen", "OXYGEN", "#93c5fd",
     "Stable during the first weeks. From the second month it drops about 10% every month: there is enough for about ten months before the air runs out. If it reaches 0%, the crew must evacuate."),
    ("icon_thermal", "TEMPERATURE", "#fb923c",
     "Thermal stability of the base. It starts changing in week 3 and then drops about 10% every month. Use HEAT THE BASE on the tablet (Crew tab): 20 energy = +15%. If it falls to 20%, the crew must evacuate."),
    ("icon_radiation", "RADIATION", "#ef4444",
     "Accumulated exposure. It starts increasing in week 3, at a speed that depends on the landing site. If it reaches 100%, the crew must evacuate."),
    ("icon_antenna", "ANTENNA", "#4ade80",
     "Link with Earth. It is either OK or DAMAGED: events such as storms can damage it."),
]

init python:
    def apply_site_resources(key):
        """Loads the starting resources of the chosen landing site."""
        r = site_resources[key]
        store.res_energy = r["energy"]
        store.res_water = r["water"]
        store.res_food = r["food"]
        store.res_oxygen = r["oxygen"]
        store.res_thermal = r["thermal"]
        store.res_radiation_rate = r["radiation_rate"]
        store.res_radiation = 0
        store.antenna_ok = True

    def reveal_resources(*names):
        """Adds indicators to the HUD (energy, water, food, oxygen, thermal, radiation, antenna)."""
        for n in names:
            store.hud_revealed.add(n)
        store.hud_on = True

    def clamp_resources():
        for name in ("res_energy", "res_water", "res_food", "res_oxygen", "res_thermal", "res_radiation"):
            setattr(store, name, max(0, min(100, getattr(store, name))))

    # --- Actions available from the tablet ---
    def feed_crew(who):
        c = ration_cost()
        if store.res_food >= c and store.crew_hunger[who] < 3:
            store.res_food -= c
            store.crew_hunger[who] += 1
            renpy.restart_interaction()

    def water_crew(who):
        c = ration_cost()
        if store.res_water >= c and store.crew_thirst[who] < 3:
            store.res_water -= c
            store.crew_thirst[who] += 1
            renpy.restart_interaction()

    def can_produce_food():
        return store.res_water >= FOOD_PRODUCE_WATER and store.res_energy >= FOOD_PRODUCE_ENERGY and store.res_food < 100

    def produce_food():
        if can_produce_food():
            store.res_water -= FOOD_PRODUCE_WATER
            store.res_energy -= FOOD_PRODUCE_ENERGY
            store.res_food += FOOD_PRODUCE_GAIN
            clamp_resources()
            store.food_produced_times += 1
            if store.food_produced_times >= 3:
                unlock("greenhouse")
            renpy.restart_interaction()

    def can_heat_base():
        return store.res_energy >= HEAT_ENERGY and store.res_thermal < 100

    def heat_base():
        if can_heat_base():
            store.res_energy -= HEAT_ENERGY
            store.res_thermal += HEAT_GAIN
            clamp_resources()
            renpy.restart_interaction()

    def produce_energy(amount):
        """Energy produced by the panels and the reactor, reduced by the solar efficiency.
        Returns the energy actually gained."""
        store.energy_carry += amount * store.solar_efficiency / 100.0
        gained = int(store.energy_carry)
        store.energy_carry -= gained
        store.res_energy += gained
        clamp_resources()
        return gained

    def month_passes():
        """Monthly environment changes (from the resource management sheet)."""
        store.res_oxygen -= 10
        store.res_thermal -= 10
        store.res_radiation += store.res_radiation_rate
        clamp_resources()

    def night_passes():
        """Applied at the start of every new day."""
        # Energy produced during the night depends on the solar panels' efficiency
        store.energy_carry += ENERGY_PER_NIGHT * store.solar_efficiency / 100.0
        gained = int(store.energy_carry)
        store.energy_carry -= gained
        store.res_energy += gained
        # The environment stays stable during the first week
        if store.day > EASY_DAYS:
            store.res_radiation += store.res_radiation_rate / 30.0
        clamp_resources()

    def passive_income():
        """Passive production every period: greenhouse food and ECLSS recycled water."""
        store.res_food += PASSIVE_FOOD
        store.res_water += PASSIVE_WATER
        clamp_resources()
        store.last_passive = (PASSIVE_FOOD, PASSIVE_WATER)

    def add_passive_line(report):
        if not store.last_passive or not report:
            return report
        f, w = store.last_passive
        store.last_passive = None
        return report[:1] + [("good", "Passive production: greenhouse +%d food, ECLSS water recycling +%d water." % (f, w))] + report[1:]

    def crew_gets_hungry():
        """Everyone loses 1 food and 1 water bar.
        If the same person went on a mission the last two days in a row, they lose 1 extra food."""
        passive_income()
        for k in store.crew_hunger:
            store.crew_hunger[k] = max(0, store.crew_hunger[k] - 1)
            store.crew_thirst[k] = max(0, store.crew_thirst[k] - 1)
        if store.repeat_penalty_pending:
            k = store.repeat_penalty_pending
            store.crew_hunger[k] = max(0, store.crew_hunger[k] - 1)
            store.repeat_penalty_pending = None

    # Screens where the HUD must NOT appear
    HUD_HIDDEN_SCREENS = ("electrical_panel", "wrong_sequence", "interactive_map", "location_card",
                          "warning_screen", "kitchen_tablet", "character_card",
                          "solar_arrow", "solar_result", "day_title", "the_end_screen", "week_end_screen")

    def hud_should_show():
        if not store.hud_on or not store.hud_revealed:
            return False
        if renpy.showing("black") or renpy.showing("bg end"):
            return False
        for s in HUD_HIDDEN_SCREENS:
            if renpy.get_screen(s):
                return False
        return True

    config.overlay_screens.append("resource_hud")

## -------------------------------------------------------------
## Icons (cropped to their visible area)
## -------------------------------------------------------------
image icon_energy = Crop((72, 101, 354, 404), "images/ui/ui_elec-removebg-preview.png")
image icon_food = Crop((38, 100, 370, 414), "images/ui/ui_comida-removebg-preview.png")
image icon_oxygen = Crop((16, 57, 398, 397), "images/ui/ui_oxigeno-removebg-preview.png")
image icon_radiation = Crop((32, 69, 410, 410), "images/ui/ui_radiacion-removebg-preview.png")
image icon_antenna = Crop((27, 71, 354, 412), "images/ui/ui_antena-removebg-preview.png")
image icon_info = Crop((13, 38, 406, 410), "images/ui/ui_info-removebg-preview.png")
image icon_thermal = Crop((51, 87, 366, 366), "images/ui/ui_temperatura.png")
image icon_water = "images/ui/ui_gota_agua.png"

## -------------------------------------------------------------
## Animations
## -------------------------------------------------------------
transform hud_pop:
    alpha 0.0 zoom 0.5
    easein 0.45 alpha 1.0 zoom 1.12
    easeout 0.2 zoom 1.0

transform hud_icon:
    xysize (46, 46)
    fit "contain"

transform info_icon:
    xysize (40, 40)
    fit "contain"

## -------------------------------------------------------------
## One HUD indicator (icon + name + bar + value)
## -------------------------------------------------------------
screen hud_item(icon, label, value, bar_color, danger_low=False, danger_high=False):
    $ danger = (danger_low and value <= 25) or (danger_high and value >= 75)
    hbox:
        spacing 8
        yalign 0.5
        at hud_pop
        add icon at hud_icon yalign 0.5
        vbox:
            spacing 3
            yalign 0.5
            text label size 13 bold True color "#cbd5e1"
            hbox:
                spacing 6
                bar:
                    value StaticValue(value, 100)
                    xsize 92
                    ysize 12
                    yalign 0.5
                    left_bar Solid(bar_color)
                    right_bar Solid("#47556999")
                    thumb None
                text "[value]%":
                    size 16
                    bold True
                    yalign 0.5
                    color ("#ff6b6b" if danger else "#f8fafc")

## -------------------------------------------------------------
## Top HUD
## -------------------------------------------------------------
screen resource_hud():
    zorder 50

    if hud_should_show():
        # Right-aligned so it never overlaps the progress badge (top-left)
        frame:
            xalign 1.0
            xoffset -8
            ypos 8
            background Solid("#1e293be6")
            padding (22, 9)

            hbox:
                spacing 30

                if "energy" in hud_revealed:
                    use hud_item("icon_energy", "ENERGY", res_energy, "#facc15", danger_low=True)
                if "water" in hud_revealed:
                    use hud_item("icon_water", "WATER", res_water, "#38bdf8", danger_low=True)
                if "food" in hud_revealed:
                    use hud_item("icon_food", "FOOD", res_food, "#f97316", danger_low=True)
                if "oxygen" in hud_revealed:
                    use hud_item("icon_oxygen", "OXYGEN", res_oxygen, "#93c5fd", danger_low=True)
                if "thermal" in hud_revealed:
                    use hud_item("icon_thermal", "TEMPERATURE", res_thermal, "#fb923c", danger_low=True)
                if "radiation" in hud_revealed:
                    use hud_item("icon_radiation", "RADIATION", res_radiation, "#ef4444", danger_high=True)
                if "antenna" in hud_revealed:
                    hbox:
                        spacing 8
                        yalign 0.5
                        at hud_pop
                        add "icon_antenna" at hud_icon yalign 0.5
                        vbox:
                            spacing 3
                            yalign 0.5
                            text "ANTENNA" size 13 bold True color "#cbd5e1"
                            if antenna_ok:
                                text "OK" size 16 bold True color "#4ade80"
                            else:
                                text "DAMAGED" size 16 bold True color "#ff6b6b"

                # Info button: opens the window explaining every indicator
                imagebutton:
                    idle Transform("icon_info", xysize=(40, 40), fit="contain", alpha=0.85)
                    hover Transform("icon_info", xysize=(40, 40), fit="contain", alpha=1.0)
                    yalign 0.5
                    action ToggleScreen("resource_info")


## -------------------------------------------------------------
## Info window: how every indicator works
## -------------------------------------------------------------
screen resource_info():
    modal True
    zorder 60

    button:
        xfill True
        yfill True
        background Solid("#000000aa")
        action Hide("resource_info")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1240
        background Solid("#0f172af5")
        padding (40, 30)

        vbox:
            spacing 14

            text "HOW THE SURVIVAL INDICATORS WORK" size 28 bold True color "#38bdf8" xalign 0.5
            text "Every indicator goes from 0 to 100. Keep them under control to survive on Mars." size 17 color "#94a3b8" xalign 0.5

            null height 4

            for icon, name, col, desc in RES_INFO:
                hbox:
                    spacing 18
                    add icon at hud_icon yalign 0.0
                    vbox:
                        xsize 1080
                        spacing 2
                        text name size 18 bold True color col
                        text desc size 16 color "#e2e8f0"

            hbox:
                spacing 18
                add "icon_info" at hud_icon yalign 0.0
                vbox:
                    xsize 1080
                    spacing 2
                    text "CREW (food and water bars)" size 18 bold True color "#cbd5e1"
                    text "Each crew member has 3 food bars and 3 water bars. Check them on the tablet's Crew tab and give rations when they get low." size 16 color "#e2e8f0"

            null height 4

            textbutton "CLOSE":
                xalign 0.5
                text_size 20
                text_bold True
                text_color "#38bdf8"
                text_hover_color "#ffffff"
                action Hide("resource_info")


## -------------------------------------------------------------
## End-of-day-1 supply report on the tablet (control room background)
## -------------------------------------------------------------
screen supplies_tablet():

    add Solid("#00000066")

    # Tablet placed slightly lower so it does not overlap the HUD
    add "images/tablet_report.png":
        xalign 0.5
        yalign 0.9
        zoom 0.75

    viewport:
        xpos 725
        ypos 404
        xsize 470
        ysize 575
        scrollbars "vertical"
        vscrollbar_xsize 8
        mousewheel True
        draggable True

        vbox:
            spacing 14

            text "SUPPLY REPORT - DAY 1":
                size 26
                bold True
                color "#0f172a"

            text "SETTLEMENT: [landing_site!u]":
                size 17
                bold True
                color "#0284c7"

            text "All supply levels have been checked after today's repairs.":
                size 17
                color "#334155"

            text "FOOD: [res_food] / 100  -  NORMAL":
                size 19
                bold True
                color "#c2410c"

            text "The settlement's stores contain [res_food] units of food. Each crew member needs a ration every day, and we can produce +20 food by spending 10 water and 10 energy.":
                size 17
                color "#334155"

            text "WATER: [res_water] / 100  -  NORMAL":
                size 19
                bold True
                color "#0369a1"

            text "The water reserves are at [res_water] units. Expeditions can bring back extra water, and the recyclers add +5 per month.":
                size 17
                color "#334155"

            text "STATUS:":
                size 17
                bold True
                color "#0284c7"

            text "Food and water levels are normal. The crew can rest.":
                size 17
                color "#334155"

    frame:
        xalign 1.0
        yalign 0.97
        xoffset -60
        background Solid("#0f172af2")
        padding (24, 8)

        textbutton "CLOSE TABLET ▶":
            text_size 20
            text_bold True
            text_color "#38bdf8"
            text_hover_color "#ffffff"
            action Return()
