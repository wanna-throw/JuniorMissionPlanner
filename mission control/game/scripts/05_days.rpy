## 05_days.rpy - Days 2, 3 and 4 (survival system, 60 Seconds style)
##
## Every morning: the night passes (+1 energy) and, from Day 3, the crew gets
## hungry and thirsty (-1 food bar and -1 water bar each). The player reads the
## report on the tablet, gives rations, can produce food and, on some days,
## chooses a mission. During the first week the environment (temperature,
## oxygen and radiation) stays stable so the player can get used to the game.

## =============================================================
## DAY 2 - The first official day: choose a mission
## =============================================================
label day_2:

    $ day = 2
    $ set_chapter(2)
    $ night_passes()

    call screen day_title("DAY 2", "The first official day of our new life on Mars")

    scene bg control_room_crew with fade

    T "*Good morning. Coffee in hand, you open the tablet to read today's report.*"

    $ day_report = [
        ("title", "REPORT - DAY 2"),
        ("text", "You have just spent your first night at the Mars base."),
        ("good", "During the night you gained +1 energy."),
        ("head", "THE CREW"),
        ("text", "Open the Crew tab to see everyone's status: how hungry and thirsty they are. For now, the whole crew is healthy."),
        ("text", "You can decide whether to feed them or not (each ration costs food or water): scroll down in the Crew tab to find the buttons. There you can also produce more food (spending 10 water and 10 energy)."),
        ("head", "TODAY"),
        ("text", "Based on the reports you received yesterday, what will you do today? Choose a mission on the left."),
        ("head", "EVENTS"),
        ("text", "There are no events for now."),
    ]
    $ day_event = None
    $ events_seen = False
    $ day_needs_mission = True
    $ mission_choice = None
    $ day_tab = "report"
    $ day_continue_text = "START THE MISSION ▶"

    $ day_report = add_passive_line(day_report)
    call screen day_tablet

    $ mission_by_day[day] = mission_choice
    $ record_mission(mission_choice)
    $ add_route(CREW_NAMES[mission_choice])
    $ samples_collected += 1

    if mission_choice == "nelson":
        jump day_2_mission_nelson
    elif mission_choice == "hanna":
        jump day_2_mission_hanna
    else:
        jump day_2_mission_miquel

# ---------------- Route 1: Nelson investigates the terrain ----------------
label day_2_mission_nelson:

    scene bg expedition_day with fade

    "Nelson leads the expedition, but nobody stays behind: the whole crew goes out with him to explore the terrain around the base."

    N "Spectrometer ready. Let's see what this crater is made of."

    T "Take samples from every rock layer, Nelson. I'll map the strata as we go."

    H "My robot can carry the heavy containers back to the rover."

    M "And I'll keep an eye on the rover's batteries."

    N "Look at this dark vein in the rock... I'll analyze it in the lab tonight."

    "After hours of work, the whole team returns to the base with the containers full of samples."

    jump day_2_night

# ---------------- Route 2: Hanna searches for water ----------------
label day_2_mission_hanna:

    scene bg expedition_night with fade

    "Hanna leads the search, and the whole crew goes with her to a nearby cave, where the radar detected ice."

    H "The robot is going in. Signal stable... starting the drill."

    T "Careful, Hanna. Keep the sample capsules sealed."

    N "Air and suit temperatures are fine for everyone. We can stay a bit longer."

    H "Got it! The sensors are detecting something frozen down there."

    "Late at night, the whole team returns to the base with the first samples."

    jump day_2_night

# ---------------- Route 3: Miquel maintains the base ----------------
label day_2_mission_miquel:

    scene bg solar_panels with fade

    "Miquel spends the day cleaning the dust off the solar panels and checking every corner of the base."

    M "These panels were covered in dust! Now they'll charge much better."

    T "Good work. Check the storage room too, nobody has opened it since the last mission."

    M "On it, boss. Let's see what's in there..."

    "By sunset, the base is clean, tidy and ready for the coming days."

    jump day_2_night

