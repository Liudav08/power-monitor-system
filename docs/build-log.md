# Build log

## 2026-07-26 to 2026-10-09 - Project Start

- Soldered and tested INA219 sensor
- designed prototype on breadboard
- coded firmware code
- coded python code
- deisgned KiCAD schematic and PCB layout for V1.0
- manufactured V1.0 and soldered all components on
- tested data analysis on laptop: still in development
- started Schematic of V2.0

## 2026-10-09 - Repository structure

- Added documentation templates for setup, design, testing, and this build log.
- Added folders for images, editable hardware files, firmware, Python software, and raw measurements.
- Hardware implementation, executable code, and measurement testing remain pending.

### 20206-10-09 - First documentation session

- Progress: breadboard prototype working, PCB iteration 1.0 fabricated, python code in development, v1.2 in development
- obsevations: minor problems faced in first part of design process; problems mostly pertained to wiring and pin assignment errors, and initial errors in the firmware. Voltage and current range not yet tested. 
![Breadboard Prototype](/docs/images//breadboard1.jpg)
![KiCAD Schematic](/docs/images/V1.0%20schematic.png)
- Next steps: test voltage and current range of data, work on schematic for V1.2, finish connecting embedded hardware to computer using python. 

### 2026-10-29 - Project and Documnetation Update

- Progress: Voltage and current range tested; input fuse working, V1.2 working, V2.0 in development, python code for V1.2 in development. 
- Issues: Prototype V1.0 had too many external wire connections; fixed this by soldering components directly on the main board and removing a screw terminal from the project. Fuse selection done via iterative testing using breadboard prototype to determine proepr fuse rating. Decided on 2.5A fast acting fuse. 
![KiCAD Schematic V1.2](/docs/images/V1.2%20schematic.png)
![KiCAD PCB Layout V1.2](/docs/images/V1.2%20pcb%20layout.png)
- Next steps: Work on schematic for V2.0 which will replace microcontroller with IC; develop new logic and firmware. 