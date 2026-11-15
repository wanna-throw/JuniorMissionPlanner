## 01_definitions.rpy - Character, variable and image definitions

## -------------------------------------------------------------
## Transforms for Dynamic Dialogue (Focus, Movement and Scale)
## -------------------------------------------------------------

# --- Static states or smooth transitions between speaking turns ---
transform pos_center_talk:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.50 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform pos_center_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.50 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

transform pos_left_talk:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.22 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform pos_left_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.22 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

transform pos_right_talk:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.78 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform pos_right_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.25 xpos 0.78 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

# --- Cinematic movements between positions ---
# Initial centered entrance
transform pos_center:
    xanchor 0.5
    yanchor 1.0
    xpos 0.50
    ypos 1.0
    zoom 1.0
    alpha 1.0
    matrixcolor BrightnessMatrix(0.0)

# Move to the left (the previous character gives up the center, shrinks and darkens)
transform move_left_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.45 xpos 0.22 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

# The second character moves to the right after their first line
transform move_right_talk:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.45 xpos 0.78 zoom 1.0 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform move_right_idle:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    ease 0.45 xpos 0.78 zoom 0.88 alpha 0.85 matrixcolor BrightnessMatrix(-0.25)

## -------------------------------------------------------------
## Automatic Character Focus Logic
## -------------------------------------------------------------
init python:
    CHAR_IMAGE_TAGS = {
        "Miquel": [
            "miquel", "miquel_halfbody", "miquel_fullbody",
            "miquel_halfbody_thinking", "miquel_halfbody_smiling"
        ],
        "Hanna": [
            "hanna", "hanna_halfbody_serious", "hanna_fullbody",
            "hanna_halfbody", "hanna_halfbody_surprised",
            "hanna_halfbody_thinking"
        ],
        "Nelson": [
            "nelson", "nelson_halfbody", "nelson_fullbody",
            "nelson_halfbody_angry", "nelson_halfbody_thinking",
            "nelson_halfbody_surprised"
        ]
    }

    # Stage position assigned to each character: 'center', 'left', 'right'
    char_positions = {
        "Miquel": "center",
        "Hanna": "center",
        "Nelson": "center"
    }

    current_speaker = [None]

    def set_char_pos(name, pos):
        """Sets a character's position ('left', 'center', 'right')."""
        char_positions[name] = pos
        current_speaker[0] = None  # Forces the next line of dialogue to refresh the state

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
                                    renpy.show(tag, at_list=[pos_left_talk])
                                elif pos == "right":
                                    renpy.show(tag, at_list=[pos_right_talk])
                                else:
                                    renpy.show(tag, at_list=[pos_center_talk])
                            else:
                                if pos == "left":
                                    renpy.show(tag, at_list=[pos_left_idle])
                                elif pos == "right":
                                    renpy.show(tag, at_list=[pos_right_idle])
                                else:
                                    renpy.show(tag, at_list=[pos_center_idle])
        return _cb

## -------------------------------------------------------------
## Characters
## -------------------------------------------------------------
define c = Character("Narrator", color="#38bdf8", callback=speaker_callback("Narrator"))
define narrator = Character(None, callback=speaker_callback("Narrator"))
define M = Character("Miquel", color="#7ed957", callback=speaker_callback("Miquel"))
define N = Character("Nelson", color="#f423a3", callback=speaker_callback("Nelson"))
define H = Character("Hanna", color="#ff751f", callback=speaker_callback("Hanna"))
define T = Character("You", color="#8c52ff", callback=speaker_callback("You"))

## -------------------------------------------------------------
## Global variables
## -------------------------------------------------------------
default score = 0
default landing_site = ""
default report_nelson = False
default report_hanna = False
default report_miquel = False

## -------------------------------------------------------------
## Backgrounds (scaled to 1920x1080)
## -------------------------------------------------------------
image bg press_conference:
    "images/bg/bg_rueda_prensa.jpg"
    size (1920, 1080)

image bg_press_conference:
    "images/bg/bg_rueda_prensa.jpg"
    size (1920, 1080)

image bg control_mission:
    "images/bg/bg_control_mission.jpg"
    size (1920, 1080)

image bg_control_mission:
    "images/bg/bg_control_mission.jpg"
    size (1920, 1080)

image bg ship:
    "images/bg/bg_nave_marte.png"
    size (1920, 1080)

