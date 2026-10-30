# Setup and wiring

Status: template. Hardware connections and run commands are not yet confirmed.

## Required equipment

| Item | Model / version | Purpose |
| --- | --- | --- |
| ESP32 board | ESP32 CP2102 | Measurement and communication |
| Measurement circuit / sensor | Generic INA219 (B219) breakout, R100 shunt, 25 x 22mm | Voltage and current sensing |
| Power supply | SPS30101N (SPS3010) | Board power |
| Reference meter | Fluke-87 | Measurement comparison |

## Exact wiring

Complete this table against the schematic before powering the circuit.

| Source component / pin | Destination component / pin | Signal / voltage | Notes |
| --- | --- | --- | --- |
| GPIO22 | SCL | signal |  |
| GPIO21 | SDA | signal |  |
| 3V3 ESP32 | 3V3 INA219 | voltage | positive power |
| GND ESP32 | GND INA219 | voltage | GND reference |
| DC positive | INA219 Vin- | voltage |  |
| Vin+ | Load positive | voltage |  |
| Load negative | DC negative | voltage |  |
| Load negative | ESP32 GND | voltage | reference |

![Full Scheamtic](/docs/images/breadboard1.jpg)

## Development environment

- Operating system: Windows 11 version 26H2
- ESP32 toolchain, board target, and versions: Arduino 2.3.10
- Python version and dependencies: Python 3.14
- Serial port, baud rate, and connection settings: baud rate 115200
