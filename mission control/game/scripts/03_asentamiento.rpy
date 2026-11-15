## 03_asentamiento.rpy - Escena del despertar, tablet y llegada al asentamiento

label despertar_nave:

    # Continúa en el interior de la nave tras el aterrizaje
    scene bg nave with dissolve

    # 1. Primer personaje (Miquel) entra y dice su primera frase centrado
    $ set_char_pos("Miquel", "center")
    show miquel_mediocuerpo at pos_centro with dissolve

    M "Comandante..."

    T "Hmm... 5 minutos más"

    M "Despierta, anda, que se nos hará muy tarde para llegar al asentamiento."

    T "¿Qué hora es?"

    # 2. Entra el segundo personaje (Hanna):
    # - El primer personaje (Miquel) se desplaza a la izquierda (pequeño y transparente)
    # - El segundo personaje (Hanna) aparece en el centro para decir su primer diálogo
    $ set_char_pos("Miquel", "left")
    show miquel_mediocuerpo at mover_izq_idle
    $ set_char_pos("Hanna", "center")
    show hanna_mediocuerpo_seria at pos_centro with dissolve

    # 3. El segundo personaje dice su primera línea centrada
    H "Vaya siesta te has echado."

    # 4. DESPUÉS de su primera línea de diálogo, el segundo personaje se mueve a la derecha
    $ set_char_pos("Hanna", "right")
    show hanna_mediocuerpo_seria at mover_der_habla
    with None
    $ renpy.pause(0.45, hard=False)

    # 5. Continúa la conversación:
    # Quien habla recupera tamaño y opacidad completa en su lado.
    # Quien calla se reduce y transparenta automáticamente.
    H "Sí que estabas cansado."

    H "*Enciende la luz*"

    H "Buenos días, estamos en Marte, ¿recuerdas?"

    T "*frotándote los ojos* Solo me he echado una buena siesta... No me he quedado inconsciente."

    H "Anda, hazte un café, que te necesitamos fresco."

    # Salida de la escena hacia la cocina
    hide miquel_mediocuerpo
    hide hanna_mediocuerpo_seria
    with dissolve

    menu:
        "Ir a la cocina":
            pass

    # Escena de la cocina de la nave
    scene bg cocina_nave with fade

    T "*Te haces un café*"

    T "Echo de menos el café de casa."

    T "*Mientras tomas tu café, revisas la información de la tablet.*"

label tripulacion:

    menu:
        "¿Sobre quién quieres consultar información?"

        "Hanna":
            show hanna_cuerpoentero at pos_centro with dissolve
            H "Mujer, 31 años, Japonesa."
            H "Encargada de la Robótica y las Telecomunicaciones de la nave."
            hide hanna_cuerpoentero with dissolve
            jump tripulacion

        "Miquel":
            show miquel_cuerpoentero at pos_centro with dissolve
            M "Hombre, 29 años, Catalán / Estadounidense."
            M "Piloto e ingeniero mecánico."
            hide miquel_cuerpoentero with dissolve
            jump tripulacion

        "Nelson":
            show nelson_cuerpoentero at pos_centro with dissolve
            N "Hombre, 34 años, Senegalés."
            N "Médico y químico."
            hide nelson_cuerpoentero with dissolve
            jump tripulacion

        "Comandante (Tú)":
            T "Comandante de la misión. Biólogo y geólogo."
            jump tripulacion

        "Continuar":
            jump llegada_asentamiento

label llegada_asentamiento:

    T "Qué buen equipo tengo..."

    T "Tengo buenas expectativas de esta misión."

    show nelson_mediocuerpo at pos_centro with dissolve

    N "Comandante, ¿estás preparado?"

    N "Nos vamos cuanto antes."

    T "Vámonos."

    hide nelson_mediocuerpo with dissolve

    scene black with fade
    "De camino al asentamiento..."

    scene bg base_marte with fade
    "Ya estamos en el asentamiento."

    T "Hana, ¿por qué tardas tanto en activar la energía?"

    show hanna_mediocuerpo_seria at pos_centro with dissolve

    H "Comandante, no entiendo qué ocurre... no funciona."

    hide hanna_mediocuerpo_seria with dissolve

    "Vas a ayudarla."

    T "Hana, mientras hago la secuencia de encendido, tú tienes que mantener el botón pulsado."

    T "Chicos, hoy solo os voy a pedir que me hagáis un informe de los recursos disponibles."

    "Para hablar con tus compañeros selecciona su opción."

    "Vayamos a hablar con Nelson."

label tripulation:

    menu:
        "Hablar con Nelson":
            show nelson_mediocuerpo at pos_centro with dissolve
            N "Hola comandante, te comparto el informe actual de los niveles de O2 y temperatura."
            T "Genial Nelson, muchas gracias."
            N "Por cierto, ¿qué te parecen las instalaciones?"
            N "Están muy bien hechas, son más modernas y acogedoras de lo que esperaba..."
            N "Pero podrían haber dejado esterilizados los utensilios."
            T "Vaya, qué lástima. Buena suerte esterilizando."
            hide nelson_mediocuerpo with dissolve
            "Ahora veamos qué tiene que decirnos Hana."
            jump tripulation

        "Hablar con Hanna":
            show hanna_mediocuerpo_seria at pos_centro with dissolve
            T "Hola Hana, ¿cómo llevas el informe?"
            H "Por ahora estos son los parámetros de radiación."
            H "Las comunicaciones están en buen estado."
            T "Perfecto, muchas gracias."
            T "Bueno, te dejo tranquila."
            hide hanna_mediocuerpo_seria with dissolve
            jump tripulation

        "Hablar con Miquel":
            show miquel_mediocuerpo at pos_centro with dissolve
            M "¡Comandante! Te estaba esperando."
            T "Veamos qué tienes para mí."
            M "Mira, los suministros y vehículos están listos para la inspección."
            hide miquel_mediocuerpo with dissolve
            jump tripulation

        "Terminar revisiones y continuar":
            jump fin_reunion_asentamiento

label fin_reunion_asentamiento:

    T "Todos los informes iniciales están en orden. Es hora de comenzar el trabajo en Marte."

    # Aquí continuará la siguiente fase de la misión
    return
