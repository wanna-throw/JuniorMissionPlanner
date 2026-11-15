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

    # Diálogo con Hanna: detección del fallo en el sistema eléctrico
    $ set_char_pos("Hanna", "center")
    show hanna_mediocuerpo_seria at pos_centro with dissolve

    H "¡Comandante! Menos mal que llegas."

    H "He detectado un fallo grave en el sistema eléctrico de la base."

    H "La energía no llega a las instalaciones centrales y los paneles principales están apagados."

    T "¿Sabemos qué está provocando la avería?"

    H "Se trata de una sobrecarga en la caja de fusibles. Tienes que ir a revisarla y reconectar los plomos."

    T "Entendido. Voy a inspeccionar el cuadro eléctrico ahora mismo."

    H "Ten mucho cuidado, Comandante: debes activar los fusibles siguiendo la secuencia exacta para restablecer el flujo sin dañar el circuito."

    H "Te he dejado la secuencia indicada en la pantalla del panel. ¡Buena suerte!"

    hide hanna_mediocuerpo_seria with dissolve

    "Te diriges hacia el panel de distribución eléctrica de la base..."

    # -------------------------------------------------------------
    # MINIJUEGO: CUADRO ELÉCTRICO Y FUSIBLES (Importado de test1)
    # -------------------------------------------------------------
    $ sequence = renpy.random.sample(range(6), 6)
    $ fuses = [False, False, False, False, False, False]
    $ current_step = 0
    $ sequence_text = " -> ".join(str(x + 1) for x in sequence)

    call screen cuadro_electrico

    # -------------------------------------------------------------
    # RESOLUCIÓN TRAS COMPLETAR EL MINIJUEGO
    # -------------------------------------------------------------
    scene bg base_marte with fade

    "¡CLIC! El último fusible encaja en su posición correcta."

    "Un zumbido potente recorre la base mientras las luces y los sistemas de ventilación vuelven a la vida."

    $ set_char_pos("Hanna", "center")
    show hanna_mediocuerpo_seria at pos_centro with dissolve

    H "¡Increíble, Comandante! La energía ha vuelto a todos los sectores."

    H "El sistema eléctrico está funcionando al 100%% de su capacidad."

    T "Excelente trabajo en equipo. Ahora que la base tiene energía estable, comprobemos el estado del resto de recursos."

    hide hanna_mediocuerpo_seria with dissolve

    T "Chicos, antes de descansar, necesito que cada uno me prepare un informe detallado desde su puesto de trabajo."

    T "Esos informes definirán nuestras misiones prioritarias para mañana."

    jump tripulation

# =============================================================
# RONDA DE INFORMES Y MISIONES PARA EL DÍA SIGUIENTE
# =============================================================
label tripulation:

    scene bg base_marte with dissolve

    menu:
        "¿A qué área del asentamiento deseas dirigirte?"

        "Ir al Laboratorio de Geología (Hablar con Nelson) (Completado)" if informe_nelson:
            jump informe_nelson_dialogo

        "Ir al Laboratorio de Geología (Hablar con Nelson)" if not informe_nelson:
            jump informe_nelson_dialogo

        "Ir al Puesto de Bio-Robótica (Hablar con Hanna) (Completado)" if informe_hanna:
            jump informe_hanna_dialogo

        "Ir al Puesto de Bio-Robótica (Hablar con Hanna)" if not informe_hanna:
            jump informe_hanna_dialogo

        "Ir al Taller de Mantenimiento (Hablar con Miquel) (Completado)" if informe_miquel:
            jump informe_miquel_dialogo

        "Ir al Taller de Mantenimiento (Hablar con Miquel)" if not informe_miquel:
            jump informe_miquel_dialogo

        "Reunir al equipo y planificar el Día 2" if (informe_nelson and informe_hanna and informe_miquel):
            jump fin_reunion_asentamiento

