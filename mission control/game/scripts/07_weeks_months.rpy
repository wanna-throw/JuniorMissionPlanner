## 07_weeks_months.rpy - Week 2, Week 3, Week 4, Month 2, Month 3 and Month 4.
## Expeditions: one crew member leads, but the whole crew always goes out together
## (the outdoor backgrounds show the three of them).
## Professions: Miquel = pilot & mechanical engineer, Hanna = robotics & telecommunications,
## Nelson = medical officer & chemist, Commander (you) = geologist & biologist.

define EMC = Character("URA Mission Control", color="#60a5fa")

default week2_leader = None
default month2_leader = None
default circuit_fixed = False

init python:
    def open_tablet(report, event=None, mission=False, cont="END THE DAY ▶"):
        store.day_report = add_passive_line(report) + resource_warnings()
        store.day_event = event
        store.events_seen = False
        store.day_needs_mission = mission
        store.mission_choice = None
        store.day_tab = "report"
        store.day_continue_text = cont

    def resource_warnings():
        """Alerts added at the end of every report when something is getting dangerous."""
        w = []
        if store.res_thermal <= 35:
            w.append(("bad", "ALERT: temperature at %d%%. Below 20%% the base is uninhabitable. Use HEAT THE BASE in the Crew tab." % store.res_thermal))
        if store.res_energy <= 15:
            w.append(("bad", "ALERT: energy at %d%%. If it reaches 0%%, every system shuts down." % store.res_energy))
        if store.res_oxygen <= 30:
            w.append(("bad", "ALERT: oxygen reserves at %d%%." % store.res_oxygen))
        if store.res_radiation >= 70:
            w.append(("bad", "ALERT: accumulated radiation at %d%%. At 100%% the crew must leave Mars." % store.res_radiation))
        if store.res_food <= 15:
            w.append(("bad", "ALERT: food reserves are very low. Produce food in the greenhouse (Crew tab)."))
        if store.res_water <= 15:
            w.append(("bad", "ALERT: water reserves are very low."))
        empty = [CREW_NAMES[k] for k in store.crew_hunger if store.crew_hunger[k] <= 0 or store.crew_thirst[k] <= 0]
        if empty:
            w.append(("bad", "ALERT: %s has an empty food or water bar. Give them a ration before ending the day, or the crew will have to abandon the base and return to Earth!" % ", ".join(empty)))
        if w:
            w = [("head", "WARNINGS")] + w
        return w

    def survival_failure():
        """Returns the ending to play if the base can no longer keep the crew alive, or None."""
        if store.res_radiation >= 100:
            return "radiation"
        if store.res_oxygen <= 0:
            return "oxygen"
        if store.res_thermal <= 20:
            return "thermal"
        if store.res_energy <= 0:
            return "power"
        rc = ration_cost()
        # Out of water or food: the crew does not die, they take the spacecraft back to Earth
        # If a crew member ends the day with an empty water/food bar (or the reserve is empty),
        # the crew evacuates and returns to Earth.
        if store.res_water <= 0 or any(store.crew_thirst[k] <= 0 for k in store.crew_thirst):
            return "water"
        if store.res_food <= 0 or any(store.crew_hunger[k] <= 0 for k in store.crew_hunger):
            return "food"
        return None


