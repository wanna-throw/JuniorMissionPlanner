## 03_asentamiento.rpy - Wake-up scene, tablet and arrival at the settlement

label ship_wakeup:

    $ set_chapter(1)

    # Continues inside the ship after landing
    scene bg ship with dissolve

    # 1. The first character (Miquel) enters and says his first line, centered
    $ set_char_pos("Miquel", "center")
    show miquel_halfbody at pos_center with dissolve

    M "Commander..."

    T "Hmm... 5 more minutes."

    M "Come on, wake up, or we'll be way too late to reach the settlement."

    T "What time is it?"

    # 2. The second character (Hanna) enters:
    # - The first character (Miquel) moves to the left (smaller and faded)
    # - The second character (Hanna) appears in the center to say her first line
    $ set_char_pos("Miquel", "left")
    show miquel_halfbody at move_left_idle
    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve

    # 3. The second character says her first line, centered
    H "Wow, that was some nap."

    # 4. AFTER her first line, the second character moves to the right
    $ set_char_pos("Hanna", "right")
    show hanna_halfbody_serious at move_right_talk
    with None
    $ renpy.pause(0.45, hard=False)

    # 5. The conversation continues:
    # Whoever speaks gets back full size and opacity on their side.
    # Whoever is silent automatically shrinks and fades.
    H "You really were tired."

    H "*Turns on the light*"

    H "Good morning. We're on Mars, remember?"

    T "*rubbing your eyes* I just had a good nap... I didn't pass out."

    H "Go make yourself a coffee, we need you wide awake."

    # Leave the scene and head to the kitchen
    hide miquel_halfbody
    hide hanna_halfbody_serious
    with dissolve

    menu:
        "Go to the kitchen":
            pass

# Ship kitchen scene
    scene bg ship_kitchen with fade

    T "*You make yourself a coffee*"

    T "I miss the coffee back home."

    T "*While drinking your coffee, you turn on the tablet to check the mission report and the crew status.*"

    # Initialize the tablet state in the kitchen
    $ current_screen = "report"
    $ crew_hunger = {"miquel": 3, "nelson": 3, "hanna": 3, "commander": 3}
    $ crew_thirst = {"miquel": 3, "nelson": 3, "hanna": 3, "commander": 3}

label tablet_loop:

    call screen kitchen_tablet

    $ tablet_action = _return

    if tablet_action in ["miquel", "hanna", "nelson", "commander"]:
        $ current_screen = "crew"
        call screen character_card(tablet_action)
        $ current_screen = "crew"
        jump tablet_loop

    elif tablet_action == "continue":
        jump settlement_arrival

label crew_tablet:
    jump tablet_loop

label settlement_arrival:

    T "What a great team I have..."

    T "I have high hopes for this mission."

    show nelson_halfbody at pos_center with dissolve

    N "Commander, are you ready?"

    N "We're leaving as soon as possible."

    T "Let's go."

    hide nelson_halfbody with dissolve

    scene black with fade
    "On the way to the settlement..."

    scene bg mars_base with fade
    "We have arrived at the settlement."

    # Dialogue with Hanna: a failure is detected in the electrical system
    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve

    H "Commander! Thank goodness you're here."

    H "I've detected a serious failure in the base's electrical system."

    H "Power isn't reaching the central facilities and the main panels are down."

    T "Do we know what's causing the fault?"

    H "It's an overload in the fuse box. You need to go check it and reconnect the fuses."

    T "Understood. I'll inspect the electrical panel right away."

    H "Be very careful, Commander: you must switch the fuses on in the exact sequence to restore the power flow without damaging the circuit."

    H "I've left the sequence for you on the panel's display. Good luck!"

    hide hanna_halfbody_serious with dissolve

    "You head to the base's power distribution panel..."

    # -------------------------------------------------------------
    # MINIGAME: ELECTRICAL PANEL AND FUSES (imported from test1)
    # -------------------------------------------------------------
    $ sequence = renpy.random.sample(range(6), 6)
    $ fuses = [False, False, False, False, False, False]
    $ current_step = 0
    $ sequence_text = " -> ".join(str(x + 1) for x in sequence)

    $ fuse_event_mode = False
    call screen electrical_panel
    $ unlock("power_up")

    # -------------------------------------------------------------
    # RESOLUTION AFTER COMPLETING THE MINIGAME
    # -------------------------------------------------------------
    scene black with fade

    "CLICK! The last fuse snaps into place."

    "The solar panel guidance systems have come online."

    "The nuclear reactor system has started up. Everything is stable and operational, with perfect safety levels."

    scene bg mars_base with fade

    "A powerful hum runs through the base as the lights and ventilation systems come back to life."

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve

    H "Amazing, Commander! Power is back in every sector."

    H "The electrical system is running at 100%% capacity."

    T "Excellent teamwork. Now that the base has stable power, let's check the status of the rest of our resources."

    hide hanna_halfbody_serious with dissolve

    T "Guys, before we rest, I need each of you to prepare a detailed report from your workstation."

    T "Those reports will define our priority missions for tomorrow."

    jump crew_selection