label day_2_night:

    scene black with fade

    "Night falls on Mars. The crew rests after a long day of work..."

    jump day_3


## =============================================================
## DAY 3 - Results of yesterday's mission
## =============================================================
label day_3:

    $ day = 3
    $ set_chapter(3)
    $ night_passes()
    $ crew_gets_hungry()
    $ yesterday = mission_by_day.get(2)

    # Result of Day 2's mission
    if yesterday == "nelson":
        $ res_energy += 5
    elif yesterday == "hanna":
        $ res_water += 5
    else:
        $ res_energy += 5
    $ clamp_resources()

    call screen day_title("DAY 3")

    scene bg control_room_crew with fade

    T "*A new day begins. You open the tablet to read the report.*"

    if yesterday == "nelson":
        $ mission_result = [
            ("head", "YESTERDAY'S MISSION"),
            ("text", "The whole crew went out on Nelson's expedition to investigate the terrain, and Nelson found lithium, silicates and rare metals."),
            ("text", "With these materials, you were able to generate energy."),
            ("good", "+5 energy"),
        ]
    elif yesterday == "hanna":
        $ mission_result = [
            ("head", "YESTERDAY'S MISSION"),
            ("text", "The whole crew went out with Hanna to search for water, and her robot found a deposit of frozen water."),
            ("good", "+5 water"),
        ]
    else:
        $ mission_result = [
            ("head", "YESTERDAY'S MISSION"),
            ("text", "While Miquel was tidying up the base, he found some hidden batteries in the storage room."),
            ("good", "+5 energy"),
        ]

    $ day_report = [
        ("title", "REPORT - DAY 3"),
        ("good", "During the night you gained +1 energy."),
    ] + mission_result + [
        ("head", "ENVIRONMENT"),
        ("text", "Thermal stability, oxygen and radiation remain stable."),
        ("head", "THE CREW"),
        ("bad", "Everyone has lost 1 food bar and 1 water bar."),
        ("text", "Open the Crew tab and scroll down to give them rations."),
        ("head", "EVENTS"),
        ("text", "There are no events for now."),
    ]
    $ day_event = None
    $ events_seen = False
    $ day_needs_mission = False
    $ mission_choice = None
    $ day_tab = "report"
    $ day_continue_text = "END THE DAY ▶"

    $ day_report = add_passive_line(day_report)
    call screen day_tablet

    # Short scene with the person who did yesterday's mission
    if yesterday == "nelson":
        scene bg nelson_station with fade
        $ set_char_pos("Nelson", "center")
        show nelson at pos_center with dissolve
        N "The analysis is finished, Commander: lithium, silicates and rare metals."
        T "And we've already turned them into battery cells. Great job, Nelson."
        show nelson thinking with dissolve
        N "If the ground has more of these, we could build a proper energy reserve."
        hide nelson with dissolve
    elif yesterday == "hanna":
        scene bg hanna_station with fade
        $ set_char_pos("Hanna", "center")
        show hanna surprised at pos_center with dissolve
        H "Commander! The robot's samples confirm it: it's a whole deposit of frozen water!"
        T "Then I'll start analyzing them in search of microbial life. And that water will keep us going."
        show hanna serious with dissolve
        H "I'll keep the robot mapping the deposit."
        hide hanna with dissolve
    else:
        scene bg miquel_station with fade
        $ set_char_pos("Miquel", "center")
        show miquel smiling at pos_center with dissolve
        M "Look what I found in the storage room, boss: spare batteries, fully charged!"
        T "The previous missions must have left them. Connect them to the grid."
        show miquel with dissolve
        M "Already done. The base has never been so clean."
        hide miquel with dissolve

    scene black with fade

    "The rest of the day passes calmly. Night falls over the base..."

    jump day_4


