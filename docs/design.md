# Design

Status: PCB V2.0 pending; V1.2 finsihed and functional; accuracy and precision to be tested. 

## Requirements

| Requirement | Target | Rationale |
| --- | --- | --- |
| Voltage range | 0 -20V | suitable voltage testing range for most smaller electronic components and parts; within the maximum load of the power supply (30V) so suitable for testing |
| Current range | 0 - 2A | Within the limit of most smaller electornic components and parts; within maximum of power supply (10A); lower operating limit to reduce risk of overheating and frying the INA219 |
| AC / DC measurement | DC measurement | DC measurement only for now: may integrate AC measurement in the future. |
| Accuracy | To be confirmed | To be confirmed |
| Sampling and reporting rate | To be confirmed | To be confirmed |
| Communication interface | I2C | what is available with the INA219 module; may change in later versions when the sensor module is replaced by a chip. |

## System architecture

Describe the measurement path, ESP32 processing, communication, and Python data collection. Add an architecture diagram to [images](images/).

## Component choices

| Component | Part number / value | Reason for selection | Datasheet |
| --- | --- | --- | --- |
| ESP32 board | ESP32 CP2102 | readily avilable development board with sufficient RAM and memory for firmware; faster than available arduino modules | [ESP32 Datasheet](/docs/datasheets/cp2102_datasheet.pdf) |
| Sensor / measurement circuit | generic INA219 (B219), R100 shunt, 22 x 25mm | readily available curernt and voltage sensor; suitable for early testing and prototype iterations | [INA219 datahseet](/docs/datasheets/ina219.pdf) |
| Input fuse | SIBA 179021.2.5 | most suitable based on current and voltage testing and desired limits; fast acting fuse | [SIBA datasheet](/docs/datasheets/SIBA-G-Miniature-Fuse-179021-Datasheet.pdf)

## Known limitations

Unresolved INA219 testing limits.
