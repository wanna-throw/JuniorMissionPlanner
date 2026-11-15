## 02_mission_intro.rpy - Prólogo y primera escena de la misión

label intro_aphrodite:

    # 1. Comienza la escena dentro de la nave espacial con transición suave
    scene bg nave with fade

    # Diálogos introductorios narrados por C
    c "Estamos en el año 2052."

    c "La tecnología ha avanzado tanto que la NASA está llevando a cabo el programa más ambicioso de la historia de la humanidad..."

    c "Se trata del programa Aphrodite, el cual tiene dos principales objetivos..."

    c "Buscar vida más allá de la Tierra..."

    c "Y crear asentamientos científicos de larga duración en otros planetas."

    c "Eres el comandante de la misión Aphrodite 3."

    c "El objetivo de la misión es llevar recursos al asentamiento desarrollado en las misiones Aphrodite 1 y 2..."

    c "Y empezar la búsqueda de vida extraterrestre."

    c "El lanzamiento de la nave se llevó a cabo el pasado 6 de Junio, del 2052, a las 18:00 UTC."

    c "Después de 6 meses y 2 días..."

    c "Y tras una maniobra de inserción orbital y frenado complicada..."

    c "Habéis logrado aterrizar."

    c "Ahora ya habrán pasado unas 2 horas."

    # Salto a la escena de despertar e interacción con la tripulación
    jump despertar_nave