## =============================================================
## DAY 4 - EVENT: Sandstorm
## =============================================================
label day_4:

    $ day = 4
    $ set_chapter(4)
    $ night_passes()
    $ crew_gets_hungry()

    call screen day_title("DAY 4")

    scene black

    "During the night, a strange noise wakes you up: the walls of the base are shaking..."

    scene bg control_room_crew with fade

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve

    H "Commander! A sandstorm hit us during the night. Check the tablet, quickly!"

    hide hanna_halfbody_serious with dissolve

    $ day_report = [
        ("title", "REPORT - DAY 4"),
        ("good", "During the night you gained +1 energy."),
        ("text", "Yesterday was a quiet day and everything went normally."),
        ("bad", "However, tonight there has been a catastrophic event: a sandstorm has hit your base and knocked a solar panel out of position."),
        ("text", "Go to the Events tab to find out more."),
        ("head", "THE CREW"),
        ("bad", "Everyone has lost 1 food bar and 1 water bar."),
        ("text", "Open the Crew tab and scroll down to give them rations."),
    ]
    $ day_event = [
        ("title", "SANDSTORM"),
        ("text", "During the night, a strong sandstorm hit the base. The wind moved one of the solar panels and now it is not pointing at the Sun correctly."),
        ("text", "It must be fixed as soon as possible! The solar panels provide the energy needed to keep the base running."),
        ("head", "TODAY'S MISSION"),
        ("text", "Adjust the solar panel so it is back in the correct position."),
        ("bad", "WARNING!"),
        ("text", "You only have ONE attempt to put the lever at the right angle."),
        ("text", "If it fails, the panel will stay misaligned for the rest of the mission: the base will produce 25% less energy from then on (every night, every week and every month you will receive only 75% of the normal energy). You will have to save electricity to keep the life support, the heating and the greenhouse running."),
    ]
    $ events_seen = False
    $ day_needs_mission = False
    $ mission_choice = None
    $ day_tab = "report"
    $ day_continue_text = "GO FIX THE SOLAR PANEL ▶"

    $ day_report = add_passive_line(day_report)
    call screen day_tablet

    jump solar_panel_event


## =============================================================
## END OF WEEK 1
## =============================================================
label week_1_end:

    scene black with fade

    if solar_efficiency >= 100:
        "The solar panel is pointing at the Sun again and the batteries start charging."

        "The panel guidance systems are back online. All systems are stable and operational."
    else:
        "The base keeps running, but with one panel misaligned the batteries charge more slowly."

    call screen week_end_screen

    jump week_2


screen week_end_screen():
    modal True
    add Solid("#000000")

    vbox:
        xalign 0.5
        yalign 0.45
        spacing 22

        text "END OF WEEK 1" size 100 bold True color "#38bdf8" xalign 0.5 at warning_fade_in(0.0)
        text "You have survived your first days on Mars." size 30 color "#e2e8f0" xalign 0.5 at warning_fade_in(0.5)

        null height 10

        frame:
            xalign 0.5
            background Solid("#0f172a")
            padding (40, 24)
            at warning_fade_in(1.0)
            vbox:
                spacing 8
                text "BASE STATUS" size 22 bold True color "#38bdf8" xalign 0.5
                text "Energy: [res_energy]%   ·   Water: [res_water]%   ·   Food: [res_food]%" size 22 color "#e2e8f0" xalign 0.5
                text "Oxygen: [res_oxygen]%   ·   Temperature: [res_thermal]%   ·   Radiation: [res_radiation]%" size 22 color "#e2e8f0" xalign 0.5
                text "Solar energy production: [solar_efficiency]%" size 22 color ("#e2e8f0" if solar_efficiency >= 100 else "#fbbf24") xalign 0.5

        null height 10
        text "Week 2 begins..." size 26 italic True color "#94a3b8" xalign 0.5 at warning_fade_in(1.5)

    textbutton "CONTINUE":
        xalign 0.5
        yalign 0.92
        text_size 26
        text_bold True
        text_color "#38bdf8"
        text_hover_color "#ffffff"
        action Return()
