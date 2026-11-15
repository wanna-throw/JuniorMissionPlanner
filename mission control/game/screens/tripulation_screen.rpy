# screens/tripulation_screen.rpy
# Choose which crew member to visit. The background shows the three crew members
# around the central table of the command room. Each one has a completely invisible
# button with the exact shape of the character. After their report, the character
# is shown darkened and can no longer be clicked.

## The background (2528x1686) is scaled to 1920 px wide and moved up 100 px.
define CREW_BG_ZOOM = 1920.0 / 2528.0

## Darkened cut-outs of each character, with their position in the original background
define CREW_SPOTS = {
    "miquel": ("images/ui/crew_done_miquel.png", 1138, 461),
    "nelson": ("images/ui/crew_done_nelson.png", 1348, 452),
    "hanna":  ("images/ui/crew_done_hanna.png", 1688, 566),
}

init python:
    def crew_spot_pos(who):
        path, x, y = CREW_SPOTS[who]
        return (int(x * CREW_BG_ZOOM), int(y * CREW_BG_ZOOM) - 100)

transform crew_cutout:
    zoom CREW_BG_ZOOM

transform attention_pulse:
    zoom 1.0
    block:
        ease 0.6 zoom 1.06
        ease 0.6 zoom 1.0
        repeat

style crew_label_frame:
    background Solid("#1e293be6")
    padding (16, 8)

screen crew_label(name, role, name_color, done, x, y):
    frame:
        style "crew_label_frame"
        xpos x
        ypos y
        xanchor 0.5
        vbox:
            xalign 0.5
            spacing 1
            text name size 26 bold True color name_color xalign 0.5
            text role size 17 color "#cbd5e1" xalign 0.5
            if done:
                text "✓ REPORT RECEIVED" size 15 bold True color "#4ade80" xalign 0.5

screen crew_spot(who, done, target):
    $ path = CREW_SPOTS[who][0]
    $ px, py = crew_spot_pos(who)
    if done:
        # Character shown darkened once their report is done
        add path at crew_cutout xpos px ypos py
    else:
        # Completely invisible button with the exact shape of the character
        button:
            xpos px
            ypos py
            background None
            hover_background None
            focus_mask Transform(path, zoom=CREW_BG_ZOOM)
            add Transform(path, zoom=CREW_BG_ZOOM, alpha=0.0)
            action Jump(target)

screen crew_selection_screen():

    use crew_spot("miquel", report_miquel, "miquel_report_dialogue")
    use crew_spot("nelson", report_nelson, "nelson_report_dialogue")
    use crew_spot("hanna", report_hanna, "hanna_report_dialogue")

    # Header, top left (out of the way of the HUD and the characters)
    frame:
        xpos 40
        ypos 100
        background Solid("#1e293bee")
        padding (26, 12)
        text "Which area of the settlement do you want to go to?" size 24 color "#38bdf8"

    # Name and job of each crew member, in gray-blue boxes
    use crew_label("Miquel", "Maintenance Workshop", "#7ed957", report_miquel, 860, 165)
    use crew_label("Nelson", "Medical & Chemistry Lab", "#f423a3", report_nelson, 1190, 165)
    use crew_label("Hanna", "Robotics & Telecom Station", "#ff751f", report_hanna, 1612, 300)

    # When the three reports are done: attention bubble to take out the tablet
    if report_nelson and report_hanna and report_miquel:
        if not supplies_checked:
            button:
                xpos 420
                ypos 860
                xanchor 0.5
                at attention_pulse
                background Solid("#0f172af0")
                hover_background Solid("#1e3a5ff5")
                padding (20, 14)
                action Return("tablet")
                hbox:
                    spacing 16
                    frame:
                        xysize (54, 54)
                        background Solid("#f59e0b")
                        text "!" size 40 bold True color "#0f172a" xalign 0.5 yalign 0.5
                    vbox:
                        yalign 0.5
                        spacing 2
                        text "NEW REPORT AVAILABLE" size 22 bold True color "#fbbf24"
                        text "Take out the tablet to check food and water" size 17 color "#e2e8f0"
        else:
            frame:
                xpos 420
                ypos 870
                xanchor 0.5
                background Solid("#1e293bee")
                padding (30, 12)
                textbutton "Gather the team and plan Day 2 ▶":
                    text_size 22
                    text_bold True
                    text_color "#38bdf8"
                    text_hover_color "#ffffff"
                    action Return("meeting")
