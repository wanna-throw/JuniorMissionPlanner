## 02_mission_intro.rpy - Restructured introduction: Press Conference -> Mission Control -> Map

label intro_aphrodite:

    # 1. Press conference: public presentation of the program and the Aphrodite 3 mission
    scene bg press_conference with fade

    c "The year is 2052."

    c "Technology has advanced so much that the United Robotics Association (URA) is carrying out the most ambitious program in human history..."

    c "It is called the Aphrodite program, and it has two main goals:"

    c "To search for life beyond Earth..."

    c "And to build long-term scientific settlements on other planets."

    c "Today, the launch of the Aphrodite 3 mission is being announced to the world."

    c "Its main objective is to bring supplies to the settlement built during the Aphrodite 1 and 2 missions..."

    c "And to formally begin the search for biosignatures and life on the surface of Mars."

    # 2. Mission Control Center: your role as commander
    scene bg control_mission with fade

    c "We are now inside the URA Mission Control facilities."

    c "You are the commander of the Aphrodite 3 mission."

    c "The rocket and the crew are ready to depart for the red planet..."

    c "But before setting the final course, you, as commander, must make a crucial decision."

    c "You must analyze the scientific feasibility reports and choose the expedition's landing site."

    c "Loading cartographic map of Mars..."

    # Preload the site card images into VRAM so they open instantly
    $ renpy.start_predict("images/crater_mawrth.png", "images/crater_eberswalde.png", "images/crater_holden.png", "images/crater_gale.png", "images/fondo_tech.png")

    # 3. Interactive Mars map screen (site selection)
    call screen interactive_map

    $ renpy.stop_predict("images/crater_mawrth.png", "images/crater_eberswalde.png", "images/crater_holden.png", "images/crater_gale.png", "images/fondo_tech.png")

# =============================================================
# 4. Confirmation after choosing the landing site on the map
# =============================================================
label confirm_landing:

    scene bg control_mission with dissolve

    c "Landing coordinates locked on [landing_site]."

    c "Telemetry data successfully uploaded to the ship's navigation computer."

    c "All set. Starting the launch countdown..."

    # Transition to the space journey and landing
    scene black with fade

    c "The ship was launched on June 6, 2052, at 18:00 UTC."

    c "After 6 months and 2 days travelling through space..."

    c "And after a difficult orbital insertion and braking maneuver..."

    c "You have successfully landed at [landing_site]!"

    c "About 2 hours have passed since then..."

    # Jump to the ship after landing (wake-up, Miquel, Hanna, coffee...)
    jump ship_wakeup
