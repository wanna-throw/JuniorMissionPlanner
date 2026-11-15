## day_tablet.rpy - Daily tablet (60 Seconds style): Report / Crew / Events tabs,
## rations, food production and mission selection.

## -------------------------------------------------------------
## Daily state (filled in by each day's label in 05_days.rpy)
## -------------------------------------------------------------
default day = 1
default day_tab = "report"          # "report", "crew" or "events"
default day_report = []             # list of ("title" | "head" | "text" | "good" | "bad", text)
default day_event = None            # None, or list like day_report
default events_seen = False
default day_needs_mission = False   # True on days where a mission must be chosen
default mission_choice = None       # "nelson", "hanna" or "miquel"
default mission_by_day = {}         # {day: who}
default day_continue_text = "END THE DAY ▶"

define CREW_NAMES = {"miquel": "Miquel", "nelson": "Nelson", "hanna": "Hanna", "commander": "Commander (you)"}
define CREW_COLORS = {"miquel": "#7ed957", "nelson": "#f423a3", "hanna": "#ff751f", "commander": "#8c52ff"}

define MISSIONS = [
    ("nelson", "Send Nelson to investigate the terrain",
     "He will collect rock samples around the crater and analyze their chemical composition."),
    ("hanna", "Send Hanna to search for water samples",
     "Her drilling robot will look for the underground ice detected by the radar."),
    ("miquel", "Send Miquel to do general maintenance",
     "He will clean the solar panels and check every corner of the base."),
]

## Tablet placed a bit lower than in the kitchen so it does not overlap the HUD (+29 px)
define TAB_DY = 29

style tab_side_frame:
    background Solid("#0f172af0")
    padding (20, 16)

style small_action_button:
    background Solid("#334155")
    hover_background Solid("#475569")
    insensitive_background Solid("#1e293b")
    padding (10, 5)

style small_action_button_text:
    size 14
    bold True
    color "#f8fafc"
    insensitive_color "#64748b"

## Little bars (3 = full)
screen need_bars(value, kind):
    $ full = "#F4A340" if kind == "hunger" else "#43B8D8"
    $ low = "#b41616" if kind == "hunger" else "#114482"
    hbox:
        spacing 3
        yalign 0.5
        for i in range(3):
            frame:
                xysize (22, 12)
                padding (0, 0)
                background Solid((full if value > 1 else low) if i < value else "#475569")

## Text block used by the Report and Events tabs
screen tablet_text_block(lines):
    vbox:
        spacing 12
        xsize 450
        for kind, t in lines:
            if kind == "title":
                text t size 26 bold True color "#0f172a"
            elif kind == "head":
                text t size 18 bold True color "#0284c7"
            elif kind == "good":
                text t size 17 bold True color "#15803d"
            elif kind == "bad":
                text t size 18 bold True color "#b91c1c"
            else:
                text t size 17 color "#334155"

## Crop of the 4 crew cards from the tablet image, scaled to fit the tablet panel
define CREW_CARDS_CROP = (131, 398, 634, 773)
define CREW_CARDS_SCALE = 450.0 / 634.0

## Position of the water / food bars on each card (already scaled)
define CREW_BAR_POS = [
    ("miquel",    (67, 189), (67, 231)),
    ("nelson",    (314, 189), (314, 231)),
    ("hanna",     (67, 473), (67, 515)),
    ("commander", (314, 468), (314, 511)),
]

screen mini_bars(value, kind, x, y):
    $ full = "#F4A340" if kind == "hunger" else "#43B8D8"
    $ low = "#b41616" if kind == "hunger" else "#114482"
    hbox:
        xpos x
        ypos y
        spacing 4
        for i in range(3):
            frame:
                xysize (28, 14)
                padding (0, 0)
                background Solid((full if value > 1 else low) if i < value else "#BDBDBD")

style ration_button:
    background Solid("#1e293b")
    hover_background Solid("#334155")
    insensitive_background Solid("#94a3b8")
    padding (8, 5)

style ration_button_text:
    size 14
    bold True
    color "#f8fafc"
    insensitive_color "#e2e8f0"

screen crew_tab_content():
    $ rc = ration_cost()
    vbox:
        spacing 14
        xsize 450

        # The four crew cards with their live water and food bars
        fixed:
            xysize (450, 549)
            add Crop(CREW_CARDS_CROP, "images/tablet_personajes.png") zoom CREW_CARDS_SCALE
            for who, wpos, fpos in CREW_BAR_POS:
                use mini_bars(crew_thirst[who], "thirst", wpos[0], wpos[1])
                use mini_bars(crew_hunger[who], "hunger", fpos[0], fpos[1])

        # Rations (scroll down)
        text "RATIONS" size 22 bold True color "#0f172a"
        text "Each ration costs [rc] food or [rc] water." size 15 color "#334155"

        for who in ["miquel", "nelson", "hanna", "commander"]:
            frame:
                background Solid("#ffffffaa")
                padding (12, 8)
                xfill True
                vbox:
                    spacing 6
                    text CREW_NAMES[who] size 17 bold True color "#0f172a"
                    hbox:
                        spacing 8
                        text "Food" size 14 color "#334155" yalign 0.5 min_width 42
                        use need_bars(crew_hunger[who], "hunger")
                        textbutton "FEED  -[rc]":
                            style "ration_button"
                            yalign 0.5
                            sensitive (res_food >= rc and crew_hunger[who] < 3)
                            action Function(feed_crew, who)
                    hbox:
                        spacing 8
                        text "Water" size 14 color "#334155" yalign 0.5 min_width 42
                        use need_bars(crew_thirst[who], "thirst")
                        textbutton "GIVE WATER  -[rc]":
                            style "ration_button"
                            yalign 0.5
                            sensitive (res_water >= rc and crew_thirst[who] < 3)
                            action Function(water_crew, who)

        frame:
            background Solid("#fef3c7dd")
            padding (12, 10)
            xfill True
            vbox:
                spacing 6
                text "PRODUCE FOOD" size 17 bold True color "#92400e"
                text "+[FOOD_PRODUCE_GAIN] food, spending [FOOD_PRODUCE_WATER] water and [FOOD_PRODUCE_ENERGY] energy." size 14 color "#334155"
                textbutton "PRODUCE  +[FOOD_PRODUCE_GAIN] FOOD":
                    style "ration_button"
                    sensitive can_produce_food()
                    action Function(produce_food)

        frame:
            background Solid("#fee2e2dd")
            padding (12, 10)
            xfill True
            vbox:
                spacing 6
                text "HEAT THE BASE" size 17 bold True color "#9a3412"
                text "+[HEAT_GAIN]% temperature, spending [HEAT_ENERGY] energy." size 14 color "#334155"
                textbutton "HEAT  +[HEAT_GAIN]%":
                    style "ration_button"
                    sensitive can_heat_base()
                    action Function(heat_base)

        null height 10

