## progress_system.rpy - Route, story progress (%) and achievements.
## The badge in the top-left corner is always visible during the game.

## -------------------------------------------------------------
## Chapters of the story (used for the progress %)
## -------------------------------------------------------------
define CHAPTERS = ["Launch", "Day 1", "Day 2", "Day 3", "Day 4", "Week 2", "Week 3",
                   "Week 4", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6", "Month 7",
                   "Month 8", "Month 9", "Month 10", "Ending"]

default chapter = 0
default route = []                  # short labels of every decision taken
default mission_history = []        # crew member who led each mission, in order
default samples_collected = 0       # scientific samples brought back by the expeditions
default crew_neglect = 0            # times a crew member was left with an empty food/water bar
default food_produced_times = 0

## -------------------------------------------------------------
## Achievements (saved across all playthroughs)
## -------------------------------------------------------------
define ACHIEVEMENTS = [
    ("touchdown", "Touchdown", "Land on Mars."),
    ("power_up", "Power Up", "Restore the base's power on Day 1."),
    ("team_briefing", "Team Briefing", "Receive the reports of the whole crew."),
    ("rock_hound", "Rock Hound", "Send Nelson to lead an expedition."),
    ("signal_hunter", "Signal Hunter", "Send Hanna to lead an expedition."),
    ("off_road", "Off-Road Pilot", "Send Miquel to lead an expedition."),
    ("team_player", "Team Player", "Let each crew member lead at least one mission in the same run."),
    ("sun_chaser", "Sun Chaser", "Realign the solar panel after the sandstorm."),
    ("electrician", "Electrician", "Repair the short circuit in Month 3."),
    ("greenhouse", "Green Thumb", "Produce food 3 times in the same run."),
    ("one_month", "One Month on Mars", "Survive the first month."),
    ("caretaker", "Caretaker", "Finish a run without ever leaving a crew member with an empty bar."),
    ("cartographer", "Cartographer", "Land at all four candidate sites (across runs)."),
    ("back_home", "Back Home Alive", "Evacuate the base and return to Earth."),
    ("lessons", "Lessons Learned", "Get the bad result at the end of the mission."),
    ("life_beyond", "Life Beyond Earth", "Get the best ending: proof of life on Mars."),
]

default persistent.achievements = None
default persistent.sites_landed = None
default persistent.endings_seen = None

init python:
    ACH_TITLES = {a[0]: a[1] for a in ACHIEVEMENTS}

    def _ensure_persistent():
        if persistent.achievements is None:
            persistent.achievements = set()
        if persistent.sites_landed is None:
            persistent.sites_landed = set()
        if persistent.endings_seen is None:
            persistent.endings_seen = set()

    def unlock(ach_id):
        _ensure_persistent()
        if ach_id not in persistent.achievements:
            persistent.achievements.add(ach_id)
            renpy.save_persistent()
            renpy.notify("★ ACHIEVEMENT UNLOCKED: " + ACH_TITLES.get(ach_id, ach_id))

    def achievements_count():
        _ensure_persistent()
        return len(persistent.achievements & set(ACH_TITLES))

    def set_chapter(i):
        store.chapter = max(store.chapter, i)

    def story_percent():
        return int(round(100.0 * store.chapter / (len(CHAPTERS) - 1)))

    def add_route(label):
        store.route = store.route + [label]

    def route_text():
        return "  ›  ".join(store.route) if store.route else "—"

    def record_mission(who):
        """Saves who led a mission, applies the repeat rule and unlocks achievements."""
        if store.mission_history and store.mission_history[-1] == who:
            store.repeat_penalty_pending = who
        store.mission_history = store.mission_history + [who]
        unlock({"nelson": "rock_hound", "hanna": "signal_hunter", "miquel": "off_road"}[who])
        if {"nelson", "hanna", "miquel"} <= set(store.mission_history):
            unlock("team_player")

    def record_landing(site_key, site_short):
        _ensure_persistent()
        persistent.sites_landed.add(site_key)
        add_route(site_short)
        if len(persistent.sites_landed) >= 4:
            unlock("cartographer")

    def check_crew_neglect():
        """Counts crew members left with an empty bar after the player could give rations."""
        n = 0
        for k in store.crew_hunger:
            if store.crew_hunger[k] <= 0 or store.crew_thirst[k] <= 0:
                n += 1
        store.crew_neglect += n
        return n

    def ending_reached(ending_id):
        _ensure_persistent()
        persistent.endings_seen.add(ending_id)
        set_chapter(len(CHAPTERS) - 1)
        if store.crew_neglect == 0 and ending_id in ("good", "bad"):
            unlock("caretaker")
        renpy.save_persistent()

    config.overlay_screens.append("progress_badge")

