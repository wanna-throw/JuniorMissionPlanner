## 08_endings.rpy - Endings: six evacuation endings (a resource runs out) and the
## two mission results (good / bad).

image bg end:
    "images/end.jpeg"
    size (1920, 1080)

image bg mars_base_dark:
    "images/bg/bg_base_marte.png"
    size (1920, 1080)
    matrixcolor BrightnessMatrix(-0.45) * SaturationMatrix(0.5)

image bg mars_base_cold:
    "images/bg/bg_base_marte.png"
    size (1920, 1080)
    matrixcolor TintMatrix("#9cc3ff") * SaturationMatrix(0.4)

image bg mars_base_alarm:
    "images/bg/bg_base_marte.png"
    size (1920, 1080)
    matrixcolor TintMatrix("#ff9a9a")

screen the_end_screen(title, title_color, subtitle):
    modal True
    add "bg end"
    add Solid("#000000a0")
    $ summary = "Achievements: %d / %d   ·   Route: %s" % (achievements_count(), len(ACHIEVEMENTS), route_text())
    vbox:
        xalign 0.5
        yalign 0.42
        spacing 22
        text title size 100 bold True color title_color xalign 0.5 at warning_fade_in(0.0)
        text subtitle size 30 color "#e2e8f0" xalign 0.5 text_align 0.5 xsize 1400 at warning_fade_in(0.5)
        text summary size 20 color "#94a3b8" xalign 0.5 text_align 0.5 xsize 1400 at warning_fade_in(1.0)
    textbutton "BACK TO THE MAIN MENU":
        xalign 0.5
        yalign 0.88
        text_size 26
        text_bold True
        text_color "#38bdf8"
        text_hover_color "#ffffff"
        action Return()

label evacuation_finish(ending_id, title):
    $ ending_reached(ending_id)
    $ unlock("back_home")
    call screen the_end_screen(title, "#ef4444", "The crew evacuated the base and returned to Earth.")
    return


## =============================================================
## FOOD DEPLETION
## =============================================================
label ending_food:
    scene bg ship_kitchen with fade
    "{i}[[Warning alarm. The food inventory system displays an empty storage alert.]{/i}" with hpunch
    H "Commander! The food inventory system is reporting a critical shortage. We've run out of available food supplies!"
    T "What about the greenhouse? Can we increase production?"
    H "The hydroponic modules are still operational, but their current production isn't enough to meet the crew's nutritional requirements."
    T "We should be able to harvest the remaining crops."
    N "We can, but most of the plants aren't ready. Harvesting them now would provide very little food and compromise future production."
    M "What about the nutritional supplements?"
    N "We've already been using them to compensate for the reduced food supply. They aren't a complete replacement for a balanced diet."
    T "So how long can we continue?"
    N "Not long enough to complete the mission safely."
    c "After months of living on Mars, the crew's food reserves had finally been exhausted."
    c "The greenhouse was still operational, but its limited production capacity could not provide enough food to sustain the entire crew."
    c "The remaining crops were not ready to be harvested, and accelerating their growth was not a viable option."
    c "Despite reducing food consumption and carefully managing the remaining resources, the crew could no longer guarantee an adequate nutritional supply."
    c "The astronauts had underestimated how important it would be to balance their food reserves with the production capacity of their greenhouse."
    N "Commander, prolonged food shortages will seriously affect our health and our ability to function. We can't continue like this."
    T "Understood. Prepare for evacuation. Prioritize the remaining edible crops, nutritional supplements, medical supplies, scientific samples, and essential equipment."
    M "I'll secure the stored supplies and organize the cargo."
    H "I'll recover the greenhouse monitoring equipment and the essential communication systems."
    N "I'll inspect the remaining food and make sure everything is safe for consumption during the return journey."
    scene bg ship with fade
    c "With food production unable to sustain the crew, the mission could no longer continue."
    c "The astronauts began transferring their remaining provisions and essential equipment to the spacecraft."
    c "Any remaining edible crops, nutritional supplements, medical supplies, scientific samples, and valuable research equipment were carefully packed and secured."
    c "After completing the final inventory, the commander ordered the evacuation."
    c "The greenhouse was left behind, along with the base's ability to produce food."
    scene bg end with fade
    c "A long-duration mission cannot depend entirely on the supplies brought from Earth."
    c "Sustainable food production and careful planning are essential for survival."
    c "Without enough food to sustain the crew, their only option was to return home."
    call evacuation_finish("food", "OUT OF FOOD")
    return


