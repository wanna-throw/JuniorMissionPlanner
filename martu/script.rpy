define M = Character("Miquel", color = "#7ed957")
define N = Character("Nelson",color = "#f423a3")
define H = Character("Hanna",color = "#ff751f")
define T = Character("Tu", color = "#8c52ff")

default puntuacion = 0

label start:

    scene black

"Estamos en el año 2052"

"La tecnología ha avanzado tanto que la NASA esta llevando a cabo el programa más ambicioso de la historia de la humanidad..."

"Se trata del programa Aphrodite, el cual tiene dos principales objetivos..."

"Buscar vida más allá de la Tierra..."

"Y crear asentamientos científicos de larga duración en otros planetas."

scene nave_marte

"Eres el comandante de la misión Aphrodite 3."

"El objetivo de la misión es llevar recursos al asentamiento desarrollado en las misiones Aphrodite 1 y 2..."

"Y empezar la búsqueda de vida extraterrestre."

"El lanzamiento de la nave se llevó a cabo el pasado 6 de Junio, del 2052, a las 18:00 UTC"

"Después de 6 meses y 2 días..."

"Y tras una maniobra de inserción orbital y frenado complicada..."

"Habéis logrado aterrizar."

"Ahora ya habrán pasado unas 2 horas"

show miquel_mediocuerpo:
    xalign 0.5
    yalign 0.5

M "Comandante..."

T "Hmm... 5 minutos más"

M "Despierta, anda, que se nos hará muy tarde para llegar al asentamiento."

T "¿Qué hora és?"

hide miquel_mediocuerpo

show hanna_mediocuerpo_seria:
    xalign 0.5
    yalign 0.5

H "Vaya siesta te has echado"

H "Si que estabas cansado"

H "*Enciende la luz*"

H "Buenos días, estamos en Marte ¿recuerdas?"

T "*frotándote los ojos* Solo me he echado una buena siesta... No me he quedado inconsciente."

H "Anda, hazte un café, que te necesitamos fresco"

hide hanna_mediocuerpo_seria

hide nave_marte

scene black

menu:
        "Ir a la cocina":
            T "*Te haces un café*"
            
T "Echo de menos el café de casa."
T "*Mientras tomas tu café, revisas la información de la tablet.*"

label tripulacion:

menu:
    "¿Sobre quién quieres consultar información?"

    "Hanna":
        show hanna_cuerpoentero
        H "Mujer, 31 años, Japonesa."
        H "Encargada de la Robótica y las Telecomunicaciones de la nave."
        hide hanna_cuerpoentero
        jump tripulacion
    "Miquel":
        show miquel_cuerpoentero
        M "Hombre, 29 años, Catalán / Estadounidense."
        M "Piloto e ingeniero mecánico."
        hide miquel_cuerpoentero
        jump tripulacion
    "Nelson":
        show nelson_cuerpoentero
        N "Hombre, 34 años, Senegalés."
        N "Médico y químico"
        hide nelson_cuerpoentero
        jump tripulacion
    "Comandante (Tú)":
        T "Comandante de la misión. Biólogo y geólogo."
        jump tripulacion
    "Volver":
        jump menu_principal

label menu_principal:

T "Qué buen equipo tengo..."

T "Tengo buenas expectativas de esta misión."

N "Comandante ¿estás preparado?"

N "Nos vamos cuanto antes."

T "Vámonos."

"De camino al asentamiento."

"Ya estamos en el asentamiento."

T "Hana ¿por qué tardas tanto en activar la energía?"

H "Comandante, no entiendo que ocurre... no funciona."

"Vas a ayudarla"

T "Hana, mientras hago la secuencia de encendido, tú tienes que mantener el botón de pulsado."


T "Chicos, hoy solo os voy a pedir que me hagáis un informe de los recursos disponibles."

"Para hablar con tus compañeros selecciona su avatar en la parte inferior derecha de la pantalla."

"Vayamos a hablar con Nelson."

label tripulation:

menu:
    "Nelson":
        N "Hola comandante, te comparto el informe actual de los niveles de O2 y temperatura."
        T "Genial Nelson, muchas gracias."
        T "Por cierto ¿qué te parecen las instalaciones?"
        N "Están muy bien hechas, son mas modernas y acogedoras de lo que esperaba..."
        N "Pero podrían haber dejado esterilizados los utensilios."
        T "Vaya que lástima, buena suerte esterilizando."
        "Ahora veamos que tiene que decirnos Hana"
        jump tripulation
    "Hanna":
        T "Hola Hana ¿cómo llevas el informe?"
        H "Por ahora estos son los parámetros de radiación."
        H "Las comunicaciones están en buen estado."
        T "Perfecto, muchas gracias."
        T "Bueno, te dejo tranquila."
        jump tripulation
    "Miquel":
        M "¡Comandante! Te estaba esperando."
        T "Veamos que tienes para mi."
        M "Mira, "
        jump tripulation