screen day_tablet():

    add Solid("#00000055")

    # ---------------- TABLET ----------------
    # Each tab shows its own tablet image, so exactly one icon is highlighted (100%)
    if day_tab == "events":
        add "images/tablet_eventos.png" xalign 0.5 yalign 0.9 zoom 0.75
    elif day_tab == "crew":
        add "images/tablet_personajes.png" xalign 0.5 yalign 0.9 zoom 0.75
        # Cover the fixed crew cards with the empty panel: the cards are drawn
        # again inside the scrollable area, together with the rations
        add Crop((0, 356, 906, 927), "images/tablet_report.png") zoom 0.75 xpos 620 ypos 373
    else:
        add "images/tablet_report.png" xalign 0.5 yalign 0.9 zoom 0.75

    viewport:
        xpos 725
        ypos 375 + TAB_DY
        xsize 470
        ysize 575
        scrollbars "vertical"
        vscrollbar_xsize 8
        mousewheel True
        draggable True

        if day_tab == "report":
            use tablet_text_block(day_report)
        elif day_tab == "crew":
            use crew_tab_content
        else:
            if day_event:
                use tablet_text_block(day_event)
            else:
                use tablet_text_block([("title", "EVENTS"), ("text", "There are no events for now.")])

    # Tab buttons at the top of the tablet (invisible)
    button:
        xpos 700
        ypos 269 + TAB_DY
        xysize (65, 65)
        background None
        action SetVariable("day_tab", "report")
    button:
        xpos 802
        ypos 269 + TAB_DY
        xysize (65, 65)
        background None
        action SetVariable("day_tab", "crew")
    if day_event:
        button:
            xpos 910
            ypos 269 + TAB_DY
            xysize (65, 65)
            background None
            action [SetVariable("day_tab", "events"), SetVariable("events_seen", True)]
        # Red dot: there is a new event
        if not events_seen:
            frame:
                xpos 966
                ypos 286
                xysize (20, 20)
                background Solid("#ef4444")
    else:
        # Events tab disabled: icon faded out (exactly over the icon)
        frame:
            xpos 902
            ypos 293
            xysize (78, 78)
            background Solid("#f1f5f9b3")

    # ---------------- LEFT PANEL: TODAY'S MISSION ----------------
    if day_needs_mission:
        frame:
            style "tab_side_frame"
            xpos 30
            ypos 128
            xsize 560

            vbox:
                spacing 12
                text "TODAY'S MISSION" size 22 bold True color "#38bdf8"
                text "Based on yesterday's reports, choose one mission:" size 15 color "#94a3b8"
                for who, title, desc in MISSIONS:
                    $ selected = (mission_choice == who)
                    $ mission_label = ("✓ " if selected else "") + title
                    button:
                        xfill True
                        background Solid("#14532d" if selected else "#1e293b")
                        hover_background Solid("#166534" if selected else "#334155")
                        padding (14, 10)
                        action SetVariable("mission_choice", who)
                        vbox:
                            spacing 4
                            text mission_label size 17 bold True color CREW_COLORS[who]
                            text desc size 14 color "#e2e8f0"

    elif day_event:
        frame:
            style "tab_side_frame"
            xpos 30
            ypos 128
            xsize 560
            vbox:
                spacing 10
                text "TODAY'S MISSION" size 22 bold True color "#ef4444"
                text "Open the Events tab (warning icon) to find out what happened." size 16 color "#e2e8f0"

    # ---------------- CONTINUE BUTTON ----------------
    $ can_continue = (mission_choice is not None) if day_needs_mission else (events_seen if day_event else True)
    frame:
        xalign 1.0
        yalign 0.98
        xoffset -30
        background Solid("#0f172af2")
        padding (24, 10)
        vbox:
            spacing 2
            textbutton day_continue_text:
                text_size 22
                text_bold True
                text_color "#38bdf8"
                text_hover_color "#ffffff"
                text_insensitive_color "#475569"
                sensitive can_continue
                action Return()
            if not can_continue:
                if day_needs_mission:
                    text "Choose a mission first" size 14 color "#94a3b8"
                else:
                    text "Read the event first" size 14 color "#94a3b8"


## -------------------------------------------------------------
## Day title card (black screen)
## -------------------------------------------------------------
screen day_title(title, subtitle=""):
    modal True
    add Solid("#000000")
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 12
        text title size 110 bold True color "#f8fafc" xalign 0.5 at warning_fade_in(0.0)
        if subtitle:
            text subtitle size 30 color "#94a3b8" xalign 0.5 at warning_fade_in(0.5)
    timer 3.0 action Return()
    key "dismiss" action Return()
