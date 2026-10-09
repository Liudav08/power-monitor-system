# ESP32 Power Monitor System

A personal electronics project using an ESP32 and an INA219 sensor module to measure a DC load's voltage, current, and power, with a Python application for receiving measurements on a computer.

**Status:** Breadboard prototype working. The first PCB iteration is finished and a second iteration is being designed to replace the the microcontroller with ICs and the sensor module with a chip. 

## Why I built this

I wanted to design a measurement system that can connect embedded hardware to a computer while also working on my skills in sensor interfacing, firmware, python, and PCB design. 

A multimeter provides useful reference measurements, but this process focuses on automating the data colleciton. Its measurement accuracy still needs to be determined though through testing. 

## Project structure

| Path | Contents |
| --- | --- |
| [docs/setup.md](docs/setup.md) | Exact wiring and instructions for running the code |
| [docs/design.md](docs/design.md) | Component choices, calculations, and PCB decisions |
| [docs/testing.md](docs/testing.md) | Test procedures, measurement comparisons, and limitations |
| [docs/build-log.md](docs/build-log.md) | Dated progress, problems, and fixes |
| [docs/images/](docs/images/) | Photos, diagrams, and PCB renders |
| [hardware/](hardware/) | Editable KiCad files |
| [firmware/](firmware/) | ESP32 code |
| [software/](software/) | Python code |
| [data/](data/) | Raw measurements |

## Project status

| Stage | Status |
| --- | --- |
| ESP32 and INA219 breadboard prototype | Working |
| Python serial reception | TODO: record current implementation status |
| Live plotting and CSV logging | planned |
| Measurement comparison with a multimeter | TODO: record completed tests |
| KiCad carrier PCB using existing modules | Completed |
| Later PCB with an INA219 IC and a custom microcontroller circuit | In development |

Start with [setup](docs/setup.md), record design choices in [design](docs/design.md), and track progress in the [build log](docs/build-log.md).