## =============================================================
## WATER DEPLETION
## =============================================================
label ending_water:
    scene bg mars_base_alarm with fade
    "{i}[[Emergency alarm. A warning appears on the water management monitor.]{/i}" with hpunch
    H "Commander! We're receiving a critical alert from the water management system. Our available water reserves have reached zero!"
    T "What about the water recovery system? Can't we recover more from wastewater?"
    N "We've already maximized the recovery process. The ECLSS is recycling as much water as possible, but we're consuming more than we're recovering."
    M "What if we reduce water consumption even further?"
    N "We've already reduced it to the minimum required for survival. We simply don't have enough water left to sustain the crew."
    T "How long can we continue like this?"
    N "We can't guarantee the crew's survival if we remain here. We need a reliable water supply, and we no longer have one."
    c "After months of resource consumption, the base's available water reserves had finally been exhausted."
    c "Despite the use of the ECLSS water recovery system, the amount of water being recycled was no longer sufficient to meet the crew's daily requirements."
    c "The astronauts had already reduced their consumption to the minimum possible, but there was no way to compensate for the lack of available water."
    c "Water recycling had helped extend the mission, but it could not create new water or replace the need for carefully managed reserves."
    N "Commander, every drop matters. We've reached a point where we can no longer maintain the crew's basic needs."
    T "We've done everything we can. We can't risk staying here any longer."
    T "Everyone, prepare for evacuation. We need to transfer our remaining drinking water, food supplies, medical equipment, scientific samples, and essential tools to the spacecraft."
    M "I'll organize the cargo and secure the equipment."
    H "I'll recover the portable monitoring and communication systems."
    N "I'll check every remaining water container and organize the medical supplies for the journey."
    scene bg ship with fade
    c "With no sustainable water supply available, the base could no longer guarantee the crew's long-term survival."
    c "The astronauts began transferring their remaining supplies and essential equipment to the spacecraft."
    c "Every available container of water was carefully accounted for, along with food, medical supplies, scientific samples, and equipment needed for the return journey."
    c "After completing the final inventory, the commander ordered the evacuation."
    c "The base was abandoned."
    scene bg end with fade
    c "A long-duration mission cannot survive on initial reserves alone."
    c "Without careful consumption and efficient recycling, even the most advanced water recovery systems will eventually reach their limits."
    c "The crew had learned this lesson too late."
    c "Their only option was to return home."
    call evacuation_finish("water", "OUT OF WATER")
    return


## =============================================================
## TOTAL POWER FAILURE
## =============================================================
label ending_power:
    scene bg mars_base with fade
    "{i}[[Electrical systems shutting down. Warning alarms begin to sound. Lights flicker before the entire base falls into darkness.]{/i}"
    scene bg mars_base_dark with vpunch
    H "Commander! We're losing power across the entire base! Our energy reserves have reached zero!"
    T "What about the backup batteries? Can we restore the power supply?"
    H "They're completely depleted. The solar arrays aren't generating enough electricity to sustain the base, and there's no available energy left to keep the critical systems running."
    M "What about the emergency generator?"
    H "We've already used its remaining capacity. There's nothing left to restart the system."
    N "The life support systems are shutting down! Oxygen production, water recovery, atmospheric regulation and temperature control are no longer operational!"
    T "How long can we survive without these systems?"
    N "We can't guarantee the crew's survival if we remain here. We need to evacuate immediately."
    c "After months of operation, the base's available energy reserves had finally been exhausted."
    c "The crew had relied on its electrical generation and storage systems to power every essential part of the habitat."
    c "However, energy consumption had exceeded production for too long, leaving the batteries completely depleted."
    c "Without electricity, the base could no longer maintain its life support infrastructure."
    c "Oxygen production stopped, water recycling became unavailable, and the thermal regulation system could no longer maintain safe internal temperatures."
    c "Despite their attempts to recover the remaining energy systems, the crew could not restore the power supply."
    T "We've reached the limit. Without electricity, none of our critical systems can operate. We have to abandon the base."
    T "Everyone, prepare for immediate evacuation. We need to transfer our remaining resources, food supplies, emergency water, medical equipment, scientific samples, and essential tools to the spacecraft."
    M "I'll organize the cargo and secure the mechanical equipment."
    H "I'll disconnect and recover the portable communication, navigation, and monitoring systems."
    N "I'll organize the medical supplies and check our remaining oxygen and water reserves for the journey."
    scene bg ship with fade
    c "With no electricity available to sustain the habitat, the base had become uninhabitable."
    c "The astronauts began transferring their remaining supplies and essential equipment to the spacecraft."
    c "Food, water, medical supplies, emergency oxygen containers, scientific samples, and portable equipment were carefully secured."
    c "Every available resource was accounted for, as nothing could be wasted during the journey home."
    c "After completing the final inventory and shutting down the remaining systems, the commander ordered the evacuation."
    c "The base was abandoned."
    scene bg end with fade
    c "With their remaining resources secured, the astronauts began preparing for their return to Earth."
    c "Their mission on Mars was over."
    c "But the journey is far from over."
    call evacuation_finish("power", "TOTAL POWER FAILURE")
    return


