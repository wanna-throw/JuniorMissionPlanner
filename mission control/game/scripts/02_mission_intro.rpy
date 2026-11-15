## 02_mission_intro.rpy - Introducción reestructurada: Rueda de Prensa -> Control de Misión -> Mapa

label intro_aphrodite:

    # 1. Rueda de Prensa: Presentación pública del programa y la misión Aphrodite 3
    scene bg rueda_prensa with fade

    c "Estamos en el año 2052."

    c "La tecnología ha avanzado tanto que la NASA está llevando a cabo el programa más ambicioso de la historia de la humanidad..."

    c "Se trata del programa Aphrodite, el cual tiene dos principales objetivos:"

    c "Buscar vida más allá de la Tierra..."

    c "Y crear asentamientos científicos de larga duración en otros planetas."

    c "Hoy se anuncia al mundo el lanzamiento de la misión Aphrodite 3."

    c "El objetivo principal es llevar recursos al asentamiento desarrollado en las misiones Aphrodite 1 y 2..."

    c "Y dar comienzo formal a la búsqueda de biofirmas y vida en la superficie de Marte."

    # 2. Centro de Control de Misión: Tu papel como comandante
    scene bg control_mission with fade

    c "Nos encontramos en las instalaciones de Control de Misión de la NASA."

    c "Tú eres el comandante de la misión Aphrodite 3."

    c "El cohete y la tripulación están listos para partir hacia el planeta rojo..."

    c "Pero antes de fijar el rumbo final, tú como comandante tendrás que tomar una decisión crucial."

    c "Debes analizar los informes de viabilidad científica y decidir el lugar de aterrizaje de la expedición."

    c "Cargando mapa cartográfico de Marte..."

    # Pre-cargar en memoria VRAM las imágenes de las fichas para que abran al instante
    $ renpy.start_predict("images/crater_mawrth.png", "images/crater_eberswalde.png", "images/crater_holden.png", "images/crater_gale.png", "images/fondo_tech.png")

    # 3. Pantalla interactiva del mapa de Marte (selección de sitio)
    call screen mapa_interactivo

    $ renpy.stop_predict("images/crater_mawrth.png", "images/crater_eberswalde.png", "images/crater_holden.png", "images/crater_gale.png", "images/fondo_tech.png")

# =============================================================
# 4. Confirmación tras elegir el sitio de aterrizaje en el mapa
# =============================================================
label confirmar_aterrizaje:

    scene bg control_mission with dissolve

    c "Coordenadas de aterrizaje fijadas en [lugar_aterrizaje]."

    c "Datos de telemetría cargados con éxito en la computadora de navegación de la nave."

    c "Todo listo. Iniciando cuenta atrás para el despegue..."

    # Transición al viaje espacial y aterrizaje
    scene black with fade

    c "El lanzamiento de la nave se llevó a cabo el pasado 6 de Junio, del 2052, a las 18:00 UTC."

    c "Después de 6 meses y 2 días de travesía por el espacio..."

    c "Y tras una maniobra de inserción orbital y frenado complicada..."

    c "¡Habéis logrado aterrizar con éxito en [lugar_aterrizaje]!"

    c "Ahora ya habrán pasado unas 2 horas..."

    # Salto a la nave tras el aterrizaje (despertar, Miquel, Hanna, café...)
    jump despertar_nave