# -------------------------------------------------------------
# 1. INFORME DE NELSON: INVESTIGAR LA GEOLOGÍA DE LA ZONA
# -------------------------------------------------------------
label informe_nelson_dialogo:

    scene bg centro_nelson with fade

    $ set_char_pos("Nelson", "center")
    show nelson at pos_centro with dissolve

    if not informe_nelson:
        N "¡Hola, Comandante! Pasa, estaba analizando los primeros escaneos del terreno exterior."

        T "Hola, Nelson. ¿Qué conclusiones has sacado de las muestras del suelo marciano?"

        show nelson pensativo with dissolve

        N "Las formaciones rocosas alrededor de nuestra zona de aterrizaje son fascinantes."

        N "Los sensores espectrales muestran capas sedimentarias muy ricas en minerales hidratados y sulfatos."

        N "Aquí está mi propuesta de informe: para mañana, nuestra misión principal debe ser {b}investigar la geología de la zona{/b}."

        N "Necesitamos salir con el equipo de prospección, perforar los estratos del cráter y recolectar testigos de roca para datar la antigüedad del terreno."

        show nelson with dissolve

        T "Excelente informe, Nelson. Entender la geología del terreno nos dirá si este suelo es seguro para levantar nuevas estructuras."

        N "Exacto. Prepararé los taladros geológicos y los contenedores estancos para la expedición de mañana."

        $ informe_nelson = True
        "Has recibido y aprobado el informe geológico de Nelson para el Día 2."

    else:
        N "Todo el equipo geológico está listo y calibrado para la misión de mañana, Comandante."
        T "Perfecto Nelson, descansa un poco antes de la salida."

    hide nelson with dissolve
    jump tripulation

# -------------------------------------------------------------
# 2. INFORME DE HANNA: BÚSQUEDA DE VIDA EN MUESTRAS DE AGUA
# -------------------------------------------------------------
label informe_hanna_dialogo:

    scene bg centro_hanna with fade

    $ set_char_pos("Hanna", "center")
    show hanna at pos_centro with dissolve

    if not informe_hanna:
        H "Comandante, estaba esperando que vinieras. Tienes que ver lo que han registrado las sondas profundas."

        T "Te noto entusiasmada, Hanna. ¿Qué han detectado los sensores?"

        show hanna sorprendida with dissolve

        H "A escasos tres metros bajo el regolito marciano... ¡hemos localizado bolsas de humedad y hielo salino!"

        H "Esto cambia por completo nuestras prioridades científicas."

        show hanna pensativa with dissolve

        H "El objetivo primordial del programa Aphrodite es encontrar vida más allá de la Tierra, y el agua líquida es el ingrediente clave."

        H "Mi informe para mañana establece la misión: {b}investigar muestras de agua en busca de vida extraterrestre{/b}."

        H "Debemos extraer muestras de ese hielo subterráneo con sondas estériles y examinarlas en el microscopio biológico buscando microbios o fósiles bacterianos."

        show hanna seria with dissolve

        T "Un hallazgo impresionante, Hanna. Buscar vida extraterrestre es el sueño de la humanidad. Tendrás prioridad absoluta en el laboratorio mañana."

        H "¡Muchas gracias, Comandante! Ya estoy esterilizando las placas de cultivo y el secuenciador genético."

        $ informe_hanna = True
        "Has recibido y aprobado el informe biológico de Hanna para el Día 2."

    else:
        H "Los analizadores de muestras de agua están al 100%% de potencia. ¡Mañana buscaremos microorganismos marcianos!"
        T "Buen trabajo, Hanna. Mantén todo estéril para no contaminar las muestras."

    hide hanna with dissolve
    jump tripulation