# =============================================================
# ROUND OF REPORTS AND MISSIONS FOR THE NEXT DAY
# =============================================================
label crew_selection:

    scene bg control_room_crew with dissolve

    call screen crew_selection_screen

    if _return == "tablet":
        jump supplies_report
    elif _return == "meeting":
        jump settlement_final_meeting

# -------------------------------------------------------------
# SUPPLY REPORT (after the three reports): food and water
# -------------------------------------------------------------
label supplies_report:

    scene bg control_room_crew

    T "*You take out the tablet to check the daily supply report.*"

    call screen supplies_tablet

    $ reveal_resources("food", "water")
    $ supplies_checked = True
    "New indicators added at the top of the screen: {b}FOOD{/b} and {b}WATER{/b}."

    T "Food and water are at normal levels. Everything is under control... for now."

    jump crew_selection

# -------------------------------------------------------------
# 1. NELSON'S REPORT: INVESTIGATE THE AREA'S GEOLOGY
# -------------------------------------------------------------
label nelson_report_dialogue:

    scene bg nelson_station with fade

    $ set_char_pos("Nelson", "center")
    show nelson at pos_center with dissolve

    if not report_nelson:
        N "Hi, Commander! Come in. I was running a chemical analysis of the first soil samples we picked up when we landed."

        T "Hi, Nelson. What does the analysis show?"

        show nelson thinking with dissolve

        N "The spectrometer detects hydrated minerals, sulfates... and traces of lithium and silicates."

        N "As a chemist, that's very promising: some of those materials could help us store energy."

        N "Here is my proposal for tomorrow: {b}investigate the terrain{/b} around the base."

        N "If we collect samples from different areas of the crater, I can analyze them here in the lab and tell you exactly which materials we can use."

        show nelson with dissolve

        T "Excellent idea, Nelson. As a geologist, I'd love to see those rock layers up close. Knowing what the ground is made of will tell us which resources we can count on."

        N "Perfect. I'll prepare the sample containers and the portable spectrometer, just in case."

        N "One more thing, Commander. As the medical officer, I've also checked the life-support readings."

        N "{b}Oxygen{/b}: we have [res_oxygen]%% in the tanks and the recyclers are working fine. Levels are normal."

        N "The reserve drops about 10%% every month, so we have around ten months of margin before we run out of air."

        show nelson thinking with dissolve

        N "{b}Temperature{/b}: the base's thermal stability is at [res_thermal]%%. That's normal for [landing_site]."

        N "It loses about 10%% every month. We can recover 15%% by spending 20 energy, but if it ever drops to 20%%, we won't be able to survive here."

        show nelson with dissolve

        $ reveal_resources("oxygen", "thermal")
        "New indicators added at the top of the screen: {b}OXYGEN{/b} and {b}TEMPERATURE{/b}."

        $ report_nelson = True
        "You have received Nelson's proposal: investigate the terrain."

    else:
        N "The spectrometer and the sample containers are ready, Commander."
        T "Perfect, Nelson. Get some rest before we head out."

    hide nelson with dissolve
    jump crew_selection

