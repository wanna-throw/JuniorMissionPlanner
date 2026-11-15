
#=========================================
# CHARACTERS
#=========================================

define Miquel = Character("Miquel", color='#ff0000')


#=========================================
# VARIABLES
#=========================================

# Event 1: Electrical panel
default fuses = [False, False, False, False, False, False]
default sequence = []
default current_step = 0
default sequence_text = ""


# Event 2: Solar panel
default arrow_angle = 0
default target_angle = 90
default selected_angle = 0
default arrow_message = ""


# Arrow position for each angle
# Format: (horizontal position, vertical position)
default arrow_positions = {
    0:   (0.39, 0.97),
    45:  (0.42, 0.8),
    90:  (0.5, 0.7),
    135: (0.58, 0.8),
    180: (0.62, 0.97)
}


# Arrow pivot offsets
default pivot_offset_x = 0
default pivot_offset_y = 0


#=========================================
# EVENT 1: ELECTRICAL PANEL
#=========================================

screen cuadro_electrico():

    add "images/cuadro_electrico.png":
        xalign 0.5
        yalign 0.5
        zoom 2.5

    $ x_start = 1180
    $ y_start = 450

    $ x_spacing = 495
    $ y_spacing = 800

    for i in range(6):

        $ x_pos = x_start + (i % 3) * x_spacing
        $ y_pos = y_start + (i // 3) * y_spacing

        $ fuse_image = Transform(
            "images/plomo_on.png" if fuses[i] else "images/plomo_off.png",
            zoom=0.48
        )

        imagebutton:
            idle fuse_image
            hover fuse_image
            xpos x_pos
            ypos y_pos
            sensitive not fuses[i]

            action If(
                i == sequence[current_step],
                [
                    SetVariable("fuses", fuses[:i] + [True] + fuses[i+1:]),
                    SetVariable("current_step", current_step + 1),
                    If(current_step + 1 == 6, Return())
                ],
                Show("wrong_sequence")
            )


#-----------------------------------------
# ERROR SCREEN - ELECTRICAL PANEL
#-----------------------------------------

screen wrong_sequence():

    modal True

    add "#0009"

    frame:
        xalign 0.5
        yalign 0.5

        xsize 1200
        ysize 750

        background Solid("#20242e")
        padding (70, 60)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 35

            text "INCORRECT SEQUENCE":
                size 75
                color "#ff4b4b"
                bold True
                xalign 0.5

            text "You activated the wrong fuse.":
                size 45
                color "#ffffff"
                xalign 0.5

            text "The correct sequence was:":
                size 40
                color "#bfc5d2"
                xalign 0.5

            text "[sequence_text]":
                size 55
                color "#ffcc66"
                bold True
                xalign 0.5

            null height 20

            textbutton "TRY AGAIN":
                xalign 0.5
                text_size 48
                text_color "#ffffff"
                text_hover_color "#ffffff"
                background Solid("#b83232")
                hover_background Solid("#e04444")
                xpadding 100
                ypadding 35

                action [
                    Hide("wrong_sequence"),
                    SetVariable("fuses", [False, False, False, False, False, False]),
                    SetVariable("current_step", 0)
                ]


#=========================================
# EVENT 2: SOLAR PANEL
#=========================================

#-----------------------------------------
# SOLAR PANEL - ARROW DISPLAY
#-----------------------------------------

screen solar_arrow_display():

    $ import math

    # Get the position for the current angle
    $ arrow_x, arrow_y = arrow_positions[arrow_angle]

    # Calculate rotation
    $ rotation = arrow_angle - 135
    $ radians = math.radians(rotation)

    # Calculate image displacement
    $ offset_x = (
        pivot_offset_x * math.cos(radians)
        - pivot_offset_y * math.sin(radians)
    )

    $ offset_y = (
        pivot_offset_x * math.sin(radians)
        + pivot_offset_y * math.cos(radians)
    )

    # Display arrow
    add Transform(
        "images/ui_arrow.png",
        rotate=rotation
    ):
        xalign arrow_x
        yalign arrow_y
        xoffset -offset_x
        yoffset -offset_y


#-----------------------------------------
# SOLAR PANEL - ANGLE SELECTION
#-----------------------------------------

screen solar_arrow():

    # Display initial arrow
    use solar_arrow_display

    frame:
        xalign 0.5
        yalign 0.98

        background Solid("#20242e")
        padding (25, 20)

        hbox:
            spacing 12
            yalign 0.5

            # Available angles
            for angle in [0, 45, 90, 135, 180]:

                $ angle_text_color = "#ffcc00" if selected_angle == angle else "#ffffff"
                $ angle_background = Solid("#725b16") if selected_angle == angle else Solid("#414653")

                textbutton "[angle]°":
                    xsize 110
                    ysize 90

                    text_size 48
                    text_bold True
                    text_color angle_text_color
                    text_xalign 0.5
                    text_yalign 0.5

                    background angle_background
                    hover_background Solid("#8c7425")

                    action SetVariable("selected_angle", angle)

            # DONE
            textbutton "DONE":
                xsize 160
                ysize 90

                text_size 42
                text_bold True
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

                background Solid("#267a42")
                hover_background Solid("#35a85b")

                action Return("done")

            # RETURN TO CONTROL ROOM
            textbutton "RETURN TO CONTROL ROOM":
                xsize 350
                ysize 90

                text_size 30
                text_bold True
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

                background Solid("#414653")
                hover_background Solid("#606979")

                action Return("control_room")


#-----------------------------------------
# SOLAR PANEL - RESULT WINDOW
#-----------------------------------------

screen solar_result(success=False):

    modal True

    # Darken background
    add "#0009"

    # Display rotated arrow in its new position
    use solar_arrow_display

    frame:
        xalign 0.5
        yalign 0.43

        xsize 1000
        ysize 600

        background Solid("#20242e")
        padding (50, 40)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 35

            if success:

                text "CORRECT POSITION!":
                    size 68
                    color "#55d889"
                    bold True
                    xalign 0.5

                text "The lever is correctly positioned.":
                    size 40
                    color "#ffffff"
                    xalign 0.5

                text "The solar panel is now activated!":
                    size 36
                    color "#bfc5d2"
                    xalign 0.5

                null height 20

                textbutton "CONTINUE":
                    xalign 0.5
                    text_size 44
                    text_color "#ffffff"
                    text_hover_color "#ffffff"
                    background Solid("#267a42")
                    hover_background Solid("#35a85b")
                    xpadding 100
                    ypadding 35

                    action Return("continue")

            else:

                text "INCORRECT POSITION":
                    size 68
                    color "#ff4b4b"
                    bold True
                    xalign 0.5

                text "The lever is incorrectly positioned.":
                    size 40
                    color "#ffffff"
                    xalign 0.5

                text "You have no more attempts.":
                    size 40
                    color "#bfc5d2"
                    xalign 0.5

                null height 20

            textbutton "RETURN TO CONTROL ROOM":
                xalign 0.5
                text_size 29
                text_color "#ffffff"
                text_hover_color "#ffffff"
                background Solid("#414653")
                hover_background Solid("#606979")
                xpadding 50
                ypadding 20

                action Return("control_room")


#=========================================
# MAIN GAME
#=========================================

label start:

    scene black

    "Welcome to my test_game!"


    #-------------------------------------
    # EVENT 1: ELECTRICAL PANEL
    #-------------------------------------

    # Generate random sequence
    $ sequence = renpy.random.sample(range(6), 6)

    # Reset fuses and progress
    $ fuses = [False, False, False, False, False, False]
    $ current_step = 0

    # Generate sequence text
    $ sequence_text = " -> ".join(str(x + 1) for x in sequence)

    "To complete the event, follow this sequence: [sequence_text]"

    call screen cuadro_electrico

    "You have turned on all the fuses!"

    Miquel "Well done, boy!"

    jump evento_solar


#=========================================
# EVENT 2: SOLAR PANEL - INTRODUCTION
#=========================================

label evento_solar:

    # Initial values
    $ arrow_angle = 0
    $ selected_angle = 0
    $ arrow_message = ""

    # Generate random target angle
    $ target_angle = renpy.random.choice([0, 45, 90, 135, 180])

    # Introduction background
    scene bg_panel_solar:
        xalign 0.5
        yalign 0.5
        zoom 2.5

    "Now we have to adjust the solar panel."

    "You must select the correct position for the lever."

    "HINT: The correct angle is [target_angle] degrees."

    "Find the correct angle to activate the solar panel."

    # Minigame background
    scene bg_evento_solar:
        xalign 0.5
        yalign 0.5
        zoom 4

    jump evento_solar_flecha


#-----------------------------------------
# SOLAR PANEL - INTERACTION
#-----------------------------------------

label evento_solar_flecha:

    # Initial arrow position
    $ arrow_angle = 0
    $ selected_angle = 0
    $ arrow_message = ""

    # Show arrow and selection buttons
    $ result = renpy.call_screen("solar_arrow")

    if result == "control_room":
        jump sala_mando

    if result == "done":

        # Apply selected angle
        $ arrow_angle = selected_angle

        # Show rotated arrow and result
        $ result = renpy.call_screen(
            "solar_result",
            success=(selected_angle == target_angle)
        )

        if result == "control_room":
            jump sala_mando

        elif result == "continue":
            "Correct! The solar panel is now in the right position."

    return


#=========================================
# CONTROL ROOM
#=========================================

label sala_mando:

    scene black

    "Returning to the control room."

    return
