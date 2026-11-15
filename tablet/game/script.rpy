# VARIABLES
default pantalla_actual = "reportaje"

default hambre_michael = 3
default sed_michael = 3
default hambre_hanna = 3
default sed_hanna = 3
default hambre_nelson = 3
default sed_nelson = 3
default hambre_user = 3
default sed_user = 3


# FONDO
screen background():
    add "bg_base_marte":
        xalign 0.5
        yalign 0.5
        zoom 1.25


# INDICADORES DE NECESIDADES
screen indicador_necesidad(valor, tipo, x, y):

    if tipo == "hambre":
        if valor == 3:
            $ color = "#F4A340"
        elif valor == 2:
            $ color = "#e5622a"
        else:
            $ color = "#b41616"

    elif tipo == "sed":
        if valor == 3:
            $ color = "#43B8D8"
        elif valor == 2:
            $ color = "#177fab"
        else:
            $ color = "#114482"

    hbox:
        xpos x
        ypos y
        spacing 4

        for i in range(3):

            if i < valor:
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



# TABLET
screen tablet():

    if pantalla_actual == "reportaje":
        add "tablet_report":
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
                text "Tu reportaje es wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg jewbwsjdkbgfw  jebfguwb eguheb hgbjhe wbgjbejhwbg jewbwsjd kbgfwjebf guwbeguhebhg bjhewbgjb ejhwbgje wbw sjdkbgfwjebfg uwbeguh ebhgbjhewbg jbejhwbgj ewbwsjdkb gfwjebf guwbeguhe bhgbjhew bgjbejhwbgj ewbwsjdk bgfwjebfguw beguhebhg bjhewbgjb guhebhgbjhewb gjbejhwbgjewb wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg":
                    size 20
                    color "#000000"


    elif pantalla_actual == "personajes":
        add "tablet_personajes":
            xalign 0.5
            yalign 0.65
            zoom 0.75

        use indicador_necesidad(hambre_michael, "hambre", 790, 620)
        use indicador_necesidad(sed_michael, "sed", 790, 575)

        use indicador_necesidad(hambre_hanna, "hambre", 790, 920)
        use indicador_necesidad(sed_hanna, "sed", 790, 875)

        use indicador_necesidad(hambre_nelson, "hambre", 1050, 620)
        use indicador_necesidad(sed_nelson, "sed", 1050, 575)

        use indicador_necesidad(hambre_user, "hambre", 1050, 915)
        use indicador_necesidad(sed_user, "sed", 1050, 870)


    elif pantalla_actual == "eventos":
        add "tablet_eventos":
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
                text "Alerta! El evento es wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg jewbwsjdkbgfw  jebfguwb eguheb hgbjhe wbgjbejhwbg jewbwsjd kbgfwjebf guwbeguhebhg bjhewbgjb ejhwbgje wbw sjdkbgfwjebfg uwbeguh ebhgbjhewbg jbejhwbgj ewbwsjdkb gfwjebf guwbeguhe bhgbjhew bgjbejhwbgj ewbwsjdk bgfwjebfguw beguhebhg bjhewbgjb guhebhgbjhewb gjbejhwbgjewb wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg wsjdkbgfw jebfguwbeguhebh gbjhewbg jbejhwbg jewbwsjdkb gfwjebfguwbeguhe bhgbjhewbgjb ejhwbgj ewbwsjdkbgf wjebfguw beguhebhgbj hewbg jbejhwbg":
                    size 20
                    color "#000000"


    # BOTONES DE NAVEGACIÓN
    button:
        xpos 700
        ypos 269
        xsize 65
        ysize 65
        background None
        action SetVariable("pantalla_actual", "reportaje")

    button:
        xpos 802
        ypos 269
        xsize 65
        ysize 65
        background None
        action SetVariable("pantalla_actual", "personajes")

    button:
        xpos 910
        ypos 269
        xsize 65
        ysize 65
        background None
        action SetVariable("pantalla_actual", "eventos")


# INICIO DEL JUEGO
label start:
    scene black
    "welcome"
    show screen background
    $ sed_michael = 1
    $ hambre_michael = 1
    call screen tablet

    return
