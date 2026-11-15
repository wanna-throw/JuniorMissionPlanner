# MISSION CONTROL – Aphrodite 3

**A science-fiction survival visual novel set on Mars, made with Ren'Py.**

The year is 2052. You are the commander of **Aphrodite 3**, a mission of the fictional *United Robotics Association (URA)*. Your goal: keep your crew alive on Mars for **10 months** (300 days), manage the base's resources and bring back scientific samples that could prove there was once life on Mars.

The game mixes a **visual novel** (dialogues, characters and decisions) with a **resource-management system inspired by *60 Seconds!***.

🎬 **Gameplay demo:** [`MissionControl_gameplay_demo.mp4`](MissionControl_gameplay_demo.mp4) (20 seconds)

---

## How to play

1. **Choose the landing site** on the interactive Mars map: Mawrth Vallis, Holden, Eberswalde or Gale (real candidate sites of NASA's Mars Science Laboratory). Each site starts with different resources.
2. **Talk to your crew.** Each crew member explains one of the base's systems and the indicator appears in the top bar.
3. **Manage the tablet** every day, week or month:
   - **Report** – what happened and how the resources changed.
   - **Crew** – food and water bars of each crew member. Scroll down to give rations, produce food in the greenhouse or heat the base.
   - **Events** – emergencies (sandstorm, short circuit…).
4. **Make decisions:** who leads each expedition (Nelson, Hanna or Miquel). The whole crew always goes out together.
5. **Solve the minigames:** the fuse panel (Day 1 and the Month 3 short circuit) and the solar panel alignment (Day 4).
6. **Survive until Month 10** and return to Earth with the samples.

### Survival indicators (0–100)

| Indicator | How it works |
|---|---|
| ⚡ Energy | Produced every night/week/month. Spent on producing food and heating. Reduced by 25 % if the solar panel is not fixed. |
| 💧 Water | ECLSS recycling gives +15 every period. Rations cost 5. Expeditions can find ice. |
| 🍎 Food | The greenhouse gives +15 every period. Rations cost 5. +20 food for 10 water + 10 energy. |
| O₂ Oxygen | Drops 10 % every month from Month 2 (MOXIE + electrolysis). |
| 🌡️ Temperature | Thermal stability. Drops 10 % every month. Below 20 % the base is uninhabitable. |
| ☀️ Radiation | Accumulates every month depending on the site. At 100 % the crew must leave. |
| 📡 Antenna | Link with Earth: OK or DAMAGED. |

If a crew member ends a day with an **empty food or water bar**, or a resource reaches its limit, the crew **evacuates and returns to Earth**.

### Endings (8)

- **6 evacuation endings:** out of food, out of water, total power failure, thermal failure, out of oxygen and extreme solar radiation.
- **Mission incomplete** (bad result): back home without useful samples.
- **Mission success** (best ending): the first evidence of life beyond Earth.

### Progress, route and achievements

A badge in the top-left corner always shows the **story progress (%)**, the current **chapter**, the **route** you are following (landing site › expedition leaders › solar panel › short circuit) and your **achievements (16)**. Achievements are saved across playthroughs and can be viewed from the main menu.

---

## The crew

| Character | Profession | Role in the base |
|---|---|---|
| **Miquel** | Pilot & mechanical engineer | Energy, rover, base maintenance |
| **Hanna** | Robotics & telecommunications | Radiation, antenna, drones and robotic probes |
| **Nelson** | Medical officer & chemist | Oxygen, temperature, chemical analysis of samples |
| **Commander (you)** | Geologist & biologist | Decisions and scientific direction |

---

## Science behind the game

The life-support systems are inspired by real NASA technology:

- **MOXIE** – oxygen from the CO₂ of the Martian atmosphere (Perseverance rover).
- **Water electrolysis and ECLSS** – the life-support and water-recovery systems of the International Space Station (≈98 % water recovery).
- **Fission Surface Power / Kilopower** – nuclear power for planetary surfaces.
- **Solar arrays and batteries** – used by Mars missions such as InSight and the Mars Exploration Rovers.
- **Subsurface ice** – mapped by the SWIM project.

Sources: [MOXIE](https://science.nasa.gov/mission/mars-2020-perseverance/moxie/) · [ECLSS](https://www.nasa.gov/reference/environmental-control-and-life-support-system-eclss/) · [Water recovery milestone](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/) · [Fission Surface Power](https://www.nasa.gov/exploration-systems-development-mission-directorate/fission-surface-power/) · [Kilopower](https://www.nasa.gov/centers-and-facilities/glenn/kilopower-project/) · [SWIM](https://swim.psi.edu/) · [MSL landing sites](https://marsoweb.nas.nasa.gov/landingsites/landingsites.html)

---

## Repository structure

```
JuniorMissionPlanner/
├── README.md                          ← this file
├── MissionControl_gameplay_demo.mp4   ← 20-second gameplay demo
└── mission control/                   ← the Ren'Py project (open it with the Ren'Py launcher)
    └── game/
        ├── script.rpy                 ← entry point (label start)
        ├── options.rpy                ← game name, version, About text
        ├── gui.rpy / screens.rpy      ← Ren'Py interface (menus, Help, Achievements button)
        ├── scripts/
        │   ├── 01_definitions.rpy         characters, backgrounds, sprites, transforms
        │   ├── 02_mission_intro.rpy       press conference and mission control
        │   ├── 02_mapa_interactivo.rpy    interactive Mars map and starting resources per site
        │   ├── 03_asentamiento.rpy        Day 1: wake-up, kitchen tablet, settlement, crew reports
        │   ├── 04_minijuego_fusibles.rpy  fuse panel minigame (tutorial + short-circuit mode)
        │   ├── 05_days.rpy                Days 2–4 and end of week 1
        │   ├── 06_minijuego_panel_solar.rpy  solar panel minigame (Day 4)
        │   ├── 07_weeks_months.rpy        Weeks 2–4 and Months 2–4 (expeditions, short circuit)
        │   ├── 08_endings.rpy             the 8 endings
        │   └── 09_months_5_10.rpy         Months 5–10 and final evaluation
        ├── screens/
        │   ├── resource_hud.rpy           survival indicators (top bar, info window)
        │   ├── day_tablet.rpy             daily tablet (Report / Crew / Events)
        │   ├── tripulation_screen.rpy     crew selection in the command room
        │   ├── expedition_choice.rpy      "who leads the expedition?" screen
        │   ├── progress_system.rpy        progress %, route and achievements
        │   └── warning_screen.rpy         fiction disclaimer at startup
        ├── images/                    ← backgrounds (bg/), characters/, ui/ icons, minigames, end screen
        └── gui/                       ← Ren'Py interface images (main menu background)
```

---

## How to run it

1. Download the **Ren'Py SDK 8.5** from [renpy.org](https://www.renpy.org/).
2. Open the Ren'Py launcher, set the projects directory to this repository and select **mission control**.
3. Press **Launch Project**. To create a Windows/Mac/Linux version use **Build Distributions**.

---

*This game is a work of fiction. The United Robotics Association (URA) is a fictional organization and the game is not affiliated with any space agency.*

**Team:** Junior Mission Planner · Made with Ren'Py 8.5