image bg ship_mars:
    "images/bg/bg_nave_marte.png"
    size (1920, 1080)

image bg ship_kitchen:
    "images/bg/bg_cocina_nave.png"
    size (1920, 1080)

image bg kitchen:
    "images/bg/bg_cocina_nave.png"
    size (1920, 1080)

image bg_ship_kitchen:
    "images/bg/bg_cocina_nave.png"
    size (1920, 1080)

image bg mars_base:
    "images/bg/bg_base_marte.png"
    size (1920, 1080)

image bg control_room_crew:
    # 2528x1686 image: scaled to 1920 px wide and centered vertically (no stretching)
    "images/bg/bg_equipo_sala_control.jpg"
    zoom (1920.0 / 2528.0)
    xpos 0 ypos 0 xanchor 0 yanchor 0
    yoffset -100

image bg expedition_day:
    "images/bg/bg_equipo_exp_dia_marte.jpg"
    size (1920, 1080)

image bg expedition_night:
    "images/bg/bg_equipo_exp_noche.jpg"
    size (1920, 1080)

image bg solar_panels:
    "images/bg/bg_panel_solar.png"
    size (1920, 1080)

image bg hanna_station:
    "images/bg/bg_centro_trabajo_hanna.jpg"
    size (1920, 1080)

image bg miquel_station:
    "images/bg/bg_centro_trabajo_miquel.png"
    size (1920, 1080)

image bg nelson_station:
    "images/bg/bg_centro_trabajo_nelson.jpg"
    size (1920, 1080)

## -------------------------------------------------------------
## Character Sprites using Ren'Py's Tag and Attribute System
## -------------------------------------------------------------

# --- NELSON (Tag: 'nelson') ---
image nelson:
    "images/characters/nelson_mediocuerpo.png"
    ysize 720
    fit "contain"

image nelson thinking:
    "images/characters/nelson_mediocuerpo_pensativo.png"
    ysize 720
    fit "contain"

image nelson surprised:
    "images/characters/nelson_mediocuerpo_sorprendido.png"
    ysize 720
    fit "contain"

image nelson angry:
    "images/characters/nelson_mediocuerpo_enfadado.png"
    ysize 720
    fit "contain"

image nelson fullbody:
    "images/characters/nelson_cuerpoentero.png"
    ysize 920
    fit "contain"

# --- HANNA (Tag: 'hanna') ---
image hanna:
    "images/characters/hanna_mediocuerpo_seria.png"
    ysize 720
    fit "contain"

image hanna serious:
    "images/characters/hanna_mediocuerpo_seria.png"
    ysize 720
    fit "contain"

image hanna thinking:
    "images/characters/hanna_mediocuerpo__pensativa.png"
    ysize 720
    fit "contain"

image hanna surprised:
    "images/characters/hanna_mediocuerpo_sorprendida.png"
    ysize 720
    fit "contain"

image hanna fullbody:
    "images/characters/hanna_cuerpoentero.png"
    ysize 920
    fit "contain"

# --- MIQUEL (Tag: 'miquel') ---
image miquel:
    "images/characters/miquel_mediocuerpo.png"
    ysize 720
    fit "contain"

image miquel thinking:
    "images/characters/miquel_mediocuerpo_pensativo.png"
    ysize 720
    fit "contain"

image miquel smiling:
    "images/characters/miquel_mediocuerpo_sonriendo.png"
    ysize 720
    fit "contain"

image miquel fullbody:
    "images/characters/miquel_cuerpoentero.png"
    ysize 920
    fit "contain"

## -------------------------------------------------------------
## Shortcut aliases (one image name per sprite)
## -------------------------------------------------------------
image nelson_halfbody = "nelson"
image nelson_halfbody_thinking = "nelson thinking"
image nelson_halfbody_surprised = "nelson surprised"
image nelson_halfbody_angry = "nelson angry"
image nelson_fullbody = "nelson fullbody"

image hanna_halfbody = "hanna"
image hanna_halfbody_serious = "hanna serious"
image hanna_halfbody_thinking = "hanna thinking"
image hanna_halfbody_surprised = "hanna surprised"
image hanna_fullbody = "hanna fullbody"

image miquel_halfbody = "miquel"
image miquel_halfbody_thinking = "miquel thinking"
image miquel_halfbody_smiling = "miquel smiling"
image miquel_fullbody = "miquel fullbody"
