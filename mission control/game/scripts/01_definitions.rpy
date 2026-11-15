## 01_definitions.rpy - Definiciones de personajes, variables e imágenes

## -------------------------------------------------------------
## Personajes
## -------------------------------------------------------------
## C es el narrador. Puedes cambiar "Narrador" por None si prefieres
## que el texto aparezca sin nombre en la caja de diálogo.
define c = Character("Narrador", color="#38bdf8")

## -------------------------------------------------------------
## Placeholders Visuales para Fondos
## -------------------------------------------------------------
## Mientras no tengas las imágenes finales, se mostrará un fondo provisional.
## En cuanto coloques el archivo 'nave.png' o 'nave.jpg' en:
##   game/images/bg/
## se mostrará tu imagen automáticamente sin tocar código.

image placeholder_bg_nave = Composite(
    (1920, 1080),
    (0, 0), Solid("#0b1329"),
    (0, 0), Text(
        "{size=+10}{b}FONDO: INTERIOR DE LA NAVE{/b}{/size}\n\n"
        "{color=#94a3b8}Coloca tu imagen aqui:{/color}\n"
        "{color=#38bdf8}game/images/bg/nave.png{/color} o {color=#38bdf8}.jpg{/color}\n\n"
        "{size=-4}{color=#64748b}(Resolucion recomendada: 1920 x 1080 px){/color}{/size}",
        size=32,
        xalign=0.5,
        yalign=0.45,
        text_align=0.5,
        color="#ffffff",
        substitute=False
    )
)

image bg nave = ConditionSwitch(
    "renpy.loadable('images/bg/nave.png')", "images/bg/nave.png",
    "renpy.loadable('images/bg/nave.jpg')", "images/bg/nave.jpg",
    "True", "placeholder_bg_nave"
)