## =============================================================
## WEEK 2
## =============================================================
label week_2:

    $ day = 8
    $ set_chapter(5)
    $ gained = produce_energy(5)
    $ crew_gets_hungry()

    call screen day_title("WEEK 2", "Day 8 on Mars")

    scene bg control_room_crew with fade

    if solar_efficiency >= 100:
        $ week_report = [
            ("title", "REPORT - WEEK 2"),
            ("good", "You received +%d energy." % gained),
            ("text", "The first week on Mars is over, and there is good news! The solar panel knocked out of position by the sandstorm was repaired and is working normally again."),
            ("text", "Thanks to your work, the base receives all the energy it needs. The systems are in good condition and the experiments can continue without worrying about electricity."),
            ("text", "Good job, Commander! But don't relax yet: a new week begins and there is still a lot to discover on this planet."),
        ]
    else:
        $ week_report = [
            ("title", "REPORT - WEEK 2"),
            ("good", "You received +%d energy (only %d%% of the normal production)." % (gained, solar_efficiency)),
            ("text", "The first week on Mars is over, but there is a problem. The solar panel knocked out of position by the sandstorm is still not pointing at the Sun."),
            ("text", "The base keeps working, but the panel can't use all the sunlight and energy production has dropped. From now on, %d%% less energy will be generated every day." % SOLAR_FAIL_PENALTY),
            ("text", "You will have to watch the resources and think carefully about how to use the electricity. You can't afford any more problems!"),
        ]
    $ week_report += [
        ("head", "THE CREW"),
        ("bad", "Everyone has lost 1 food bar and 1 water bar."),
        ("text", "Open the Crew tab and scroll down to give them rations."),
        ("head", "EVENTS"),
        ("text", "There are no events for now."),
    ]
    $ open_tablet(week_report)

    call screen day_tablet

    $ check_crew_neglect()
    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    # The tablet turns off: main room of the base
    scene bg control_room_crew with dissolve

    T "Have you seen the report? It looks like we still have a lot of ground to explore near the base."

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve
    H "Absolutely! I'd love to know what's out there. We've been looking at the same landscape for days."
    hide hanna_halfbody_serious with dissolve

    T "Then we'll have to organize an expedition. We can't just sit here waiting for Mars to tell us its secrets."

    $ set_char_pos("Nelson", "center")
    show nelson_halfbody at pos_center with dissolve
    N "I think I should lead it. I could collect rock and mineral samples and run a chemical analysis when we get back. Maybe we'll find a substance that helps our experiments."
    hide nelson_halfbody with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve
    H "That's good, but I could use the trip to scan the area with my electronic equipment: detect signals, fly the scouting drone and check for anything we can't see with the naked eye."
    hide hanna_halfbody_serious with dissolve

    $ set_char_pos("Miquel", "center")
    show miquel_halfbody_smiling at pos_center with dissolve
    M "Don't forget about me! I could drive the exploration rover. I know its engines and mechanisms inside out, so we could cover more distance and cross rough terrain more safely."
    hide miquel_halfbody_smiling with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve
    H "Well, it looks like all three of us have something to offer."
    hide hanna_halfbody_serious with dissolve

    T "That's clear. What matters is that whoever leads explores the area well and comes back with as much information as possible."

    $ set_char_pos("Miquel", "center")
    show miquel_halfbody_smiling at pos_center with dissolve
    M "Exactly! Although, if you ask me, I'm ready to leave right now."
    hide miquel_halfbody_smiling with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve
    H "You're always in a hurry, Miquel!"
    hide hanna_halfbody_serious with dissolve

    $ set_char_pos("Miquel", "center")
    show miquel_halfbody_smiling at pos_center with dissolve
    M "It's not every day you get the chance to explore Mars!"
    hide miquel_halfbody_smiling with dissolve

    $ set_char_pos("Nelson", "center")
    show nelson_halfbody at pos_center with dissolve
    N "So, Commander... who do you think is the best person to lead this expedition?"
    hide nelson_halfbody with dissolve

    call screen expedition_choice_screen("WHO WILL LEAD THE EXPEDITION?", {
        "miquel": "Drives the rover",
        "nelson": "Chemical analysis",
        "hanna": "Drone and sensors"})

    $ week2_leader = _return
    $ record_mission(week2_leader)
    $ add_route(CREW_NAMES[week2_leader])
    $ samples_collected += 1

    scene bg expedition_day with fade

    if week2_leader == "nelson":
        "Nelson leads the expedition, and the whole crew suits up and heads out with him in the rover."
        N "Every rock here is a chemistry book. I'll use the portable spectrometer to see what they're made of."
        T "This layered outcrop is perfect. As a geologist, I'd say it formed in water a very long time ago."
        H "My robot will carry the sample boxes. Nelson, don't fill them all with the first rock you see!"
        "Hour after hour, the team chips samples from the outcrops and labels every container."
    elif week2_leader == "hanna":
        "Hanna leads the expedition, and the whole crew goes out with her. She launches a small scouting drone, like the Ingenuity helicopter, to map the area from the air."
        H "Drone online. The ground-penetrating radar is picking up something odd under the dust..."
        M "I'll park the rover on stable ground so your antenna has a clear signal."
        N "Remember the suit timers, everyone: we head back before the oxygen margin drops below 30 minutes."
        "Following the drone's map, the team digs where the radar showed the strongest echo."
    else:
        "Miquel leads the expedition at the wheel of the rover, with the whole crew aboard."
        M "Hold on tight! This slope is steep, but the suspension can take it."
        T "Stop here, Miquel. Look at that rock formation: it's cracked, as if something pushed from inside."
        H "My sensors read a temperature difference near the crack. Strange..."
        "Miquel drives the rover closer, and the crew gets out to take a better look."

    "At sunset, the whole team returns to the base with their findings."

    scene black with fade
    "The days go by. The crew settles into the routine of the base..."

    jump week_3