# -------------------------------------------------------------
# 2. HANNA'S REPORT: SEARCHING FOR LIFE IN WATER SAMPLES
# -------------------------------------------------------------
label hanna_report_dialogue:

    scene bg hanna_station with fade

    $ set_char_pos("Hanna", "center")
    show hanna at pos_center with dissolve

    if not report_hanna:
        H "Commander, I was waiting for you. You have to see what my robotic probes have picked up."

        T "You seem excited, Hanna. What have the sensors detected?"

        show hanna surprised with dissolve

        H "Barely three meters under the Martian regolith... the ground radar found pockets of moisture and salty ice!"

        H "Water is the key ingredient to search for life, and it's also vital for us to survive here."

        show hanna thinking with dissolve

        H "My proposal for tomorrow: {b}search for water samples{/b}."

        H "I can send my drilling robot to extract samples of that underground ice, sealed in sterile capsules so they don't get contaminated."

        show hanna serious with dissolve

        T "An impressive finding, Hanna. If the robot brings back those samples, I'll analyze them myself: as a biologist, searching for microbial life is a dream come true."

        H "Great! I'll program the drilling robot and calibrate its sensors tonight."

        H "Before you go, let me give you the environment and communications readings."

        show hanna thinking with dissolve

        H "{b}Radiation{/b}: here at [landing_site], exposure rises about [res_radiation_rate]%% every month. Right now we're at [res_radiation]%%, so levels are normal."

        H "Our shielding protects us for now, but we'll have to keep an eye on it as the months go by."

        show hanna serious with dissolve

        H "{b}Telecommunications{/b}: the main antenna is aligned and the link with Earth is stable. Antenna status: OK."

        $ reveal_resources("radiation", "antenna")
        "New indicators added at the top of the screen: {b}RADIATION{/b} and {b}ANTENNA{/b}."

        $ report_hanna = True
        "You have received Hanna's proposal: search for water samples."

    else:
        H "The drilling robot is programmed and ready to go, Commander."
        T "Good job, Hanna."

    hide hanna with dissolve
    jump crew_selection

# -------------------------------------------------------------
# 3. MIQUEL'S REPORT: BASE MAINTENANCE
# -------------------------------------------------------------
label miquel_report_dialogue:

    scene bg miquel_station with fade

    $ set_char_pos("Miquel", "center")
    show miquel at pos_center with dissolve

    if not report_miquel:
        M "Hey, Commander! Glad you stopped by the hangar."

        T "Hi, Miquel. How are the vehicles and the module systems doing after the landing?"

        show miquel thinking with dissolve

        M "The landing was rough and Martian dust gets in everywhere. I just checked the hatch seals and the external filters."

        M "Also, after the electrical failure we just fixed, the power lines and auxiliary connectors need a thorough inspection."

        show miquel smiling with dissolve

        M "That's why my report for tomorrow is vital: {b}carry out general maintenance on the base{/b}."

        M "We need to clean the Martian dust off the solar panels, reinforce the airlock pressure seals and tune up the rover engines so the team can go out safely."

        T "Totally agree, Miquel. Without a safe, pressurized base, no scientist can do their job. Your mission is the backbone of the team."

        M "Count on it, boss! Tomorrow I'll leave the base looking brand new."

        M "Oh, and here's the power report."

        M "{b}Energy{/b}: after the repair, the batteries are at [res_energy]%%. That's a normal level for this site."

        M "At first the solar panels add about 1%% per day, and around 15%% per month. Every task that uses power costs energy, so let's use it wisely."

        $ reveal_resources("energy")
        "New indicator added at the top of the screen: {b}ENERGY{/b}."

        $ report_miquel = True
        "You have received Miquel's proposal: general maintenance of the base."

    else:
        M "I've got the torque wrenches and spare filters ready for tomorrow's maintenance."
        T "Well done, Miquel. See you at the final meeting."

    hide miquel with dissolve
    jump crew_selection

# =============================================================
# FINAL CREW MEETING: PLANNING DAY 2
# =============================================================
label settlement_final_meeting:

    $ unlock("team_briefing")

    scene bg mars_base with fade

    "With the three reports in hand, you gather the whole crew in the base's central command room."

    # The three crew members appear at their positions
    $ set_char_pos("Nelson", "left")
    $ set_char_pos("Hanna", "center")
    $ set_char_pos("Miquel", "right")

    show nelson at pos_left_idle
    show hanna at pos_center_idle
    show miquel at pos_right_idle
    with dissolve

    T "Crew of the Aphrodite 3 mission: we have made it through the space journey, the landing and our first electrical emergency."

    T "I've read your three proposals:"

    T "1. {b}Miquel:{/b} general maintenance of the base, cleaning the solar panels and checking the rovers."

    T "2. {b}Nelson:{/b} go out and investigate the terrain, collecting samples to analyze their chemical composition."

    T "3. {b}Hanna:{/b} send the drilling robot to extract samples of the underground ice."

    T "Tomorrow morning I'll decide which mission we carry out first."

    show miquel smiling at pos_right_talk with dissolve
    M "Understood, Commander! Whatever you decide, the base will be in the best hands."

    show hanna serious at pos_center_talk with dissolve
    H "My drilling robot will be ready whenever you need it."

    show nelson at pos_left_talk with dissolve
    N "And my spectrometer is calibrated. We'll be ready."

    T "Great work, everyone, on our first day on the red planet."

    T "Get some good rest tonight, because tomorrow will be the first official day of our new life on Mars."

    # Farewell
    hide nelson
    hide hanna
    hide miquel
    with dissolve

    # Night transition
    scene black with fade

    "The lights of the Martian base dim as it enters its night cycle."

    "The Aphrodite 3 crew rests in their quarters, recovering their energy after a journey of millions of kilometers..."

    "The first day on Mars has come to a successful end."

    # End of Day 1 -> Day 2
    jump day_2



