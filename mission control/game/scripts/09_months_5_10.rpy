## 09_months_5_10.rpy - Months 5 to 10: long-term survival until the end of the
## 10-month mission (300 days). Every month the environment changes and one
## realistic event (based on NASA systems: MOXIE, ECLSS, solar panels...) happens.

default current_month = 5

## (title, report lines, energy, water, food, oxygen, thermal)
define MONTH_EVENTS = {
    5: ("A DUST DEVIL CLEANS THE PANELS",
        ["A dust devil swept across the base during the afternoon. Like the ones that cleaned the panels of the Spirit and Opportunity rovers, it blew the dust off our solar arrays."],
        8, 0, 0, 0, 0),
    6: ("MOXIE MAINTENANCE",
        ["Hanna and Miquel serviced the oxygen production unit. It works like NASA's MOXIE: it splits the CO2 of the Martian atmosphere at about 800 °C to obtain oxygen.",
         "The cleaned filters improved its production."],
        -5, 0, 0, 8, 0),
    7: ("ECLSS FILTER REPLACEMENT",
        ["The water recycling filters were clogged with mineral residues. Nelson analyzed them and confirmed that the recycled water was still safe to drink.",
         "Replacing them used up some stored water."],
        0, -10, 0, 0, 0),
    8: ("FIRST BIG GREENHOUSE HARVEST",
        ["The hydroponic greenhouse has completed its first big cycle. Lettuce, radishes and potatoes grown without soil, using recycled water and LED light."],
        0, 0, 15, 0, 0),
    9: ("SOLAR CONJUNCTION",
        ["Mars is behind the Sun as seen from Earth. During this solar conjunction, radio communications are interrupted for about two weeks.",
         "Hanna kept the antenna in safe mode. The crew worked alone, without help from Earth."],
        0, 0, 0, 0, -5),
    10: ("LAST MONTH ON MARS",
        ["The return window to Earth is about to open. The crew is packing the samples in sealed containers and preparing the spacecraft."],
        0, 0, 0, 0, 0),
}

label month_cycle:

    $ day = 30 * (current_month - 1) + 1
    $ set_chapter(6 + current_month)
    $ gained = produce_energy(20)
    $ crew_gets_hungry()
    $ month_passes()
    $ ev = MONTH_EVENTS[current_month]
    $ res_energy += ev[2]
    $ res_water += ev[3]
    $ res_food += ev[4]
    $ res_oxygen += ev[5]
    $ res_thermal += ev[6]
    $ clamp_resources()

    $ month_title = "MONTH %d" % current_month
    $ month_sub = "%d months on Mars" % (current_month - 1)
    call screen day_title(month_title, month_sub)

    scene bg control_room_crew with fade

    python:
        changes = []
        for amount, name in ((ev[2], "energy"), (ev[3], "water"), (ev[4], "food"), (ev[5], "oxygen"), (ev[6], "temperature")):
            if amount:
                changes.append(("good" if amount > 0 else "bad", "%+d %s" % (amount, name)))
        report = [
            ("title", "REPORT - MONTH %d" % current_month),
            ("good", "The panels and the reactor produced +%d energy this month." % gained),
            ("head", ev[0]),
        ] + [("text", t) for t in ev[1]] + changes + [
            ("head", "ENVIRONMENT (MONTHLY)"),
            ("bad", "Oxygen -10%%, temperature -10%%, radiation +%d%%." % res_radiation_rate),
            ("head", "THE CREW"),
            ("bad", "Everyone has lost 1 food bar and 1 water bar."),
            ("head", "MISSION"),
            ("text", "Days on Mars: %d of 300. Samples secured: %d." % (day, samples_collected)),
        ]
    $ open_tablet(report, cont=("END THE MISSION ▶" if current_month == 10 else "END THE MONTH ▶"))

    call screen day_tablet

    $ check_crew_neglect()
    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    # Short scene with the crew every month
    if current_month == 6:
        scene bg hanna_station with fade
        $ set_char_pos("Hanna", "center")
        show hanna thinking at pos_center with dissolve
        H "The oxygen sensors look stable again. MOXIE is noisy, but it's doing its job."
        hide hanna with dissolve
    elif current_month == 7:
        scene bg nelson_station with fade
        $ set_char_pos("Nelson", "center")
        show nelson thinking at pos_center with dissolve
        N "No bacteria, no heavy metals. The water is safe. Chemistry never lies."
        hide nelson with dissolve
    elif current_month == 8:
        scene bg ship_kitchen with fade
        $ set_char_pos("Miquel", "center")
        show miquel smiling at pos_center with dissolve
        M "Fresh potatoes on Mars! Commander, this is the best dinner we've had in months."
        hide miquel with dissolve
    elif current_month == 9:
        scene bg control_room_crew with fade
        T "Two weeks without contact with Earth. Now it really feels like we are alone on another planet."

    if current_month >= 10:
        jump mission_final

    $ current_month += 1

    scene black with fade
    "Another month goes by on the red planet..."

    jump month_cycle


label mission_final:

    scene bg control_room_crew with fade

    T "Crew, it's time to go home. Load the samples and prepare the spacecraft."

    if samples_collected >= 3 and crew_neglect <= 6:
        jump ending_good
    else:
        jump ending_bad
