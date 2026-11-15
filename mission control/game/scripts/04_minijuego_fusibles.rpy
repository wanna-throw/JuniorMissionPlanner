## 04_minijuego_fusibles.rpy - Electrical panel fuse minigame (imported from test1 and adapted to 1080p)

# =========================================
# ELECTRICAL PANEL VARIABLES
# =========================================
default fuses = [False, False, False, False, False, False]
default sequence = []
default current_step = 0
default sequence_text = ""

# =========================================
# MAIN SCREEN: ELECTRICAL PANEL
# =========================================
screen electrical_panel():

    # Dark technical background of the panel
    add Solid("#070d18")

    # Centered electrical panel image
    add "images/cuadro_electrico.png":
        xalign 0.5
        yalign 0.5
        zoom 1.25

    # Top banner with the sequence the player must follow
    frame:
        xalign 0.5
        ypos 30
        background Solid("#0f172ae6")
        padding (40, 16)

        vbox:
            xalign 0.5
            spacing 6

            text "POWER DISTRIBUTION PANEL - FUSE SEQUENCE":
                size 20
                color "#60a5fa"
                bold True
                xalign 0.5

            text "[sequence_text]":
                size 34
                color "#facc15"
                bold True
                xalign 0.5

    # Coordinates adapted to 1920x1080 resolution
    $ x_start = 590
    $ y_start = 225
    $ x_spacing = 248
    $ y_spacing = 400

    # Render the 6 interactive fuses
    for i in range(6):

        $ x_pos = int(x_start + (i % 3) * x_spacing)
        $ y_pos = int(y_start + (i // 3) * y_spacing)

        $ fuse_image = Transform(
            "images/plomo_on.png" if fuses[i] else "images/plomo_off.png",
            zoom=0.24
        )

        imagebutton:
            idle fuse_image
            hover fuse_image
            pos (x_pos, y_pos)
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

# =========================================
# ERROR SCREEN: WRONG SEQUENCE
# =========================================
screen wrong_sequence():

    modal True

    add "#0009"

    frame:
        xalign 0.5
        yalign 0.5

        xsize 800
        ysize 460

        background Solid("#1e293b")
        padding (50, 40)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "WRONG SEQUENCE":
                size 46
                color "#ef4444"
                bold True
                xalign 0.5

            text "You switched on the wrong fuse.":
                size 26
                color "#f1f5f9"
                xalign 0.5

            text "The correct sequence is:":
                size 22
                color "#94a3b8"
                xalign 0.5

            text "[sequence_text]":
                size 36
                color "#facc15"
                bold True
                xalign 0.5

            null height 10

            textbutton "TRY AGAIN":
                xalign 0.5
                text_size 26
                text_color "#ffffff"
                text_hover_color "#ffffff"
                background Solid("#b91c1c")
                hover_background Solid("#dc2626")
                xpadding 50
                ypadding 16

                action [
                    Hide("wrong_sequence"),
                    SetVariable("fuses", [False, False, False, False, False, False]),
                    SetVariable("current_step", 0)
                ]