## =============================================================
## WEEK 3
## =============================================================
label week_3:

    $ day = 15
    $ set_chapter(6)
    $ gained = produce_energy(5)
    $ crew_gets_hungry()

    if week2_leader == "nelson":
        $ res_water += 20
        $ result = [
            ("head", "EXPEDITION RESULT"),
            ("text", "During the exploration, Nelson found some rocks with small crystals inside. When he analyzed them, he discovered that they contained traces of frozen water."),
            ("text", "He managed to collect a small amount of ice that, once treated, we can use to obtain water."),
            ("good", "+20 water"),
        ]
    elif week2_leader == "hanna":
        $ res_energy += 15
        $ result = [
            ("head", "EXPEDITION RESULT"),
            ("text", "While exploring the area, Hanna found some small devices covered in dust. After examining them, she recovered some parts that can be used to improve our equipment."),
            ("text", "With them, she also recovered part of the energy stored in some batteries that still worked."),
            ("good", "+15 energy"),
        ]
    else:
        $ res_water += 15
        $ result = [
            ("head", "EXPEDITION RESULT"),
            ("text", "During the expedition, Miquel found a small crack in a rock formation. When he drove the rover closer, he discovered a faint vapor coming out of it."),
            ("text", "Intrigued, he used the rover's tools to remove some rocks and found a small accumulation of ice protected from the Sun. He collected it and brought it back to the base."),
            ("good", "+15 water"),
        ]

    # The environment starts to change
    $ res_thermal -= 5
    $ res_radiation += max(1, res_radiation_rate // 2)
    $ clamp_resources()

    call screen day_title("WEEK 3", "Day 15 on Mars")

    scene bg control_room_crew with fade

    $ open_tablet([
        ("title", "REPORT - WEEK 3"),
        ("good", "You received +%d energy." % gained),
    ] + result + [
        ("head", "ENVIRONMENT"),
        ("bad", "Thermal stability and radiation are starting to change: temperature -5%%, radiation +%d%%." % max(1, res_radiation_rate // 2)),
        ("text", "Mars has no global magnetic field and a very thin atmosphere, so radiation slowly accumulates. Keep an eye on both indicators."),
        ("head", "THE CREW"),
        ("bad", "Everyone has lost 1 food bar and 1 water bar."),
        ("head", "EVENTS"),
        ("text", "There are no events for now."),
    ])

    call screen day_tablet

    $ check_crew_neglect()
    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    # Short scene with the expedition leader
    if week2_leader == "nelson":
        scene bg nelson_station with fade
        $ set_char_pos("Nelson", "center")
        show nelson thinking at pos_center with dissolve
        N "The crystals are hydrated minerals. When I heated them, the water condensed in the trap: pure enough after filtering."
        T "Then the ground around us is a water reserve. Great chemistry, Nelson."
        hide nelson with dissolve
    elif week2_leader == "hanna":
        scene bg hanna_station with fade
        $ set_char_pos("Hanna", "center")
        show hanna surprised at pos_center with dissolve
        H "Those devices were old weather sensors from a previous mission! Their battery cells still held charge."
        T "So someone was here before us. Good thinking, Hanna."
        hide hanna with dissolve
    else:
        scene bg miquel_station with fade
        $ set_char_pos("Miquel", "center")
        show miquel smiling at pos_center with dissolve
        M "The vapor was ice sublimating in the sunlight. Without the rover's drill we'd never have reached it."
        T "Ice protected from the Sun... that's exactly where it survives on Mars. Well done, Miquel."
        hide miquel with dissolve

    scene black with fade
    "Another week passes..."

    jump week_4


## =============================================================
## WEEK 4
## =============================================================
label week_4:

    $ day = 22
    $ set_chapter(7)
    $ gained = produce_energy(5)
    $ res_water += 5
    $ passive_income()

    call screen day_title("WEEK 4", "Day 22 on Mars")

    scene bg control_room_crew with fade

    $ open_tablet([
        ("title", "REPORT - WEEK 4"),
        ("good", "You received +%d energy." % gained),
        ("text", "A quiet week at the base. The crew has followed the routine without incidents."),
        ("head", "WATER RECYCLING"),
        ("text", "The ECLSS life-support system recovers water from the air humidity and from waste water, like on the International Space Station, where NASA reached about 98% water recovery."),
        ("good", "+5 water recovered"),
        ("head", "THE CREW"),
        ("text", "Nobody has lost food or water this week."),
        ("head", "EVENTS"),
        ("text", "There are no events for now."),
    ])

    call screen day_tablet

    $ check_crew_neglect()
    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    scene black with fade
    "The first month on Mars comes to an end..."

    jump month_2


## =============================================================
## MONTH 2
## =============================================================
label month_2:

    $ day = 31
    $ set_chapter(8)
    $ gained = produce_energy(5)
    $ crew_gets_hungry()
    $ month_passes()
    $ unlock("one_month")

    call screen day_title("MONTH 2", "One month on Mars")

    scene bg control_room_crew with fade

    $ open_tablet([
        ("title", "REPORT - MONTH 2"),
        ("good", "You received +%d energy." % gained),
        ("text", "Commander, we did it! The crew has been living on Mars for a whole month!"),
        ("text", "It has been weeks full of discoveries, experiments and the odd setback. We have learned to adapt to this new home and, little by little, the base works better and better."),
        ("text", "But this is only the beginning. There are still many places to explore, experiments to carry out and mysteries of Mars to discover."),
        ("head", "NEW OBJECTIVE"),
        ("text", "The second month on Mars begins! Keep managing the resources, looking after the base and working as a team to complete the mission."),
        ("head", "ENVIRONMENT (MONTHLY)"),
        ("bad", "Oxygen -10%%, temperature -10%%, radiation +%d%%." % res_radiation_rate),
        ("head", "THE CREW"),
        ("bad", "Everyone has lost 1 food bar and 1 water bar."),
        ("head", "EVENTS"),
        ("text", "There are no events for now."),
        ("good", "Keep it up, crew!"),
    ])

    call screen day_tablet

    $ check_crew_neglect()
    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    # The tablet turns off: main room of the base
    scene bg control_room_crew with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_thinking at pos_center with dissolve
    H "Hey, have you seen the latest images we received?"
    hide hanna_halfbody_thinking with dissolve

    $ set_char_pos("Miquel", "center")
    show miquel_halfbody_thinking at pos_center with dissolve
    M "What now? I hope it's not another sandstorm..."
    hide miquel_halfbody_thinking with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_surprised at pos_center with dissolve
    H "No, relax! I've been reviewing the drone photos of the surroundings and I found something quite strange. Look at this crater."
    hide hanna_halfbody_surprised with dissolve

    $ set_char_pos("Nelson", "center")
    show nelson_halfbody_thinking at pos_center with dissolve
    N "It looks pretty big. What's so special about it?"
    hide nelson_halfbody_thinking with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve
    H "It doesn't appear on any of our maps. And there are rock formations around it that I'd never seen before."
    hide hanna_halfbody_serious with dissolve

    T "Then we'll have to take a look! We didn't come all the way to Mars to stare at photographs. As a geologist, I want to know how that crater formed."

    $ set_char_pos("Nelson", "center")
    show nelson_halfbody at pos_center with dissolve
    N "I agree. I could collect samples and analyze their chemical composition."
    hide nelson_halfbody with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_serious at pos_center with dissolve
    H "We could also take my scanning equipment to analyze the area. Maybe we'll find something interesting!"
    hide hanna_halfbody_serious with dissolve

    $ set_char_pos("Miquel", "center")
    show miquel_halfbody at pos_center with dissolve
    M "And we'll need someone who can drive the rover in case the terrain gets tricky."
    hide miquel_halfbody with dissolve

    $ set_char_pos("Nelson", "center")
    show nelson_halfbody at pos_center with dissolve
    N "Well, Commander, what do you think? Shall we organize an expedition?"
    hide nelson_halfbody with dissolve

    $ set_char_pos("Hanna", "center")
    show hanna_halfbody_surprised at pos_center with dissolve
    H "Count me in! I think I could discover something interesting with my equipment."
    hide hanna_halfbody_surprised with dissolve

    $ set_char_pos("Miquel", "center")
    show miquel_halfbody_smiling at pos_center with dissolve
    M "Well, I want to go too!"
    hide miquel_halfbody_smiling with dissolve

    $ set_char_pos("Nelson", "center")
    show nelson_halfbody at pos_center with dissolve
    N "Don't forget about me! Someone will have to analyze everything we find."
    hide nelson_halfbody with dissolve

    call screen expedition_choice_screen("WHO DO WE SEND TO EXPLORE THE CRATER?", {
        "miquel": "Rover into the crater",
        "nelson": "Mineral analysis",
        "hanna": "Radar and signals"})

    $ month2_leader = _return
    $ record_mission(month2_leader)
    $ add_route(CREW_NAMES[month2_leader])
    $ samples_collected += 1

    scene bg expedition_night with fade

    if month2_leader == "nelson":
        "Nelson leads the crater expedition. The whole crew goes with him, reaching the rim as the light fades."
        N "Look at these colors: reds, yellows, almost green. Iron oxides and maybe sulfates."
        T "The layers go down the crater wall like the pages of a book. This place could be billions of years old."
        M "I'll keep the rover's lights on the slope so nobody slips."
    elif month2_leader == "hanna":
        "Hanna leads the crater expedition. The whole crew goes with her, carrying her radar and signal receivers."
        H "I'm picking up a weak, repeating radio signal... it's coming from under those rocks!"
        N "A signal? Out here? Careful, it could be an old power source."
        M "Leave the heavy lifting to me. I'll move the rocks with the rover's arm."
    else:
        "Miquel leads the crater expedition, driving the rover with the whole crew aboard."
        M "The north side has a much gentler slope. We can drive all the way down there."
        T "Look at the base of the wall... that dark opening isn't a shadow. It's a tunnel!"
        H "My sensors say the air inside is a few degrees warmer. Let's go in slowly."

    "Hours later, the team returns to the base with the rover full of samples and data."

    scene black with fade
    "Weeks of work go by..."

    jump month_3


## =============================================================
## MONTH 3 - EVENT: Short circuit
## =============================================================
label month_3:

    $ day = 61
    $ set_chapter(9)
    $ gained = produce_energy(10)
    $ crew_gets_hungry()
    $ month_passes()

    if month2_leader == "nelson":
        $ res_water += 10
        $ result = [
            ("head", "CRATER EXPEDITION RESULT"),
            ("text", "During the exploration, Nelson found some very colorful rocks. When he examined them, he discovered that they contain minerals that react when they come into contact with certain chemicals."),
            ("text", "Although he doesn't know exactly what they could be used for, he collected several samples for future experiments."),
            ("text", "On the way, he also discovered a small accumulation of ice in a sheltered area of the crater. Good news for the base's water reserve!"),
            ("good", "+10 water"),
        ]
    elif month2_leader == "hanna":
        $ res_energy += 10
        $ result = [
            ("head", "CRATER EXPEDITION RESULT"),
            ("text", "While investigating the crater, Hanna detected a signal that seemed to come from under some rocks."),
            ("text", "After locating its source, she discovered an old exploration probe that still kept part of its power system. She recovered some of its components and used its energy for the base."),
            ("good", "+10 energy"),
        ]
    else:
        $ res_water += 15
        $ res_energy += 5
        $ result = [
            ("head", "CRATER EXPEDITION RESULT"),
            ("text", "Along the way, Miquel discovered that one part of the crater had a much gentler slope than the rest. Investigating the area, he found an old natural tunnel crossing the rock formation, like the lava tubes seen from orbit."),
            ("text", "He drove the rover inside and found a small area protected from the outside, with a natural ice deposit and some equipment that still worked."),
            ("text", "He collected part of the ice and recovered the energy from the equipment before returning to the base."),
            ("good", "+15 water and +5 energy"),
        ]
    $ clamp_resources()

    call screen day_title("MONTH 3", "Two months on Mars")

    scene black

    "In the middle of the night, a dry crack echoes through the base. The lights flicker and go out..."

    scene bg control_room_crew with fade

    $ open_tablet([
        ("title", "REPORT - MONTH 3"),
        ("good", "You received +%d energy." % gained),
    ] + result + [
        ("head", "ENVIRONMENT (MONTHLY)"),
        ("bad", "Oxygen -10%%, temperature -10%%, radiation +%d%%." % res_radiation_rate),
        ("head", "THE CREW"),
        ("bad", "Everyone has lost 1 food bar and 1 water bar."),
        ("bad", "Alert! A short circuit has been detected. Go to the Events tab to find out more."),
    ], event=[
        ("title", "SHORT CIRCUIT"),
        ("text", "During the night, a short circuit occurred in one of the base's electrical systems. Some lights stopped working and several pieces of equipment suddenly shut down."),
        ("text", "Luckily, the affected area has been isolated, but the problem has not been solved yet. If it isn't repaired soon, part of the stored energy could be lost and other systems could be left without electricity."),
        ("head", "TODAY'S MISSION"),
        ("text", "Find the fault and repair the electrical circuit so that every system works properly again."),
        ("text", "The diagnostic display will show the correct fuse sequence for only 5 seconds: memorize it! You have 2 attempts."),
        ("bad", "WARNING!"),
        ("text", "If it isn't fixed, the base will lose 20 energy, and the laboratory freezer that stores our samples will lose power."),
    ], cont="REPAIR THE CIRCUIT ▶")

    call screen day_tablet

    $ check_crew_neglect()
    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    scene bg mars_base with fade

    $ set_char_pos("Miquel", "center")
    show miquel_halfbody_thinking at pos_center with dissolve
    M "The breaker panel is still smoking. A cable melted inside the junction box, so the fuses have to be reset in the right order."
    M "If we switch them on in the wrong order, the surge will burn the rest of the circuit."
    hide miquel_halfbody_thinking with dissolve

    T "Then let's do it carefully. Show me the diagnostic sequence."

    $ sequence = renpy.random.sample(range(6), 6)
    $ fuses = [False, False, False, False, False, False]
    $ current_step = 0
    $ sequence_text = " -> ".join(str(x + 1) for x in sequence)
    $ fuse_event_mode = True
    $ fuse_attempts = 2

    call screen electrical_panel

    $ fuse_event_mode = False

    if _return == "fixed":
        $ circuit_fixed = True
        $ unlock("electrician")
        $ add_route("Circuit ✓")
        scene bg mars_base with fade
        "The last fuse clicks into place and every light in the base comes back on."
        show miquel_halfbody_smiling at pos_center with dissolve
        M "Perfect! No damage to the rest of the circuit."
        hide miquel_halfbody_smiling with dissolve
    else:
        $ circuit_fixed = False
        $ res_energy -= 20
        $ samples_collected = max(0, samples_collected - 1)
        $ clamp_resources()
        $ add_route("Circuit ✗")
        scene bg mars_base with fade
        "A spark jumps from the panel and part of the circuit burns out."
        show nelson_halfbody_angry at pos_center with dissolve
        N "The lab freezer has been without power for hours. Some of the samples we collected have thawed: they're compromised."
        hide nelson_halfbody_angry with dissolve
        "{b}The base has lost 20 energy and one set of scientific samples.{/b}"

    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    scene black with fade
    "Another month goes by on the red planet..."

    jump month_4


## =============================================================
## MONTH 4 - Consequences of the short circuit
## =============================================================
label month_4:

    $ day = 91
    $ set_chapter(10)
    $ gained = produce_energy(10)
    $ crew_gets_hungry()
    $ month_passes()

    if circuit_fixed:
        $ result = [
            ("text", "Good news, Commander! The short circuit that was causing problems at the base has been repaired."),
            ("text", "All the electrical systems are working normally again and the fault did not affect the rest of the facilities. What a scare!"),
            ("text", "Thanks to your intervention, we can continue the mission without further worries."),
        ]
    else:
        $ result = [
            ("text", "Bad news, Commander. The short circuit could not be repaired and some systems of the base are still not working properly."),
            ("text", "The fault caused the loss of part of the stored energy, and electricity consumption must be reduced to keep the situation from getting worse."),
            ("text", "We will have to learn to work with fewer resources until the problem can be solved."),
        ]

    call screen day_title("MONTH 4", "Three months on Mars")

    scene bg control_room_crew with fade

    $ open_tablet([
        ("title", "REPORT - MONTH 4"),
        ("good", "You received +%d energy." % gained),
    ] + result + [
        ("head", "ENVIRONMENT (MONTHLY)"),
        ("bad", "Oxygen -10%%, temperature -10%%, radiation +%d%%." % res_radiation_rate),
        ("head", "THE CREW"),
        ("bad", "Everyone has lost 1 food bar and 1 water bar."),
        ("head", "EVENTS"),
        ("text", "There are no events for now."),
    ], cont="END THE MONTH ▶")

    call screen day_tablet

    $ check_crew_neglect()
    $ fail = survival_failure()
    if fail:
        jump expression "ending_" + fail

    $ current_month = 5
    jump month_cycle