# =============================================================
# INTERACTIVE TABLET SYSTEM AND CHARACTER CARDS (KITCHEN)
# =============================================================

# TABLET VARIABLES
default current_screen = "report"

default supplies_checked = False


# NEEDS INDICATOR (FOOD AND WATER)
screen need_indicator(value, kind, x, y):

    if kind == "hunger":
        if value == 3:
            $ color = "#F4A340"
        elif value == 2:
            $ color = "#e5622a"
        else:
            $ color = "#b41616"

    elif kind == "thirst":
        if value == 3:
            $ color = "#43B8D8"
        elif value == 2:
            $ color = "#177fab"
        else:
            $ color = "#114482"

    hbox:
        xpos x
        ypos y
        spacing 4

        for i in range(3):
            if i < value:
                frame:
                    xsize 32
                    ysize 16
                    padding (0, 0)
                    background Solid(color)
            else:
                frame:
                    xsize 32
                    ysize 16
                    padding (0, 0)
                    background Solid("#BDBDBD")


# TABLET SCREEN
screen kitchen_tablet():

    # Background shadow over the kitchen
    add Solid("#00000066")

    # NOTIFICATION IN THE TOP-LEFT CORNER (WITHOUT COVERING THE TABLET)
    frame:
        xpos 50
        ypos 120
        xsize 500
        background Solid("#0f172ae6")
        padding (24, 20)

        vbox:
            spacing 10

            hbox:
                spacing 10
                text "ℹ️" size 22
                text "TABLET INSTRUCTIONS" size 19 bold True color "#38bdf8"

            null height 2

            text "1. Go to the top of the tablet and tap the {b}Crew icon{/b}." size 16 color "#e2e8f0"

            text "2. Once inside, {b}click on each person{/b} to view their full body and their profile." size 16 color "#e2e8f0"

            null height 2

            text "• When you have finished reviewing the team, press the button at the bottom to continue the mission." size 14 italic True color "#94a3b8"

    if current_screen == "report":
        add "images/tablet_report.png":
            xalign 0.5
            yalign 0.65
            zoom 0.75

        viewport:
            xpos 725
            ypos 375
            xsize 470
            ysize 575
            scrollbars "vertical"
            vscrollbar_xsize 8
            mousewheel True
            draggable True

            vbox:
                spacing 14

                text "MISSION REPORT":
                    size 26
                    bold True
                    color "#0f172a"

                text "APHRODITE 3 PROGRAM (2052)":
                    size 17
                    bold True
                    color "#0284c7"

                text "The URA's Aphrodite program has two fundamental, historic goals: the formal search for biosignatures of extraterrestrial life and a permanent scientific settlement on Mars.":
                    size 17
                    color "#334155"

                text "SELECTED LANDING ZONE:":
                    size 17
                    bold True
                    color "#0284c7"

                text "After evaluating the options at Mission Control, the Commander set the coordinates to [landing_site], a key region with sedimentary formations and high biological potential.":
                    size 17
                    color "#334155"

                text "SPACE JOURNEY:":
                    size 17
                    bold True
                    color "#0284c7"

                text "The ship lifted off on June 6, 2052 (18:00 UTC). After 6 months and 2 days crossing deep space and a complex orbital braking maneuver, the module touched down successfully.":
                    size 17
                    color "#334155"

                text "STATUS AFTER LANDING:":
                    size 17
                    bold True
                    color "#0284c7"

                text "About 2 hours have passed since touchdown. After a restorative nap in the module, the crew meets in the kitchen to plan the trip to the Martian base.":
                    size 17
                    color "#334155"

                null height 10

                text "💡 Check the 'Crew' tab to review the status and profile of each team member.":
                    size 15
                    italic True
                    color "#64748b"


    elif current_screen == "crew":
        add "images/tablet_personajes.png":
            xalign 0.5
            yalign 0.65
            zoom 0.75

        # Indicators with full supplies (3/3)
        use need_indicator(crew_hunger["miquel"], "hunger", 790, 620)
        use need_indicator(crew_thirst["miquel"], "thirst", 790, 575)

        use need_indicator(crew_hunger["hanna"], "hunger", 790, 920)
        use need_indicator(crew_thirst["hanna"], "thirst", 790, 875)

        use need_indicator(crew_hunger["nelson"], "hunger", 1050, 620)
        use need_indicator(crew_thirst["nelson"], "thirst", 1050, 575)

        use need_indicator(crew_hunger["commander"], "hunger", 1050, 915)
        use need_indicator(crew_thirst["commander"], "thirst", 1050, 870)

        # 4 INVISIBLE BUTTONS OVER EACH CHARACTER:
        # 1. Miquel (Top left)
        button:
            xpos 660
            ypos 370
            xsize 270
            ysize 285
            background None
            action Return("miquel")

        # 2. Nelson (Top right)
        button:
            xpos 940
            ypos 370
            xsize 270
            ysize 285
            background None
            action Return("nelson")

        # 3. Hanna (Bottom left)
        button:
            xpos 660
            ypos 670
            xsize 270
            ysize 285
            background None
            action Return("hanna")

        # 4. Commander / You (Bottom right)
        button:
            xpos 940
            ypos 670
            xsize 270
            ysize 285
            background None
            action Return("commander")


    # TOP NAVIGATION BUTTONS ON THE TABLET
    button:
        xpos 700
        ypos 269
        xsize 65
        ysize 65
        background None
        action SetVariable("current_screen", "report")

    button:
        xpos 802
        ypos 269
        xsize 65
        ysize 65
        background None
        action SetVariable("current_screen", "crew")


    # BOTTOM BUTTON: PUT AWAY THE TABLET AND CONTINUE TO THE SETTLEMENT
    frame:
        xalign 0.5
        ypos 1010
        background Solid("#0f172af2")
        padding (24, 8)

        textbutton "PUT AWAY TABLET AND CONTINUE MISSION ▶":
            text_size 20
            text_bold True
            text_color "#38bdf8"
            text_hover_color "#ffffff"
            action Return("continue")


