
# Vayu Astra — Serial Communication Protocol

## Overview

Vayu Astra uses USB serial communication
between the Raspberry Pi and ESP32.

The Raspberry Pi processes camera data.
The ESP32 receives pan and tilt commands.

This document describes the reference
protocol currently implemented by the
ESP32 command validator.

## Communication Settings

| Parameter | Value |
|---|---|
| Interface | USB serial |
| Baud rate | 115200 |
| Raspberry Pi | Python / pyserial |
| ESP32 | Arduino firmware |
| Command encoding | ASCII |
| Command terminator | Newline |

## Command Format

P<pan>,T<tilt>

Example:

P90,T90

The command must end with a newline.

## Current Validation Limits

| Axis | Minimum | Maximum |
|---|---|---|
| Pan | 75 | 105 |
| Tilt | 80 | 100 |

These are software validation limits only.
They are not verified mechanical limits.

## ESP32 Responses

Valid command:

ACCEPTED P90,T90

Invalid or out-of-range command:

REJECTED

Oversized command:

ERROR: COMMAND TOO LONG

## Python Serial Example

```python
import serial

port = serial.Serial(
    "/dev/ttyUSB1",
    115200,
    timeout=1
)

command = "P90,T90\n"
port.write(command.encode("ascii"))

response = port.readline().decode(
    "ascii",
    errors="replace"
).strip()

print(response)

port.close()
```

The serial device path must be checked
on the Raspberry Pi before running.

## Important Safety Note

The current ESP32 reference firmware
only validates commands.

It does not move the MG996R servos.

An ACCEPTED response means the command
passed software validation, not that
the servos reached the requested angles.

## Planned Integration

1. Verify serial communication.
2. Calibrate MG996R servos independently.
3. Add safe servo control.
4. Connect OpenCV tracking output.
5. Test tracking with restricted motion.

## Thermal Sensor

Status: Planned.

Thermal sensor data is not included
in the current serial protocol.