# -------------------------------------------------------------
# 3. INFORME DE MIQUEL: MANTENIMIENTO A LA BASE
# -------------------------------------------------------------
label informe_miquel_dialogo:

    scene bg centro_miquel with fade

    $ set_char_pos("Miquel", "center")
    show miquel at pos_centro with dissolve

    if not informe_miquel:
        M "¡Hombre, Comandante! Menos mal que te pasas por el hangar."

        T "Hola, Miquel. ¿Cómo se encuentran los vehículos y los sistemas del módulo tras el aterrizaje?"

        show miquel pensativo with dissolve

        M "El aterrizaje fue duro y el polvo marciano se mete en todas partes. Acabo de revisar las juntas de la compuerta y los filtros exteriores."

        M "Además, con el fallo eléctrico que acabamos de reparar, las líneas de potencia y los conectores auxiliares necesitan una revisión a fondo."

        show miquel sonriendo with dissolve

        M "Por eso mi informe para mañana es vital: {b}hacer mantenimiento general a la base{/b}."

        M "Debemos limpiar los paneles solares del polvo marciano, reforzar los sellos de presurización de las esclusas y poner a punto los motores de los rovers para que el equipo pueda salir sin peligro."

        T "Totalmente de acuerdo, Miquel. Sin una base segura y presurizada, ningún científico podrá hacer su trabajo. Tu misión es la columna vertebral del equipo."

        M "¡Cuenta con ello, jefe! Mañana dejaré la base como recién salida de fábrica."

        $ informe_miquel = True
        "Has recibido y aprobado el informe de mantenimiento de Miquel para el Día 2."

    else:
        M "Tengo las llaves dinamométricas y los filtros de repuesto listos para el mantenimiento de mañana."
        T "Bien hecho, Miquel. Nos vemos en la reunión final."

    hide miquel with dissolve
    jump tripulation

# =============================================================
# REUNIÓN FINAL DE LA TRIPULACIÓN: PLANIFICACIÓN DEL DÍA 2
# =============================================================
label fin_reunion_asentamiento:

    scene bg base_marte with fade

    "Con los tres informes en mano, reúnes a toda la tripulación en la sala central de mando de la base."

    # Aparecen los tres tripulantes en sus puestos
    $ set_char_pos("Nelson", "left")
    $ set_char_pos("Hanna", "center")
    $ set_char_pos("Miquel", "right")

    show nelson at pos_izq_idle
    show hanna at pos_centro_idle
    show miquel at pos_der_idle
    with dissolve

    T "Tripulación de la misión Aphrodite 3: hemos superado el viaje espacial, el aterrizaje y la primera emergencia eléctrica."

    T "He revisado vuestros tres informes y cada uno tiene una misión esencial para mañana:"

    T "1. {b}Miquel:{/b} Realizará el mantenimiento general de la base, limpiando paneles solares y asegurando los rovers."

    T "2. {b}Nelson:{/b} Liderará la expedición exterior para investigar la geología del terreno y perforar los estratos rocosos."

    T "3. {b}Hanna:{/b} Procesará las muestras de agua subterránea en el laboratorio en busca de biofirmas y vida extraterrestre."

    show miquel sonriendo at pos_der_habla with dissolve
    M "¡Entendido, Comandante! La base estará en las mejores manos."

    show hanna seria at pos_centro_habla with dissolve
    H "Los microscopios están listos. Espero que mañana hagamos historia."

    show nelson at pos_izq_habla with dissolve
    N "Será un día de grandes descubrimientos geológicos. ¡A por todas, equipo!"

    T "Buen trabajo a todos en nuestro primer día en el planeta rojo. Ahora, a descansar."

    # Despedida y transición de noche
    hide nelson
    hide hanna
    hide miquel
    with dissolve

    scene black with fade

    "Las luces de la base marciana se atenúan al entrar en ciclo nocturno."

    "La tripulación de la Aphrodite 3 descansa en sus camarotes, recuperando energías tras un viaje de millones de kilómetros..."

    "El primer día en Marte ha concluido con éxito."

    "DÍA 2: COMIENZA LA EXPLORACIÓN..."

    # Fin del Día 1
    return
