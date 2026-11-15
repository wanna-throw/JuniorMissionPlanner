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

    T "*Mientras tomas tu café, enciendes la tablet para consultar el informe de misión y el estado de la tripulación.*"

    # Inicialización de estado de la tablet en la cocina
    $ pantalla_actual = "reportaje"
    $ hambre_michael = 3
    $ sed_michael = 3
    $ hambre_hanna = 3
    $ sed_hanna = 3
    $ hambre_nelson = 3
    $ sed_nelson = 3
    $ hambre_user = 3
    $ sed_user = 3

label bucle_tablet:

    call screen tablet_cocina

    $ accion_tablet = _return

    if accion_tablet in ["miquel", "hanna", "nelson", "comandante"]:
        $ pantalla_actual = "personajes"
        call screen ficha_personaje(accion_tablet)
        $ pantalla_actual = "personajes"
        jump bucle_tablet

    elif accion_tablet == "continuar":
        jump llegada_asentamiento

label tripulacion:
    jump bucle_tablet

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



# =============================================================
# SISTEMA DE TABLET INTERACTIVA Y FICHAS DE PERSONAJES (COCINA)
# =============================================================

# VARIABLES DE LA TABLET
default pantalla_actual = "reportaje"

default hambre_michael = 3
default sed_michael = 3
default hambre_hanna = 3
default sed_hanna = 3
default hambre_nelson = 3
default sed_nelson = 3
default hambre_user = 3
default sed_user = 3


# INDICADOR DE NECESIDADES (COMIDA Y AGUA)
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


# SCREEN DE LA TABLET
screen tablet_cocina():

    # Sombra de fondo sobre la cocina
    add Solid("#00000066")

    if pantalla_actual == "reportaje":
        add "images/tablet_report.png":
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
                spacing 14

                text "INFORME DE MISIÓN":
                    size 26
                    bold True
                    color "#0f172a"

                text "PROGRAMA APHRODITE 3 (2052)":
                    size 17
                    bold True
                    color "#0284c7"

                text "El programa Aphrodite de la NASA tiene dos objetivos históricos fundamentales: la búsqueda formal de biofirmas de vida extraterrestre y el asentamiento científico permanente en Marte.":
                    size 17
                    color "#334155"

                text "ZONA DE ATERRIZAJE SELECCIONADA:":
                    size 17
                    bold True
                    color "#0284c7"

                text "Tras evaluar las opciones en Control de Misión, el Comandante fijó las coordenadas en [lugar_aterrizaje], una región clave con formaciones sedimentarias y alto potencial biológico.":
                    size 17
                    color "#334155"

                text "TRAVESÍA ESPACIAL:":
                    size 17
                    bold True
                    color "#0284c7"

                text "La nave despegó el 6 de junio de 2052 (18:00 UTC). Tras 6 meses y 2 días de travesía por el espacio profundo y una compleja maniobra de frenado orbital, el módulo tocó suelo con éxito.":
                    size 17
                    color "#334155"

                text "ESTADO TRAS EL ATERRIZAJE:":
                    size 17
                    bold True
                    color "#0284c7"

                text "Han transcurrido aproximadamente 2 horas desde el contacto. Tras una siesta reparadora en el módulo, la tripulación se reúne en la cocina para planificar el desembarco hacia la base marciana.":
                    size 17
                    color "#334155"

                null height 10

                text "💡 Consulta la pestaña de 'Personajes' para revisar el estado y perfil de cada miembro del equipo.":
                    size 15
                    italic True
                    color "#64748b"


    elif pantalla_actual == "personajes":
        add "images/tablet_personajes.png":
            xalign 0.5
            yalign 0.65
            zoom 0.75

        # Indicadores con suministros llenos (3/3)
        use indicador_necesidad(hambre_michael, "hambre", 790, 620)
        use indicador_necesidad(sed_michael, "sed", 790, 575)

        use indicador_necesidad(hambre_hanna, "hambre", 790, 920)
        use indicador_necesidad(sed_hanna, "sed", 790, 875)

        use indicador_necesidad(hambre_nelson, "hambre", 1050, 620)
        use indicador_necesidad(sed_nelson, "sed", 1050, 575)

        use indicador_necesidad(hambre_user, "hambre", 1050, 915)
        use indicador_necesidad(sed_user, "sed", 1050, 870)

        # 4 BOTONES INVISIBLES SOBRE CADA PERSONAJE:
        # 1. Miquel (Arriba Izquierda)
        button:
            xpos 660
            ypos 370
            xsize 270
            ysize 285
            background None
            hover_background Solid("#38bdf822")
            action Return("miquel")

        # 2. Nelson (Arriba Derecha)
        button:
            xpos 940
            ypos 370
            xsize 270
            ysize 285
            background None
            hover_background Solid("#38bdf822")
            action Return("nelson")

        # 3. Hanna (Abajo Izquierda)
        button:
            xpos 660
            ypos 670
            xsize 270
            ysize 285
            background None
            hover_background Solid("#38bdf822")
            action Return("hanna")

        # 4. Comandante / Tú (Abajo Derecha)
        button:
            xpos 940
            ypos 670
            xsize 270
            ysize 285
            background None
            hover_background Solid("#38bdf822")
            action Return("comandante")


    # BOTONES SUPERIORES DE NAVEGACIÓN EN LA TABLET
    button:
        xpos 700
        ypos 269
        xsize 65
        ysize 65
        background None
        hover_background Solid("#ffffff22")
        action SetVariable("pantalla_actual", "reportaje")

    button:
        xpos 802
        ypos 269
        xsize 65
        ysize 65
        background None
        hover_background Solid("#ffffff22")
        action SetVariable("pantalla_actual", "personajes")


    # BOTÓN INFERIOR: GUARDAR TABLET Y CONTINUAR HACIA EL ASENTAMIENTO
    frame:
        xalign 0.5
        ypos 1010
        background Solid("#0f172af2")
        padding (24, 8)

        textbutton "GUARDAR TABLET Y CONTINUAR MISIÓN ▶":
            text_size 20
            text_bold True
            text_color "#38bdf8"
            text_hover_color "#ffffff"
            action Return("continuar")


