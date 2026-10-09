# Design

Status: template. Component selections, calculations, and PCB design are pending.

## Requirements

| Requirement | Target | Rationale |
| --- | --- | --- |
| Voltage range | To be confirmed | To be confirmed |
| Current range | To be confirmed | To be confirmed |
| AC / DC measurement | To be confirmed | To be confirmed |
| Accuracy | To be confirmed | To be confirmed |
| Sampling and reporting rate | To be confirmed | To be confirmed |
| Communication interface | To be confirmed | To be confirmed |

## System architecture

Describe the measurement path, ESP32 processing, communication, and Python data collection. Add an architecture diagram to [images](images/).

## Component choices

| Component | Part number / value | Reason for selection | Datasheet |
| --- | --- | --- | --- |
| ESP32 board | To be confirmed | To be confirmed | To be added |
| Sensor / measurement circuit | To be confirmed | To be confirmed | To be added |

## Calculations

For each calculation, include the equation, input values with units, assumptions, result, and design margin.

- Input scaling and ADC range.
- Sensor sensitivity and calibration conversion.
- Resolution and expected measurement uncertainty.
- Sampling rate and filtering.
- Power calculation appropriate to the selected AC or DC method.
- Supply budget, component ratings, and thermal limits.

## PCB decisions

Record board dimensions, layer count, connectors, placement, routing, grounding, protection, and any isolation constraints. Link the editable [KiCad files](../hardware/) and exported PCB renders in [images](images/).

## Design decisions

| Date | Decision | Alternatives considered | Reason / evidence |
| --- | --- | --- | --- |
| To be added | To be added | To be added | To be added |

## Known limitations

Document unsupported operating conditions and unresolved design risks. Link measurement evidence from [testing](testing.md).
