
#=================================
# TEST1: learning
#=================================
    #Characters
define Miquel = Character("Miquel", color='#ff0000')
    
    #Program
default fuses = [False, False, False, False, False, False]
default sequence = []
default current_step = 0

#=================================
# Functions
#=================================

screen cuadro_electrico():

    # Background
    add "images/cuadro_electrico.png":
        xalign 0.5
        yalign 0.5
        zoom 2.5

    # Initial positions
    $ x_start = 1180
    $ y_start = 450

    # Distance between fuses
    $ x_spacing = 495
    $ y_spacing = 800

    # Create 6 fuses
    for i in range(6):
        $ x_pos = x_start + (i % 3) * x_spacing         # %  -> resto (modulo)      
        $ y_pos = y_start + (i // 3) * y_spacing        # // -> resultado entero (division entera)
        $ fuse_image = Transform("images/plomo_on.png" if fuses[i] else "images/plomo_off.png",zoom=0.48)
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




screen wrong_sequence():

    modal True

    add "#0009"

    frame:
        xalign 0.5
        yalign 0.5

        xsize 1200
        ysize 650

        background Solid("#20242e")
        padding (70, 60)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 45

            text "INCORRECT SEQUENCE":
                size 75
                color "#ff4b4b"
                bold True
                xalign 0.5

            text "You activated the wrong fuse.":
                size 55
                color "#ffffff"
                xalign 0.5

            text "Please try again and follow the correct sequence.":
                size 40
                color "#bfc5d2"
                xalign 0.5
                text_align 0.5

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


#=================================
# Main
#=================================

label start:

    scene black
    "Welcome to my test_game!"
    # Generate a random sequence
    $ sequence = renpy.random.sample(range(6), 6)
    # Reset the fuses and progress
    $ fuses = [False, False, False, False, False, False]
    $ current_step = 0
    # Show the sequence to the player
    $ sequence_text = " -> ".join(str(x + 1) for x in sequence)
    "To complete the event, follow this sequence: [sequence_text]"
    call screen cuadro_electrico
    "You have turned on all the fuses!"
    Miquel "Well done, boy!"
    return
