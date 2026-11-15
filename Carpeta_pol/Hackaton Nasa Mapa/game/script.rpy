# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
# ==========================================
# 1. CONFIGURACIÓN DE PUNTOS INTERACTIVOS (Ajusta aquí a mano)
# Formato: ("Nombre en recuadro", pos_x, pos_y, "orientacion", "etiqueta_salto")
# Orientaciones disponibles: "arriba", "izquierda", "derecha"
# ==========================================
define puntos_mision = [
    ("Acidalia Planitia",        858, 417, "arriba",    "explorar_acidalia"),
    ("Valles Marineris (Oeste)", 776, 704, "izquierda", "explorar_valles_marineris_1"),
    ("Valles Marineris (Este)",  786, 685, "derecha",   "explorar_valles_marineris_2"),
    ("Elysium Planitia",        1693, 583, "arriba",    "explorar_elysium")
]

# ==========================================
# 2. CONFIGURACIÓN DE REFERENCIAS DEL FONDO (Solo texto sin recuadro)
# Formato: ("NOMBRE REGIÓN", pos_x, pos_y)
# ==========================================
default formaciones_marte = [
    ("VASTITAS BOREALIS", 1120, 40),
    ("TANTALUS FOSSAE", 450, 240),
    ("TEMPE FOSSAE", 580, 300),
    ("ACIDALIA PLANITIA", 850, 210),
    ("UTOPIA RUPES", 1440, 270),
    ("AMAZONIS PLANITIA", 120, 390),
    ("ARABIA TERRA", 990, 420),
    ("ELYSIUM VOLCANIC REGION", 1740, 370),
    ("THARSIS VOLCANIC REGION", 360, 560),
    ("MARGARITIFER TERRA", 830, 535),
    ("TERRA MERIDIANI", 980, 580),
    ("TERRA SABAEA", 1240, 520),
    ("NEPENTHES MENSAE", 1590, 490),
    ("ELYSIUM PLANITIA", 1750, 540),
    ("VALLES MARINERIS", 650, 620),
    ("TYRRHENA TERRA", 1430, 610),
    ("CLARITAS FOSSAE", 440, 700),
    ("TERRA SIRENUM", 150, 775),
    ("ICARIA FOSSAE", 310, 825),
    ("HELLAS PLANITIA", 1330, 790),
    ("TERRA CIMMERIA", 1740, 730),
    ("AONIA TERRA", 450, 900),
    ("NOACHIS TERRA", 930, 840),
    ("PROMETHEI TERRA", 1520, 920),
    ("CHRONIUM PLANUM", 1710, 895)
]

# ==========================================
# 3. ANIMACIONES DE LOS MARCADORES
# ==========================================
transform marcador_arriba:
    anchor (0.5, 1.0)
    on idle:
        linear 0.12 yoffset 0 zoom 1.0
    on hover:
        linear 0.12 yoffset -10 zoom 1.08

transform marcador_izquierda:
    anchor (0.88, 1.0)
    on idle:
        linear 0.12 yoffset 0 zoom 1.0
    on hover:
        linear 0.12 yoffset -10 zoom 1.08

transform marcador_derecha:
    anchor (0.12, 1.0)
    on idle:
        linear 0.12 yoffset 0 zoom 1.0
    on hover:
        linear 0.12 yoffset -10 zoom 1.08

# ==========================================
# 4. PANTALLA PRINCIPAL DEL MAPA
# ==========================================
screen mapa_interactivo():
    # Imagen base
    add "images/mapa_marte.png" xysize (1920, 1080)

    # Capa 1: Textos cartográficos de referencia
    for nombre_zona, zx, zy in formaciones_marte:
        text nombre_zona:
            pos (zx, zy)
            anchor (0.5, 0.5)
            size 13
            color "#e6dcd3B3"
            outlines [(1, "#000000CC", 0, 0)]

    # Capa 2: Puntos interactivos de misión
    for nombre_base, px, py, orientacion, destino in puntos_mision:
        
        if orientacion == "arriba":
            button:
                pos (px, py)
                at marcador_arriba
                background None
                action Jump(destino)
                vbox:
                    spacing 4
                    frame:
                        xalign 0.5
                        background Solid("#467294E6")
                        padding (10, 4)
                        text nombre_base size 16 color "#ffffff" bold True
                    add Transform("images/pin_marte.png", zoom=0.15) xalign 0.5

        elif orientacion == "izquierda":
            button:
                pos (px, py)
                at marcador_izquierda
                background None
                action Jump(destino)
                hbox:
                    spacing 6
                    frame:
                        yalign 0.35
                        background Solid("#467294E6")
                        padding (10, 4)
                        text nombre_base size 16 color "#ffffff" bold True
                    add Transform("images/pin_marte.png", zoom=0.15)

        elif orientacion == "derecha":
            button:
                pos (px, py)
                at marcador_derecha
                background None
                action Jump(destino)
                hbox:
                    spacing 6
                    add Transform("images/pin_marte.png", zoom=0.15)
                    frame:
                        yalign 0.35
                        background Solid("#467294E6")
                        padding (10, 4)
                        text nombre_base size 16 color "#ffffff" bold True


label start:
    "Tras la publicación de la tripulación, se deberá selecionar el outpost al que se enviara la tripulación"
    call screen mapa_interactivo
    return