# SCREEN DE DETALLE DE PERSONAJE (EN LA COCINA)
screen ficha_personaje(quien):

    # Fondo único de la cocina
    add "bg cocina_nave"

    # Oscurecimiento de fondo para destacar la ficha técnica
    add Solid("#00000055")

    # Si es un compañero (Miquel, Hanna, Nelson): recuadro gris azulado con cuerpo entero y características
    if quien in ["miquel", "hanna", "nelson"]:
        frame:
            xalign 0.5
            yalign 0.44
            xsize 1460
            ysize 820
            background Solid("#1e293bee")
            padding (40, 30)

            hbox:
                spacing 40
                yalign 0.5

                # Contenedor de la imagen de cuerpo entero
                frame:
                    xsize 440
                    ysize 750
                    background Solid("#0f172a99")
                    padding (10, 10)

                    if quien == "miquel":
                        add "images/characters/miquel_cuerpoentero.png":
                            xalign 0.5
                            yalign 1.0
                            ysize 730
                            fit "contain"
                    elif quien == "hanna":
                        add "images/characters/hanna_cuerpoentero.png":
                            xalign 0.5
                            yalign 1.0
                            ysize 730
                            fit "contain"
                    elif quien == "nelson":
                        add "images/characters/nelson_cuerpoentero.png":
                            xalign 0.5
                            yalign 1.0
                            ysize 730
                            fit "contain"

                # Bloque de características técnicas
                vbox:
                    spacing 16
                    xsize 900
                    yalign 0.5

                    if quien == "miquel":
                        text "MIQUEL":
                            size 44
                            bold True
                            color "#7ed957"

                        text "Piloto de la Misión & Ingeniero Mecánico":
                            size 24
                            bold True
                            color "#94a3b8"

                        null height 10

                        frame:
                            background Solid("#0f172acc")
                            padding (25, 20)
                            xfill True

                            vbox:
                                spacing 12
                                text "{b}• Edad:{/b} 29 años" size 20 color "#e2e8f0"
                                text "{b}• Origen:{/b} Catalán / Estadounidense" size 20 color "#e2e8f0"
                                text "{b}• Especialidad:{/b} Pilotaje orbital, sistemas mecánicos de aterrizaje y mantenimiento de hábitats." size 20 color "#e2e8f0"
                                text "{b}• Rol en la misión:{/b} Responsable de las maniobras de navegación de la nave Aphrodite 3, de los sistemas motrices de los rovers y de la integridad mecánica de la base." size 20 color "#e2e8f0"
                                text "{b}• Estado de suministros:{/b} Comida 3/3 | Agua 3/3 (Plenamente operativo)" size 20 color "#7ed957"

                    elif quien == "hanna":
                        text "HANNA":
                            size 44
                            bold True
                            color "#ff751f"

                        text "Especialista en Robótica & Telecomunicaciones":
                            size 24
                            bold True
                            color "#94a3b8"

                        null height 10

                        frame:
                            background Solid("#0f172acc")
                            padding (25, 20)
                            xfill True

                            vbox:
                                spacing 12
                                text "{b}• Edad:{/b} 31 años" size 20 color "#e2e8f0"
                                text "{b}• Origen:{/b} Japonesa" size 20 color "#e2e8f0"
                                text "{b}• Especialidad:{/b} Redes de telecomunicación espacial, bio-robótica e instrumentación de laboratorio." size 20 color "#e2e8f0"
                                text "{b}• Rol en la misión:{/b} Gestión del enlace cuántico con la Tierra, calibración de sensores espectrométricos y dirección del instrumental robótico de prospección." size 20 color "#e2e8f0"
                                text "{b}• Estado de suministros:{/b} Comida 3/3 | Agua 3/3 (Plenamente operativa)" size 20 color "#ff751f"

                    elif quien == "nelson":
                        text "NELSON":
                            size 44
                            bold True
                            color "#f423a3"

                        text "Oficial Médico & Bioquímico de la Expedición":
                            size 24
                            bold True
                            color "#94a3b8"

                        null height 10

                        frame:
                            background Solid("#0f172acc")
                            padding (25, 20)
                            xfill True

                            vbox:
                                spacing 12
                                text "{b}• Edad:{/b} 34 años" size 20 color "#e2e8f0"
                                text "{b}• Origen:{/b} Senegalés" size 20 color "#e2e8f0"
                                text "{b}• Especialidad:{/b} Fisiología espacial, química analítica y soporte vital ambiental." size 20 color "#e2e8f0"
                                text "{b}• Rol en la misión:{/b} Monitorización biológica de la tripulación, análisis químico de muestras del suelo y supervisión de los sistemas de filtrado de aire y agua." size 20 color "#e2e8f0"
                                text "{b}• Estado de suministros:{/b} Comida 3/3 | Agua 3/3 (Plenamente operativo)" size 20 color "#f423a3"

    # Si el jugador se clica a sí mismo (Comandante): solo características, sin foto de cuerpo entero
    elif quien == "comandante":
        frame:
            xalign 0.5
            yalign 0.44
            xsize 1140
            ysize 680
            background Solid("#1e293bee")
            padding (50, 40)

            vbox:
                spacing 20
                yalign 0.5

                text "COMANDANTE (TÚ)":
                    size 44
                    bold True
                    color "#8c52ff"

                text "Líder de la Expedición Aphrodite 3 & Dirección Científica":
                    size 24
                    bold True
                    color "#94a3b8"

                frame:
                    background Solid("#0f172acc")
                    padding (35, 30)
                    xfill True

                    vbox:
                        spacing 14
                        text "{b}• Rango:{/b} Comandante en Jefe de la misión marciana Aphrodite 3." size 21 color "#e2e8f0"
                        text "{b}• Especialidad:{/b} Biólogo y geólogo planetario." size 21 color "#e2e8f0"
                        text "{b}• Responsabilidades:{/b} Máxima autoridad en la toma de decisiones estratégicas, asignación y aprobación de misiones operativas, y coordinación científica del asentamiento." size 21 color "#e2e8f0"
                        text "{b}• Objetivo Principal:{/b} Garantizar la supervivencia de la tripulación, liderar la prospección de biofirmas y asegurar la habitabilidad a largo plazo en Marte." size 21 color "#e2e8f0"
                        text "{b}• Estado de suministros:{/b} Comida 3/3 | Agua 3/3 (En perfectas condiciones)" size 21 color "#8c52ff"

    # Botón en la esquina inferior izquierda: Volver a la tablet
    frame:
        xpos 60
        ypos 970
        background Solid("#0f172af5")
        padding (22, 10)

        textbutton "◀  VOLVER A LA TABLET":
            text_size 22
            text_bold True
            text_color "#38bdf8"
            text_hover_color "#ffffff"
            action Return()