# CHARACTER DETAIL SCREEN (IN THE KITCHEN)
screen character_card(who):

    # Kitchen background
    add "bg ship_kitchen"

    # Darken the background to highlight the profile card
    add Solid("#00000055")

    # If it's a crewmate (Miquel, Hanna, Nelson): blue-gray box with full-body image and profile
    if who in ["miquel", "hanna", "nelson"]:
        frame:
            xalign 0.5
            yalign 0.44
            xsize 1460
            ysize 820
            background Solid("#1e293bee")
            padding (40, 30)

            hbox:
                spacing 40
                yalign 0.5

                # Full-body image container
                frame:
                    xsize 440
                    ysize 750
                    background Solid("#0f172a99")
                    padding (10, 10)

                    if who == "miquel":
                        add "images/characters/miquel_cuerpoentero.png":
                            xalign 0.5
                            yalign 1.0
                            ysize 730
                            fit "contain"
                    elif who == "hanna":
                        add "images/characters/hanna_cuerpoentero.png":
                            xalign 0.5
                            yalign 1.0
                            ysize 730
                            fit "contain"
                    elif who == "nelson":
                        add "images/characters/nelson_cuerpoentero.png":
                            xalign 0.5
                            yalign 1.0
                            ysize 730
                            fit "contain"

                # Technical profile block
                vbox:
                    spacing 16
                    xsize 900
                    yalign 0.5

                    if who == "miquel":
                        text "MIQUEL":
                            size 44
                            bold True
                            color "#7ed957"

                        text "Mission Pilot & Mechanical Engineer":
                            size 24
                            bold True
                            color "#94a3b8"

                        null height 10

                        frame:
                            background Solid("#0f172acc")
                            padding (25, 20)
                            xfill True

                            vbox:
                                spacing 12
                                text "{b}• Age:{/b} 29 years old" size 20 color "#e2e8f0"
                                text "{b}• Origin:{/b} Catalan / American" size 20 color "#e2e8f0"
                                text "{b}• Specialty:{/b} Orbital piloting, mechanical landing systems and habitat maintenance." size 20 color "#e2e8f0"
                                text "{b}• Mission role:{/b} In charge of the Aphrodite 3 ship's navigation maneuvers, the rovers' drive systems and the mechanical integrity of the base." size 20 color "#e2e8f0"
                                text "{b}• Supply status:{/b} Food 3/3 | Water 3/3 (Fully operational)" size 20 color "#7ed957"

                    elif who == "hanna":
                        text "HANNA":
                            size 44
                            bold True
                            color "#ff751f"

                        text "Robotics & Telecommunications Specialist":
                            size 24
                            bold True
                            color "#94a3b8"

                        null height 10

                        frame:
                            background Solid("#0f172acc")
                            padding (25, 20)
                            xfill True

                            vbox:
                                spacing 12
                                text "{b}• Age:{/b} 31 years old" size 20 color "#e2e8f0"
                                text "{b}• Origin:{/b} Japanese" size 20 color "#e2e8f0"
                                text "{b}• Specialty:{/b} Robotics, space telecommunication networks and robotic probes." size 20 color "#e2e8f0"
                                text "{b}• Mission role:{/b} Managing the link with Earth, maintaining the antennas and sensors, and directing the drilling and prospecting robots." size 20 color "#e2e8f0"
                                text "{b}• Supply status:{/b} Food 3/3 | Water 3/3 (Fully operational)" size 20 color "#ff751f"

                    elif who == "nelson":
                        text "NELSON":
                            size 44
                            bold True
                            color "#f423a3"

                        text "Expedition Medical Officer & Chemist":
                            size 24
                            bold True
                            color "#94a3b8"

                        null height 10

                        frame:
                            background Solid("#0f172acc")
                            padding (25, 20)
                            xfill True

                            vbox:
                                spacing 12
                                text "{b}• Age:{/b} 34 years old" size 20 color "#e2e8f0"
                                text "{b}• Origin:{/b} Senegalese" size 20 color "#e2e8f0"
                                text "{b}• Specialty:{/b} Space medicine, analytical chemistry and life support." size 20 color "#e2e8f0"
                                text "{b}• Mission role:{/b} Looking after the crew's health, chemical analysis of soil samples and supervision of the life-support systems (air, water and temperature)." size 20 color "#e2e8f0"
                                text "{b}• Supply status:{/b} Food 3/3 | Water 3/3 (Fully operational)" size 20 color "#f423a3"

    # If the player clicks on themselves (Commander): profile only, no full-body picture
    elif who == "commander":
        frame:
            xalign 0.5
            yalign 0.44
            xsize 1140
            ysize 680
            background Solid("#1e293bee")
            padding (50, 40)

            vbox:
                spacing 20
                yalign 0.5

                text "COMMANDER (YOU)":
                    size 44
                    bold True
                    color "#8c52ff"

                text "Aphrodite 3 Expedition Leader & Scientific Director":
                    size 24
                    bold True
                    color "#94a3b8"

                frame:
                    background Solid("#0f172acc")
                    padding (35, 30)
                    xfill True

                    vbox:
                        spacing 14
                        text "{b}• Rank:{/b} Commander-in-Chief of the Aphrodite 3 Mars mission." size 21 color "#e2e8f0"
                        text "{b}• Specialty:{/b} Planetary biologist and geologist." size 21 color "#e2e8f0"
                        text "{b}• Responsibilities:{/b} Highest authority for strategic decisions, assignment and approval of operational missions, and scientific coordination of the settlement." size 21 color "#e2e8f0"
                        text "{b}• Main Objective:{/b} Ensure the crew's survival, lead the search for biosignatures and secure long-term habitability on Mars." size 21 color "#e2e8f0"
                        text "{b}• Supply status:{/b} Food 3/3 | Water 3/3 (In perfect condition)" size 21 color "#8c52ff"

    # Button in the bottom-left corner: back to the tablet
    frame:
        xpos 60
        ypos 970
        background Solid("#0f172af5")
        padding (22, 10)

        textbutton "◀  BACK TO THE TABLET":
            text_size 22
            text_bold True
            text_color "#38bdf8"
            text_hover_color "#ffffff"
            action Return()
