## 01_definitions.rpy - Definiciones de personajes, variables e imágenes

## -------------------------------------------------------------
## Transformaciones para Diálogo Dinámico (Enfoque, Movimiento y Escala)
## -------------------------------------------------------------

# --- Estados estáticos o transiciones suaves de turno de habla ---
transform pos_centro_habla:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.50 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform pos_centro_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.50 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

transform pos_izq_habla:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.22 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform pos_izq_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.22 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

transform pos_der_habla:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.78 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform pos_der_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.78 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

# --- Desplazamientos cinematográficos entre posiciones ---
# Entrada inicial centrado
transform pos_centro:
    xanchor 0.5
    yanchor 1.0
    xpos 0.50
    ypos 1.0
    zoom 1.0
    alpha 1.0
    matrixcolor BrightnessMatrix(0.0)

# Desplazamiento hacia la izquierda (el personaje previo cede el centro, se reduce y oscurece)
transform mover_izq_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.45 xpos 0.22 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

# Desplazamiento del segundo personaje hacia la derecha tras su primer diálogo
transform mover_der_habla:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.45 xpos 0.78 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform mover_der_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.45 xpos 0.78 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

## -------------------------------------------------------------
## Lógica de Enfoque Automático de Personajes
## -------------------------------------------------------------
init python:
    CHAR_IMAGE_TAGS = {
        "Miquel": [
            "miquel_mediocuerpo", "miquel_cuerpoentero",
            "miquel_mediocuerpo_pensativo", "miquel_mediocuerpo_sonriendo"
        ],
        "Hanna": [
            "hanna_mediocuerpo_seria", "hanna_cuerpoentero",
            "hanna_mediocuerpo", "hanna_mediocuerpo_sorprendida",
            "hanna_mediocuerpo__pensativa"
        ],
        "Nelson": [
            "nelson_mediocuerpo", "nelson_cuerpoentero",
            "nelson_mediocuerpo_enfadado", "nelson_mediocuerpo_pensativo",
            "nelson_mediocuerpo_sorprendido"
        ]
    }

    # Posición de escenario asignada a cada personaje: 'center', 'left', 'right'
    char_positions = {
        "Miquel": "center",
        "Hanna": "center",
        "Nelson": "center"
    }

    current_speaker = [None]

    def set_char_pos(name, pos):
        """Asigna la posición de un personaje ('left', 'center', 'right')."""
        char_positions[name] = pos
        current_speaker[0] = None  # Fuerza a que el próximo diálogo actualice el estado

    def speaker_callback(speaker_name):
        def _cb(event, interact=True, **kwargs):
            if not interact:
                return
            if event == "begin":
                if current_speaker[0] == speaker_name:
                    return
                current_speaker[0] = speaker_name

                for char_name, tags in CHAR_IMAGE_TAGS.items():
                    for tag in tags:
                        if renpy.showing(tag):
                            pos = char_positions.get(char_name, "center")
                            if char_name == speaker_name:
                                if pos == "left":
                                    renpy.show(tag, at_list=[pos_izq_habla])
                                elif pos == "right":
                                    renpy.show(tag, at_list=[pos_der_habla])
                                else:
                                    renpy.show(tag, at_list=[pos_centro_habla])
                            else:
                                if pos == "left":
                                    renpy.show(tag, at_list=[pos_izq_idle])
                                elif pos == "right":
                                    renpy.show(tag, at_list=[pos_der_idle])
                                else:
                                    renpy.show(tag, at_list=[pos_centro_idle])
        return _cb

## -------------------------------------------------------------
## Personajes
## -------------------------------------------------------------
define c = Character("Narrador", color="#38bdf8", callback=speaker_callback("Narrador"))
define narrator = Character(None, callback=speaker_callback("Narrador"))
define M = Character("Miquel", color="#7ed957", callback=speaker_callback("Miquel"))
define N = Character("Nelson", color="#f423a3", callback=speaker_callback("Nelson"))
define H = Character("Hanna", color="#ff751f", callback=speaker_callback("Hanna"))
define T = Character("Tú", color="#8c52ff", callback=speaker_callback("Tú"))

## -------------------------------------------------------------
## Variables globales
## -------------------------------------------------------------
default puntuacion = 0
default lugar_aterrizaje = ""

## -------------------------------------------------------------
## Fondos (adaptados a 1920x1080)
## -------------------------------------------------------------
image bg rueda_prensa:
    "images/bg/bg_rueda_prensa.jpg"
    size (1920, 1080)

image bg_rueda_prensa:
    "images/bg/bg_rueda_prensa.jpg"
    size (1920, 1080)

image bg control_mission:
    "images/bg/bg_control_mission.jpg"
    size (1920, 1080)

image bg_control_mission:
    "images/bg/bg_control_mission.jpg"
    size (1920, 1080)

image bg nave:
    "images/bg/bg_nave_marte.png"
    size (1920, 1080)

image bg nave_marte:
    "images/bg/bg_nave_marte.png"
    size (1920, 1080)

image bg cocina_nave:
    "images/bg/bg_cocina_nave.png"
    size (1920, 1080)

image bg cocina:
    "images/bg/bg_cocina_nave.png"
    size (1920, 1080)

image bg_cocina_nave:
    "images/bg/bg_cocina_nave.png"
    size (1920, 1080)

image bg base_marte:
    "images/bg/bg_base_marte.png"
    size (1920, 1080)

image bg centro_hanna:
    "images/bg/bg_centro_trabajo_hanna.jpg"
    size (1920, 1080)

image bg centro_miquel:
    "images/bg/bg_centro_trabajo_miquel.png"
    size (1920, 1080)

image bg centro_nelson:
    "images/bg/bg_centro_trabajo_nelson.jpg"
    size (1920, 1080)

## -------------------------------------------------------------
## Sprites de Personajes (escalados proporcionalmente a 1080p)
## -------------------------------------------------------------
image miquel_mediocuerpo:
    "images/characters/miquel_mediocuerpo.png"
    ysize 720
    fit "contain"

image hanna_mediocuerpo_seria:
    "images/characters/hanna_mediocuerpo_seria.png"
    ysize 720
    fit "contain"

image hanna_cuerpoentero:
    "images/characters/hanna_cuerpoentero.png"
    ysize 920
    fit "contain"

image miquel_cuerpoentero:
    "images/characters/miquel_cuerpoentero.png"
    ysize 920
    fit "contain"

image nelson_cuerpoentero:
    "images/characters/nelson_cuerpoentero.png"
    ysize 920
    fit "contain"

image nelson_mediocuerpo:
    "images/characters/nelson_mediocuerpo.png"
    ysize 720
    fit "contain"
