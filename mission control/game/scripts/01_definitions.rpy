## 01_definitions.rpy - Definiciones de personajes, variables e imágenes

## -------------------------------------------------------------
## Personajes
## -------------------------------------------------------------
## C es el narrador. Puedes cambiar "Narrador" por None si prefieres
## que el texto aparezca sin nombre en la caja de diálogo.
define c = Character("Narrador", color="#38bdf8")

## -------------------------------------------------------------
## Fondos
## -------------------------------------------------------------
## Fondo del interior de la nave espacial (adaptado a la resolución del juego: 1920x1080)
image bg nave:
    "images/bg/bg_nave_marte.png"
    size (1920, 1080)

image bg_nave_marte:
    "images/bg/bg_nave_marte.png"
    size (1920, 1080)
