## warning_screen.rpy - Warning / disclaimer screen shown when the game launches

transform warning_fade_in(delay=0.0):
    alpha 0.0
    pause delay
    linear 0.8 alpha 1.0

transform warning_blink:
    alpha 0.0
    pause 2.0
    linear 0.6 alpha 1.0
    block:
        linear 0.9 alpha 0.35
        linear 0.9 alpha 1.0
        repeat

style warning_text:
    size 25
    color "#e5e5e5"
    text_align 0.5
    xalign 0.5
    line_spacing 6

screen warning_screen():
    modal True
    default can_continue = False

    add Solid("#000000")

    vbox:
        xalign 0.5
        yalign 0.42
        xsize 1500
        spacing 26

        text "WARNING":
            size 130
            bold True
            color "#e01414"
            outlines [(4, "#4a0000", 0, 0)]
            xalign 0.5
            at warning_fade_in(0.0)

        null height 4

        text "This game is a work of fiction.":
            style "warning_text"
            size 32
            bold True
            color "#ffffff"
            at warning_fade_in(0.4)

        text "All names, characters, organizations (including the United Robotics Association, URA), missions, places and events are products of the author's imagination or are used fictitiously. Any resemblance to actual persons, living or dead, to real organizations or to actual events is purely coincidental.":
            style "warning_text"
            at warning_fade_in(0.6)

        text "This game is not affiliated with, sponsored by or endorsed by any space agency, government or real company. Scientific information has been adapted for entertainment and educational purposes and may not be accurate.":
            style "warning_text"
            at warning_fade_in(0.8)

        text "{b}{color=#ff5a5a}PHOTOSENSITIVITY WARNING:{/color}{/b} A very small percentage of people may experience seizures when exposed to certain lights, flashes or patterns. If you feel dizzy, notice altered vision, eye or muscle twitching, disorientation or any involuntary movement, stop playing immediately and consult a doctor.":
            style "warning_text"
            at warning_fade_in(1.0)

        text "Play in a well-lit room, keep a reasonable distance from the screen and take a 10-15 minute break every hour.":
            style "warning_text"
            at warning_fade_in(1.2)

    text "Click or press any key to continue":
        size 22
        color "#9a9a9a"
        xalign 0.5
        yalign 0.95
        at warning_blink

    timer 1.5 action SetScreenVariable("can_continue", True)

    key "dismiss" action If(can_continue, Return())
    key "game_menu" action If(can_continue, Return())


# Shown automatically by Ren'Py when the game launches, before the main menu
label splashscreen:
    scene black
    call screen warning_screen with Dissolve(0.8)
    scene black with Dissolve(0.8)
    return
