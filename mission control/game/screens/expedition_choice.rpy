## expedition_choice.rpy - "Who leads the expedition?" selection screen.
## Same command-room background as the crew selection: each crew member has a
## completely invisible button with the exact shape of the character.

screen expedition_choice_screen(question, roles):

    for who in ["miquel", "nelson", "hanna"]:
        $ path = CREW_SPOTS[who][0]
        $ px, py = crew_spot_pos(who)
        button:
            xpos px
            ypos py
            background None
            hover_background None
            focus_mask Transform(path, zoom=CREW_BG_ZOOM)
            add Transform(path, zoom=CREW_BG_ZOOM, alpha=0.0)
            action Return(who)

    frame:
        xpos 275
        ypos 100
        background Solid("#1e293bee")
        padding (26, 12)
        vbox:
            spacing 2
            text question size 26 bold True color "#fbbf24"
            text "Click on the crew member who will lead it. The whole crew goes with them." size 17 color "#cbd5e1"

    use crew_label("Miquel", roles["miquel"], "#7ed957", False, 860, 185)
    use crew_label("Nelson", roles["nelson"], "#f423a3", False, 1190, 185)
    use crew_label("Hanna", roles["hanna"], "#ff751f", False, 1612, 300)
