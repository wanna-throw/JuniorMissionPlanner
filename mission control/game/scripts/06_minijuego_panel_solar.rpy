## 06_minijuego_panel_solar.rpy - Solar panel minigame (imported from test1 and adapted to 1080p)
## In test1 the game ran at 3840x2160: every pixel size here is half of the original.

default yesterday = None
default mission_result = []

# =========================================
# SOLAR PANEL VARIABLES
# =========================================
default arrow_angle = 0
default target_angle = 90
default selected_angle = 0
default solar_success = False

# Arrow position for each angle - (horizontal align, vertical align)
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

image bg solar_dial:
    "images/bg/bg_evento_solar.png"
    xalign 0.5
    yalign 0.5
    zoom 2

image bg solar_panels_close:
    "images/bg/bg_panel_solar.png"
    xalign 0.5
    yalign 0.5
    zoom 1.25

# -----------------------------------------
# SOLAR PANEL - ARROW DISPLAY
# -----------------------------------------
screen solar_arrow_display():

    $ import math

    $ arrow_x, arrow_y = arrow_positions[arrow_angle]

    $ rotation = arrow_angle - 135
    $ radians = math.radians(rotation)

    $ offset_x = (pivot_offset_x * math.cos(radians) - pivot_offset_y * math.sin(radians))
    $ offset_y = (pivot_offset_x * math.sin(radians) + pivot_offset_y * math.cos(radians))

    add Transform("images/ui/ui_arrow.png", zoom=0.5, rotate=rotation):
        xalign arrow_x
        yalign arrow_y
        xoffset -offset_x
        yoffset -offset_y

# -----------------------------------------
# SOLAR PANEL - ANGLE SELECTION
# -----------------------------------------
screen solar_arrow():

    use solar_arrow_display

    # Instructions
    frame:
        xalign 0.5
        ypos 30
        background Solid("#0f172ae6")
        padding (30, 14)
        vbox:
            spacing 4
            text "SOLAR PANEL - MANUAL ALIGNMENT" size 22 bold True color "#38bdf8" xalign 0.5
            text "Select the angle of the lever and press DONE. You only have one attempt!" size 18 color "#e2e8f0" xalign 0.5

    frame:
        xalign 0.5
        yalign 0.98

        background Solid("#20242e")
        padding (12, 10)

        hbox:
            spacing 6
            yalign 0.5

            for angle in [0, 45, 90, 135, 180]:

                $ angle_text_color = "#ffcc00" if selected_angle == angle else "#ffffff"
                $ angle_background = Solid("#725b16") if selected_angle == angle else Solid("#414653")

                textbutton "[angle]°":
                    xsize 70
                    ysize 50
                    text_size 24
                    text_bold True
                    text_color angle_text_color
                    text_xalign 0.5
                    text_yalign 0.5
                    background angle_background
                    hover_background Solid("#8c7425")
                    action SetVariable("selected_angle", angle)

            textbutton "DONE":
                xsize 100
                ysize 50
                text_size 22
                text_bold True
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5
                background Solid("#267a42")
                hover_background Solid("#35a85b")
                action Return("done")

# -----------------------------------------
# SOLAR PANEL - RESULT WINDOW
# -----------------------------------------
screen solar_result(success=False):

    modal True

    add "#0009"

    use solar_arrow_display

    frame:
        xalign 0.5
        yalign 0.43
        xsize 560
        ysize 320
        background Solid("#20242e")
        padding (30, 24)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 18

            if success:
                text "CORRECT POSITION!" size 36 color "#55d889" bold True xalign 0.5
                text "The lever is correctly positioned." size 20 color "#ffffff" xalign 0.5
                text "The solar panel is now activated!" size 18 color "#bfc5d2" xalign 0.5
            else:
                text "INCORRECT POSITION" size 36 color "#ff4b4b" bold True xalign 0.5
                text "The lever is incorrectly positioned." size 20 color "#ffffff" xalign 0.5
                text "You have no more attempts." size 20 color "#bfc5d2" xalign 0.5

            null height 6

            textbutton "CONTINUE":
                xalign 0.5
                text_size 22
                text_color "#ffffff"
                text_hover_color "#ffffff"
                background Solid("#267a42" if success else "#414653")
                hover_background Solid("#35a85b" if success else "#606979")
                xpadding 50
                ypadding 16
                action Return("continue")

# =========================================
# DAY 4 EVENT: INTRODUCTION
# =========================================
label solar_panel_event:

    $ target_angle = renpy.random.choice([0, 45, 90, 135, 180])

    scene bg solar_panels with fade

    "You put on your suit and go outside with Miquel. The storm has left a thick layer of dust everywhere."

    $ set_char_pos("Miquel", "center")
    show miquel thinking at pos_center with dissolve

    M "There it is: the wind has turned this panel. Its guidance motor is jammed, so we'll have to move the lever by hand."

    M "As the pilot, I've checked the navigation computer: to face the Sun, the lever must be at {b}[target_angle] degrees{/b}."

    T "Got it. [target_angle] degrees. Let's do this."

    hide miquel with dissolve

    "HINT: The correct angle is [target_angle] degrees."

    jump solar_panel_minigame

label solar_panel_minigame:

    $ arrow_angle = 0
    $ selected_angle = 0

    scene bg solar_dial with fade

    $ result = renpy.call_screen("solar_arrow")

    $ arrow_angle = selected_angle
    $ solar_success = (selected_angle == target_angle)
    $ renpy.call_screen("solar_result", success=solar_success)

    if solar_success:
        scene bg solar_panels with fade
        $ set_char_pos("Miquel", "center")
        show miquel smiling at pos_center with dissolve
        M "Perfect, Commander! The panel is pointing straight at the Sun."
        T "Energy is flowing again. Let's go back inside before the dust comes back."
        hide miquel with dissolve
        jump week_1_end
    else:
        jump solar_panel_failed

# =========================================
# FAILED ATTEMPT: the panel stays misaligned -> less energy production
# =========================================
define SOLAR_FAIL_PENALTY = 25   # % of energy production lost

label solar_panel_failed:

    $ solar_efficiency = max(0, solar_efficiency - SOLAR_FAIL_PENALTY)

    scene bg solar_panels with fade

    "The lever ends up in the wrong position and the guidance motor locks again."

    $ set_char_pos("Miquel", "center")
    show miquel thinking at pos_center with dissolve

    M "It's stuck, Commander. The panel isn't facing the Sun properly anymore."

    M "It will still work, but it will produce less energy than before."

    hide miquel with dissolve

    "{b}The energy you produce has been reduced by [SOLAR_FAIL_PENALTY]%%.{/b} Solar energy production: [solar_efficiency]%%."

    jump week_1_end