## =============================================================
## THERMAL REGULATION FAILURE
## =============================================================
label ending_thermal:
    scene bg mars_base_cold with fade
    "{i}[[Warning alarm. The temperature control monitor displays a critical system warning.]{/i}" with hpunch
    H "Commander! The thermal regulation system has dropped below 20%% capacity!"
    T "What's happening? Are we losing internal temperature?"
    M "The system is struggling to maintain the habitat's temperature. Its remaining capacity is no longer enough to compensate for the heat we're losing to the Martian environment."
    N "If the temperature continues to drop, the crew will be exposed to increasingly dangerous conditions. We also need to protect our water supplies, food, and medical equipment from freezing."
    T "Can we reduce the temperature requirements or redirect more energy to the heating system?"
    M "We've already reduced the thermal load as much as possible. The system is operating at its limit, and we can't maintain safe conditions much longer."
    T "How much time do we have?"
    N "I can't give you an exact estimate, but we shouldn't wait until the habitat becomes too cold to work safely."
    c "After months of operation, the base's thermal regulation capacity had fallen below the minimum safe threshold."
    c "The system was no longer capable of maintaining stable temperatures throughout the habitat."
    c "As heat continued to escape into the extremely cold Martian environment, the internal temperature began to decrease."
    c "Despite reducing energy consumption in other areas and prioritizing the thermal regulation system, its remaining capacity was insufficient to maintain habitable conditions."
    c "The crew had reached a point where they could no longer guarantee their own safety."
    M "Commander, we've reached the limit of what this system can do. We can't maintain the temperature required to keep the habitat habitable."
    T "Understood. Everyone, prepare for evacuation. Prioritize thermal protective clothing, emergency heating equipment, medical supplies, food, water, scientific samples, and essential tools."
    H "I'll recover the portable monitoring systems and disconnect the remaining control units."
    M "I'll organize the mechanical equipment and secure the cargo compartments."
    N "I'll prepare the medical supplies and make sure everyone has adequate thermal protection for the journey."
    scene bg ship with fade
    c "With the thermal regulation system no longer capable of maintaining safe internal conditions, the base had become increasingly dangerous to inhabit."
    c "The astronauts began transferring their remaining supplies and essential equipment to the spacecraft."
    c "Thermal protective clothing, emergency heating equipment, medical supplies, food, water, and scientific samples were carefully secured."
    c "After completing the final inventory and shutting down the remaining systems, the commander ordered the evacuation."
    c "The habitat was abandoned, left exposed to the freezing Martian environment."
    scene bg end with fade
    c "Maintaining a habitable environment requires constant energy, monitoring, and careful resource management."
    c "On Mars, even the temperature inside your home is something you must fight to preserve."
    c "The crew had no choice but to return home."
    call evacuation_finish("thermal", "THERMAL FAILURE")
    return


