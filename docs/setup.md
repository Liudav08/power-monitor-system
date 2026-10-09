# Setup and wiring

Status: template. Hardware connections and run commands are not yet confirmed.

## Required equipment

| Item | Model / version | Purpose |
| --- | --- | --- |
| ESP32 board | To be confirmed | Measurement and communication |
| Measurement circuit / sensor | To be confirmed | Voltage and current sensing |
| Power supply | To be confirmed | Board power |
| Reference meter | To be confirmed | Measurement comparison |

## Exact wiring

Complete this table against the schematic before powering the circuit.

| Source component / pin | Destination component / pin | Signal / voltage | Notes |
| --- | --- | --- | --- |
| To be confirmed | To be confirmed | To be confirmed | To be confirmed |

Record ESP32 GPIO assignments, supply voltages, grounding, connector orientation, and isolation requirements here. Link the matching schematic in [hardware](../hardware/) and wiring diagram in [images](images/).

## Development environment

- Operating system: to be confirmed.
- ESP32 toolchain, board target, and versions: to be confirmed.
- Python version and dependencies: to be confirmed.
- Serial port, baud rate, and connection settings: to be confirmed.

## Build, flash, and run

1. Add the firmware to [firmware](../firmware/) and document its dependency installation and exact build command.
2. Document the board configuration, flash command, and serial monitor command.
3. Add the Python application to [software](../software/) and document environment setup and the exact run command.
4. Document the expected startup output and where measurements are saved in [data](../data/).

No executable firmware or software has been added yet.

## First measurement

Record pre-power checks, calibration steps, a known test load, expected readings, and troubleshooting steps. Follow the [testing procedure](testing.md) and record results before claiming measurement accuracy.
