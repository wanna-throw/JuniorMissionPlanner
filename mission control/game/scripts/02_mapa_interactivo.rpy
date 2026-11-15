## 02_mapa_interactivo.rpy - Sistema de Selección de Base en Marte (Importado de Carpeta_pol)

# ==========================================
# 1. CONFIGURACIÓN DE PUNTOS INTERACTIVOS (NOMBRES REALES MSL)
# Formato: ("Nombre en recuadro", pos_x, pos_y, "orientacion", "clave_datos")
# ==========================================
define puntos_mision = [
    ("Mawrth Vallis",     858, 407, "arriba",    "mawrth"),
    ("Holden Crater",     776, 704, "izquierda", "holden"),
    ("Eberswalde Crater", 786, 685, "derecha",   "eberswalde"),
    ("Gale Crater",      1693, 593, "arriba",    "gale")
]

# ==========================================
# 2. CONFIGURACIÓN DE REFERENCIAS DEL FONDO (Solo texto sin recuadro)
# ==========================================
define formaciones_marte = [
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
# 3. PLANTILLA DE DATOS CIENTÍFICOS REALES (NASA / MSL WORKSHOP)
# ==========================================
define datos_ubicaciones = {
    "mawrth": {
        "titulo": "Mawrth Vallis Site",
        "imagen": "images/crater_mawrth.png",
        "coordenadas": "24N, 341E",
        "hipotesis": "• Mawrth Vallis records geologic processes during early Martian history, when aqueous phyllosilicate-forming processes were pervasive and persistent. This site provides the opportunity to understand the potential for early habitability on the planet and may be representative of global conditions on Mars.",
        "contras": "• There is no consensus on the depositional setting or the mechanisms for concentrating or preserving organics and it is unlikely that the depositional setting will be further refined prior to landing and in situ evaluation.\n• Although textural and chemical characterization of the units using the MSL payload may distinguish between models for emplacement history, there is not a consensus that such an approach will be successful.",
        "pros": "• {b}Setting -{/b} Exposes the oldest preserved rocks of the four candidate sites and provides an opportunity to explore Noachian crust to seek and investigate information about the processes active on early Mars.\n• {b}Diversity -{/b} Hydrated minerals are present and modeled to contribute several tens of percent by volume to the rocks (most of any of the sites) that formed in aqueous environments.\n• {b}Preservation -{/b} The phyllosilicate-bearing units include smectites, suggesting they are well preserved and may contain/help preserve organics.\n• {b}Exploration Targets -{/b} A good list of prioritized targets within the ellipse has been identified and targets outside the ellipse, including sulfates, are also well-defined.",
        "incertidumbres": "• The depositional setting(s) associated with emplacement of the rocks and mineralogic units at Mawrth remains uncertain.\n• The amount, source, and duration of interaction with water in development of the units remains uncertain.\n• It is uncertain if the observed alteration record extends to the primary Fe/Mg smectite deposit and its potential organic record.\n• It remains uncertain whether Oyama crater ejecta persists or which unit it might correspond to.",
        "destino": "explorar_mawrth"
    },
    "eberswalde": {
        "titulo": "Eberswalde Crater Site",
        "imagen": "images/crater_eberswalde.png",
        "coordenadas": "23.9S, 327E",
        "hipotesis": "• Eberswalde crater stratigraphy, geomorphology, and mineralogy record the evolution of a crater lake, the history of hydrologic and climatic changes resulting in the formation of fluvial-deltaic systems, and a sedimentary depositional environment that might have been favorable to the preservation of organic materials and/or other kinds of biosignatures.",
        "contras": "• Relatively limited variety and modeled abundance of phyllosilicate minerals known to preserve organics detected from orbit.\n• Science in landing ellipse is secondary to that outside of the ellipse.",
        "pros": "• {b}Setting -{/b} Eberswalde shows excellent preservation of a fluvial-deltaic system emplaced into a standing body of water that integrates sedimentary material from a broad source region.\n• {b}Diversity -{/b} In addition to fluvio-lacustrine deposits (e.g., sinuous ridges), Holden crater ejecta and possible megabreccia related to the Eberswalde impact event occur.\n• {b}Preservation -{/b} Orbital detection of clay minerals near the bottom of the delta front, maybe in bottom set deposits, define a well-defined target for exploration.\n• {b}Exploration Targets -{/b} Well-defined fluvial-deltaic-lacustrine and megabreccia targets coupled with mineralogical diversity within and outside of the ellipse defines a short and long term exploration strategy.",
        "incertidumbres": "• Little evidence for shorelines corresponding to the elevation of the delta surface and the spillway to the eastern basin, though some aspects suggest it may have been ice-covered.\n• Delta emplacement might be consistent with delivery of water and sediment shortly after the Holden impact; this cannot be ruled out in advance of landing.\n• Delta is no older than Early Hesperian and some investigators believe it may have been deposited as late as the Early Amazonian.",
        "destino": "explorar_eberswalde"
    },
    "holden": {
        "titulo": "Holden Crater Site",
        "imagen": "images/crater_holden.png",
        "coordenadas": "26S, 325E",
        "hipotesis": "• Holden crater preserves evidence of a closed fluvial-lacustrine system that provides the opportunity to apply a geomorphic systems approach to evaluating and preserving evidence for a sustained, habitable environment.",
        "contras": "• Relatively limited variety of phyllosilicate minerals known to preserve organics detected from orbit.\n• Origin of stratified light-toned materials as lacustrine versus alternate depositional processes remains uncertain.",
        "pros": "• {b}Setting -{/b} The bajada in the ellipse and light-toned layered materials comprise one of the largest and best preserved alluvial systems on Mars.\n• {b}Diversity -{/b} Diversity is represented by fan sediments, phyllosilicate-bearing light toned layered deposits, Uzboi flood deposits, and mega-breccias in the crater walls/floor.\n• {b}Preservation -{/b} Strata comprising the light-toned layered materials may be the equivalent of bottom set beds emplaced in a lacustrine setting, which might preserve organics for interrogation by the MSL.\n• {b}Exploration Targets -{/b} Well-defined exploration targets exist within and outside the landing ellipse. Targets within the ellipse offer access to all major units for interrogation.",
        "incertidumbres": "• There are no shorelines or stratal geometries and limited evidence for other properties associated with the light-toned layered deposits and fans.\n• Age of light-toned layered deposits and adjacent alluvial fan surfaces are no older than Early Hesperian and fans may be as young as Early Amazonian.\n• Diverse megabreccia occurrences within the ellipse, walls, and rims may include evidence that they supported an impact-induced hydrothermal system.",
        "destino": "explorar_holden"
    },
    "gale": {
        "titulo": "Gale Crater Site",
        "imagen": "images/crater_gale.png",
        "coordenadas": "4.5S, 137.4E",
        "hipotesis": "• These strata contain multiple hydrous minerals (sulfates, phyllosilicates) that indicate varying aqueous environmental conditions. Layered sediments within Gale crater record a sequence of aqueous habitable environments over an extended period.",
        "contras": "• The original extent and timing of processes responsible for the present mound morphology needs better definition and the regional and global stratigraphic context of the mound is not firmly established.\n• Science in landing ellipse on and near an alluvial fan is secondary to that outside of the ellipse and observations within the ellipse may be encumbered by dust.",
        "pros": "• {b}Setting -{/b} Diverse stratigraphy in a 5 km mound within a 5 km deep Late Noachian crater. Stratigraphy includes well-defined beds of hydrated minerals.\n• {b}Diversity -{/b} Multiple mineralogical and stratigraphic units within the 5 km thick mound sequence with alternating inter-bedded phyllosilicate and sulfate bearing beds in the lower mound.\n• {b}Preservation -{/b} The phyllosilicate-bearing units in the lower mound and moat include smectites that would help preserve organics if present. Biosignatures may be best preserved in the sulfate bearing strata.\n• {b}Exploration Targets -{/b} The specific distribution of science targets within and outside of the ellipse is well defined. Preserved organics could occur in a high thermal inertia unit in fan in ellipse.",
        "incertidumbres": "• Although several testable models for mound formation exist, uncertainty remains about the depositional setting for much of the stratigraphy.\n• Crater statistics suggest Gale is Late Noachian, whereas floor deposits are interpreted to be Early Hesperian.\n• The source of water associated with deposition remains uncertain, but valleys suggests groundwater as opposed to meteoric sources.\n• Preservation potential of organics in the sulfate units may be compromised by the known presence of iron oxides.",
        "destino": "explorar_gale"
    }
}

# ==========================================
# 4. ANIMACIONES DE LOS MARCADORES
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
# 5. PANTALLA PRINCIPAL DEL MAPA (1920x1080)
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
    for nombre_base, px, py, orientacion, clave_datos in puntos_mision:
        
        if orientacion == "arriba":
            button:
                pos (px, py)
                at marcador_arriba
                background None
                action Show("ficha_ubicacion", id_ubicacion=clave_datos)
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
                action Show("ficha_ubicacion", id_ubicacion=clave_datos)
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
                action Show("ficha_ubicacion", id_ubicacion=clave_datos)
                hbox:
                    spacing 6
                    add Transform("images/pin_marte.png", zoom=0.15)
                    frame:
                        yalign 0.35
                        background Solid("#467294E6")
                        padding (10, 4)
                        text nombre_base size 16 color "#ffffff" bold True

# ==========================================
# 6. PANTALLA PLANTILLA DE DETALLE DE BASE (1920x1080)
# ==========================================
screen ficha_ubicacion(id_ubicacion):
    modal True
    $ info = datos_ubicaciones[id_ubicacion]

    # Fondo tecnológico azul de circuitos
    add "images/fondo_tech.png" xysize (1920, 1080)
    # Capa oscura semitransparente para garantizar que el texto blanco se lea perfecto
    add Solid("#061026B3")

    # Contenedor principal con márgenes
    vbox:
        xpos 50
        ypos 35
        xsize 1820
        spacing 20

        # --- ZONA DE INFORMACIÓN (2 COLUMNAS) ---
        hbox:
            spacing 25
            xsize 1820
            ysize 920

            # ==========================================
            # COLUMNA IZQUIERDA (Imagen + Hipótesis + Contras)
            # ==========================================
            vbox:
                xsize 895
                spacing 20

                # Bloque Superior Izquierdo: Título + Imagen del Cráter + Coordenadas + Hipótesis
                frame:
                    xsize 895
                    ysize 640
                    background Solid("#0b1d3aD9")
                    padding (25, 20)

                    vbox:
                        spacing 10
                        # Título subrayado centrado
                        text "{u}" + info["titulo"] + "{/u}" size 30 color "#66ccff" bold True xalign 0.5
                        
                        # Imagen del cráter/sitio
                        add info["imagen"] xysize (740, 185) fit "contain" xalign 0.5
                        
                        # Coordenadas debajo de la imagen
                        text info["coordenadas"] size 22 color "#a3d5ff" bold True xalign 0.5

                        null height 5
                        text "Overarching Hypothesis:" size 24 color "#66ccff" bold True
                        
                        # Viewport sin barra visual (scroll con la rueda del ratón)
                        viewport:
                            mousewheel True
                            ysize 265
                            text info["hipotesis"] size 20 color "#eef6ff" line_spacing 4

                # Bloque Inferior Izquierdo: Possible Cons of Site
                frame:
                    xsize 895
                    ysize 260
                    background Solid("#0b1d3aD9")
                    padding (25, 20)

                    vbox:
                        spacing 10
                        text "Possible Cons of Site:" size 24 color "#ff7b7b" bold True
                        viewport:
                            mousewheel True
                            ysize 175
                            text info["contras"] size 19 color "#eef6ff" line_spacing 4

            # ==========================================
            # COLUMNA DERECHA (Pros + Incertidumbres)
            # ==========================================
            vbox:
                xsize 900
                spacing 20

                # Bloque Superior Derecho: Specific Pros of Site
                frame:
                    xsize 900
                    ysize 540
                    background Solid("#0b1d3aD9")
                    padding (25, 20)

                    vbox:
                        spacing 10
                        text "Specific Pros of Site:" size 24 color "#66ff99" bold True
                        viewport:
                            mousewheel True
                            ysize 450
                            text info["pros"] size 19 color "#eef6ff" line_spacing 4

                # Bloque Inferior Derecho: Remaining Uncertainties
                frame:
                    xsize 900
                    ysize 360
                    background Solid("#0b1d3aD9")
                    padding (25, 20)

                    vbox:
                        spacing 10
                        text "Remaining Uncertainties:" size 24 color "#ffd166" bold True
                        viewport:
                            mousewheel True
                            ysize 270
                            text info["incertidumbres"] size 19 color "#eef6ff" line_spacing 4

        # --- BARRA INFERIOR DE BOTONES (VOLVER ATRÁS / ACEPTAR BASE) ---
        hbox:
            xalign 0.5
            spacing 80

            # Botón Volver al Mapa
            textbutton "← VOLVER AL MAPA":
                background Solid("#1e3a5f")
                hover_background Solid("#2d568c")
                padding (40, 15)
                text_size 24
                text_color "#ffffff"
                text_bold True
                action Hide("ficha_ubicacion")

            # Botón Aceptar Base
            textbutton "ACEPTAR ESTA BASE ✓":
                background Solid("#1b6ca8")
                hover_background Solid("#2892e0")
                padding (40, 15)
                text_size 24
                text_color "#ffffff"
                text_bold True
                action [Hide("ficha_ubicacion"), Jump(info["destino"])]

# ==========================================
# 7. DESTINOS TRAS ELEGIR BASE
# ==========================================
label explorar_mawrth:
    $ lugar_aterrizaje = "Mawrth Vallis"
    jump confirmar_aterrizaje

label explorar_eberswalde:
    $ lugar_aterrizaje = "el Cráter Eberswalde"
    jump confirmar_aterrizaje

label explorar_holden:
    $ lugar_aterrizaje = "el Cráter Holden"
    jump confirmar_aterrizaje

label explorar_gale:
    $ lugar_aterrizaje = "el Cráter Gale"
    jump confirmar_aterrizaje