## =============================================================
## OXYGEN DEPLETION
## =============================================================
label ending_oxygen:
    scene bg nelson_station with fade
    "{i}[[Emergency pressure alarm. A warning light flashes as the oxygen monitoring system detects critically low reserves.]{/i}" with hpunch
    H "Commander! The oxygen management system is reporting a critical alert. Our available oxygen reserves have reached zero!"
    T "What about our oxygen production systems?"
    H "MOXIE and the electrolysis unit are operational, but their combined production is no longer enough to meet the crew's consumption."
    N "We're consuming oxygen faster than we're producing it. Even with the atmospheric management systems operating, we can't maintain a safe oxygen balance."
    M "Can we reduce the consumption rate?"
    N "We've already minimized physical activity and reduced non-essential operations. There's nothing more we can do without putting the crew at risk."
    T "How long can we maintain a breathable atmosphere?"
    N "I can't guarantee that we can maintain safe conditions much longer. We need to evacuate before the atmospheric oxygen level becomes dangerous."
    c "After months of operation, the base's available oxygen reserves had finally been exhausted."
    c "Although the oxygen production systems were still functioning, their output was insufficient to compensate for the crew's daily consumption."
    c "The MOXIE unit, designed to extract oxygen from carbon dioxide in the Martian atmosphere, could not provide enough oxygen to sustain the entire crew."
    c "The backup electrolysis system was also unable to meet the growing demand."
    c "Despite reducing consumption and prioritizing life support operations, the oxygen balance could no longer be maintained."
    c "The astronauts had underestimated how important it would be to balance oxygen production, storage, and consumption throughout the mission."
    N "Commander, we can't stay here. Without a reliable oxygen supply, the habitat will soon become uninhabitable."
    T "Understood. Everyone, prepare for immediate evacuation. Secure the emergency oxygen supplies, portable breathing equipment, medical supplies, food, water, scientific samples, and essential tools."
    M "I'll organize the cargo and secure the remaining equipment."
    H "I'll recover the portable monitoring and communication systems. We need to verify the spacecraft's life support before departure."
    N "I'll calculate our oxygen requirements for the return journey and inspect all emergency supplies."
    scene bg ship with fade
    c "With oxygen production unable to sustain the crew, the base could no longer guarantee a breathable atmosphere."
    c "The astronauts began transferring their remaining resources and essential equipment to the spacecraft."
    c "Emergency oxygen supplies, portable breathing equipment, medical supplies, food, water, and scientific samples were carefully secured."
    c "The crew completed the final checks, ensuring that the spacecraft's life support systems could sustain them throughout the return journey."
    c "Once everyone was aboard and the cargo had been secured, the commander ordered the evacuation."
    c "The base was abandoned."
    scene bg end with fade
    c "Oxygen is not an unlimited resource. Its production, recovery, and storage must be carefully managed to keep the crew alive."
    c "Without a sustainable oxygen supply, there was no possibility of continuing the mission."
    c "The astronauts had only one objective left."
    c "Make it back to Earth alive."
    call evacuation_finish("oxygen", "OUT OF OXYGEN")
    return