## -------------------------------------------------------------
## Badge: always visible during the game (top-left corner)
## -------------------------------------------------------------
screen progress_badge():
    zorder 55
    if not main_menu and not _menu and not renpy.get_screen("warning_screen") and not renpy.get_screen("achievements_screen"):
        $ pct = story_percent()
        $ chap = CHAPTERS[chapter]
        $ rtxt = route_text()
        $ achtxt = "★ Achievements %d/%d" % (achievements_count(), len(ACHIEVEMENTS))
        frame:
            xpos 8
            ypos 8
            xsize 250
            background Solid("#0f172ae6")
            padding (12, 8)
            vbox:
                spacing 3
                hbox:
                    spacing 8
                    text "STORY" size 13 bold True color "#94a3b8" yalign 0.5
                    bar:
                        value StaticValue(chapter, len(CHAPTERS) - 1)
                        xsize 90
                        ysize 10
                        yalign 0.5
                        left_bar Solid("#38bdf8")
                        right_bar Solid("#334155")
                        thumb None
                    text "[pct]%" size 14 bold True color "#f8fafc" yalign 0.5
                text "Chapter: [chap]" size 13 color "#cbd5e1"
                text "Route: [rtxt!q]" size 12 color "#fbbf24"
                textbutton achtxt:
                    padding (0, 0)
                    text_size 13
                    text_bold True
                    text_color "#4ade80"
                    text_hover_color "#ffffff"
                    action Show("achievements_screen")

## -------------------------------------------------------------
## Achievements window (from the badge or the main menu)
## -------------------------------------------------------------
screen achievements_screen():
    modal True
    zorder 100
    $ _ensure_persistent()
    $ done = persistent.achievements
    $ total_pct = int(round(100.0 * achievements_count() / len(ACHIEVEMENTS)))
    $ summary = "Game completion: %d%%   ·   Unlocked: %d / %d   ·   Endings seen: %d / 8" % (total_pct, achievements_count(), len(ACHIEVEMENTS), len(persistent.endings_seen))

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 900
        background Solid("#0f172af7")
        padding (40, 30)

        vbox:
            spacing 12
            text "ACHIEVEMENTS" size 34 bold True color "#38bdf8" xalign 0.5
            text summary size 18 color "#cbd5e1" xalign 0.5

            viewport:
                ysize 680
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    spacing 8
                    for aid, title, desc in ACHIEVEMENTS:
                        $ ok = aid in done
                        frame:
                            xsize 990
                            background Solid("#14532d" if ok else "#1e293b")
                            padding (16, 10)
                            hbox:
                                spacing 16
                                text ("★" if ok else "☆") size 30 color ("#facc15" if ok else "#475569") yalign 0.5
                                vbox:
                                    yalign 0.5
                                    text title size 20 bold True color ("#f8fafc" if ok else "#94a3b8")
                                    text desc size 15 color ("#d1fae5" if ok else "#64748b")

            textbutton "CLOSE":
                xalign 0.5
                text_size 22
                text_bold True
                text_color "#38bdf8"
                text_hover_color "#ffffff"
                action Hide("achievements_screen")

## Achievement pop-ups appear centered below the HUD, so they never cover the badge
style notify_frame:
    xalign 0.5
    ypos 110
