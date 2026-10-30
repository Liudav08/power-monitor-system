"""Live plot and CSV logger. Run: python monitor.py COM5"""
import argparse
import csv
import math
from collections import deque
from datetime import datetime
import time
import serial
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('port', help='e.g. COM5 or /dev/ttyUSB0')
    args = parser.parse_args()
    filename = datetime.now().strftime('power_log_%Y%m%d_%H%M%S_%f.csv')
    history = [deque(maxlen=600) for _ in range(4)]
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(9, 7))
    lines = [ax.plot([], [])[0] for ax in axes]
    for ax, label in zip(axes, ['Load voltage (V)', 'Current (mA)', 'Power (mW)']):
        ax.set_ylabel(label)
        ax.grid(True)
    axes[-1].set_xlabel('Recorded time (s)')
    plt.tight_layout()
    plt.ion()
    plt.show()
    energy = elapsed = 0.0
    previous = None
    print(f'Saving {filename}. Close plot or press Ctrl+C to stop.')
    try:
        with serial.Serial(args.port, 115200, timeout=0.1) as port, open(filename, 'x', newline='') as file:
            time.sleep(2)  # Classic Nano commonly resets when serial opens.
            port.reset_input_buffer()
            writer = csv.writer(file)
            writer.writerow(['device_ms', 'recorded_s', 'load_V', 'current_A', 'power_W', 'energy_Wh'])
            while plt.fignum_exists(fig.number):
                raw = port.readline().decode('ascii', errors='replace').strip()
                if raw.startswith('#'):
                    print(raw)
                try:
                    fields = raw.split(',')
                    if len(fields) != 4:
                        raise ValueError
                    stamp = int(fields[0])
                    voltage, current, reported_power = map(float, fields[1:])
                    if not 0 <= stamp <= 0xFFFFFFFF or not all(map(math.isfinite, [voltage, current, reported_power])):
                        raise ValueError
                except ValueError:
                    plt.pause(0.01)
                    continue
                power = voltage * current
                if previous is not None:
                    old_stamp, old_power = previous
                    dt = ((stamp - old_stamp) & 0xFFFFFFFF) / 1000.0
                    if 0 < dt <= 1.0:
                        elapsed += dt
                        energy += (old_power + power) * 0.5 * dt / 3600.0
                    else:
                        print('Timestamp gap/reset: interval excluded from recorded time and energy.')
                previous = stamp, power
                writer.writerow([stamp, elapsed, voltage, current, power, energy])
                file.flush()
                for values, value in zip(history, [elapsed, voltage, current * 1000, power * 1000]):
                    values.append(value)
                for ax, line, values in zip(axes, lines, list(history)[1:]):
                    line.set_data(history[0], values)
                    ax.relim()
                    ax.autoscale_view()
                fig.suptitle(f'{voltage:.3f} V | {current*1000:.2f} mA | {power*1000:.2f} mW | {energy:.6f} Wh')
                fig.canvas.draw_idle()
                plt.pause(0.01)
    except KeyboardInterrupt:
        pass
    except serial.SerialException as error:
        print(f'Serial connection error: {error}')
    finally:
        plt.close('all')
    print(f'Log: {filename}; energy over recorded intervals: {energy:.6f} Wh')


if __name__ == '__main__':
    main()
