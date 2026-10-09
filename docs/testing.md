# Testing

Status: planned procedures. No measurement tests have been completed or reported.

## Test configuration

Record the hardware revision, firmware revision, software revision, supply, load, reference instrument and its accuracy, calibration, environment, and date for each test.

## Procedures

### Wiring and startup

1. Check the assembled circuit against the wiring table and schematic.
2. Verify supplies and signal levels against the selected component ratings.
3. Record startup behavior, communication, and data logging results.

### Measurement comparison

1. Define test points across the intended measurement range.
2. Measure each point with the power monitor and a reference instrument under the same conditions.
3. Capture repeated readings and the measurement interval.
4. Save the unmodified readings in [data](../data/).
5. Calculate signed error as monitor reading minus reference reading; calculate percentage error as 100 times signed error divided by reference reading. Percentage error is undefined at a zero reference reading.
6. Compare results with the accuracy targets in [design](design.md).

### Calibration and repeatability

Document the calibration method and coefficients. Use separate measurements for validation, repeat test points, and record drift or noise.

### Operating limits

Once the design limits are established, test only within those limits. Record behavior for supported load changes, connection loss, restart, and extended operation.

## Results

| Date | Test / condition | Reference reading | Monitor reading | Error | Pass / fail | Raw data |
| --- | --- | --- | --- | --- | --- | --- |
| Pending | Pending | Pending | Pending | Pending | Not evaluated | Pending |

Acceptance criteria must be defined before assigning pass / fail results.

## Limitations

Record reference instrument uncertainty, sample count, tested range, timing differences, untested conditions, and any assumptions that limit the conclusions.