## =============================================================
## EXTREME SOLAR RADIATION EVENT
## =============================================================
label ending_radiation:
    scene bg control_room_crew with fade
    "{i}[[Incoming transmission signal. The communication terminal activates.]{/i}"
    H "Commander! We're receiving an emergency transmission from Earth!"
    T "Put it through."
    scene bg control_mission with dissolve
    EMC "Mars Mission, this is Mission Control. We've detected an extreme solar particle event heading towards Mars. Current predictions indicate that radiation levels could reach dangerous values within the next few hours."
    T "Understood. What's our current exposure level?"
    H "Our radiation monitoring systems are reporting that the crew's accumulated exposure has already reached the critical threshold of 100%%."
    N "That's extremely dangerous. Additional exposure could significantly increase the health risks for everyone aboard."
    M "Can the habitat's shielding protect us from the incoming storm?"
    N "It can reduce exposure, but it cannot guarantee adequate protection during an event of this magnitude, especially considering how much radiation we've already accumulated."
    EMC "We strongly recommend immediate evacuation. The spacecraft must be prepared for departure before the solar particle event reaches its peak."
    T "Understood. We're initiating emergency evacuation procedures."
    scene bg mars_base_alarm with fade
    c "After months of exposure to the Martian environment, the crew's accumulated radiation indicator had finally reached its critical limit."
    c "Mars lacks a global magnetic field and has a much thinner atmosphere than Earth, leaving its surface considerably more exposed to energetic particles from space."
    c "The warning from Earth made the situation even more serious."
    c "An extreme solar particle event was approaching, and the crew could no longer afford additional exposure."
    c "Although the habitat included radiation shielding and a designated shelter, these measures could not guarantee sufficient protection under the current conditions."
    N "Commander, we must leave before the storm reaches its peak. Further exposure could put everyone's health at serious risk."
    T "Agreed. Everyone, prepare for immediate evacuation. Prioritize radiation monitoring equipment, medical supplies, protective equipment, food, water, scientific samples, and essential tools."
    H "I'll secure the radiation detectors, communication equipment, and navigation systems."
    M "I'll organize the cargo and secure the equipment that can be transported safely."
    N "I'll prepare the medical supplies and record everyone's accumulated radiation exposure for the return journey."
    scene bg ship with fade
    c "With the solar particle event approaching, the crew began transferring their remaining supplies and essential equipment to the spacecraft."
    c "Radiation monitoring devices, medical supplies, protective equipment, food, water, and scientific samples were carefully secured."
    c "The crew completed the final checks, ensuring that the spacecraft's radiation protection and life support systems were operational."
    c "After confirming that everyone was aboard, the commander ordered the final evacuation."
    c "The base was abandoned."
    scene bg end with fade
    c "The astronauts had reached the limit of what they could safely endure on Mars."
    c "Radiation exposure is an invisible threat that accumulates over time, making preparation and prevention essential throughout the entire mission."
    c "With the solar storm approaching, there was no time left to waste."
    c "Their only chance was to leave the planet."
    call evacuation_finish("radiation", "SOLAR STORM")
    return


## =============================================================
## MISSION RESULT: BAD
## =============================================================
label ending_bad:
    scene bg ship with fade
    c "After months of hardship and a long journey back home, our astronauts have finally returned to Earth."
    scene bg control_mission with fade
    c "Unfortunately, the mission could not be completed due to a series of complications. The samples they were supposed to find and collect during the expedition were compromised, leaving the team with no useful data for further research."
    c "However, even failure can teach us valuable lessons."
    c "As a result of this mission, future expeditions were far better prepared and equipped with significantly more infrastructure, laying the foundations for larger-scale exploration missions."
    scene bg end with fade
    c "And so, our story comes to an end."
    c "Thank you for playing."
    $ ending_reached("bad")
    $ unlock("lessons")
    call screen the_end_screen("MISSION INCOMPLETE", "#fbbf24", "The crew came back home, but without useful samples.")
    return


## =============================================================
## MISSION RESULT: GOOD
## =============================================================
label ending_good:
    scene bg end with fade
    c "MISSION SUCCESS!!!"
    scene bg ship with fade
    c "After months of travel, exploration, and countless challenges, our crew has finally returned home, bringing back the samples safely to Earth."
    scene bg control_mission with fade
    c "Following an extensive analysis conducted by the URA laboratories, the results revealed something extraordinary."
    c "Among the collected samples, scientists identified potential biosignatures: organic compounds, unusual mineral formations, and microscopic structures preserved within ancient Martian rocks."
    c "Further geological analysis revealed traces of minerals such as clay and sulfates, suggesting that these samples may have once been exposed to liquid water. Such environments could have provided the conditions necessary for microbial life to emerge and survive."
    c "After months of investigation and independent laboratory testing, the evidence was confirmed: Mars once harbored microbial life."
    scene bg press_conference with fade
    c "This discovery marks an unprecedented milestone in human history. For the first time, humanity has confirmed that life existed beyond Earth, fundamentally changing our understanding of biology, evolution, and our place in the universe."
    c "Our astronauts, and above all their captain, will forever be remembered as the first humans to bring back evidence of extraterrestrial life."
    c "Their courage, determination, and sacrifice have opened an entirely new chapter in the history of exploration."
    scene bg end with fade
    c "And so, our story comes to an end."
    c "But perhaps, somewhere among the stars, another story is just beginning."
    c "Thank you for playing."
    $ ending_reached("good")
    $ unlock("life_beyond")
    call screen the_end_screen("MISSION SUCCESS", "#4ade80", "The crew brought back the first evidence of life beyond Earth.")
    return
