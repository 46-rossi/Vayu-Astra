
# Vayu Astra — Software Architecture

## Overview

Vayu Astra is a working physical prototype
for AI-assisted camera tracking and
surveillance demonstrations.

The software architecture uses:

- Raspberry Pi for camera processing
- Python for application logic
- Picamera2 for camera capture
- OpenCV for image processing
- ESP32 for servo control
- Serial communication between devices
- Flask for browser-based video streaming

## Processing Architecture

```text
Raspberry Pi Camera Module 3
             |
             v
         Picamera2
             |
             v
      OpenCV Processing
             |
             v
      Target Detection
             |
             v
     Position Estimation
             |
             v
      Tracking Controller
             |
             v
      USB Serial Link
             |
             v
           ESP32
             |
             v
      PCA9685 Driver
             |
             v
       Pan/Tilt Servos
```

## Raspberry Pi Software

The Raspberry Pi application handles:

1. Capturing camera frames
2. Processing images using OpenCV
3. Estimating target position
4. Calculating tracking corrections
5. Sending commands to the ESP32
6. Serving a browser-based video feed

Previous development used a serial connection
such as /dev/ttyUSB1 at 115200 baud.

The actual serial port must be verified
on the connected Raspberry Pi.

## ESP32 Software

The ESP32 receives tracking commands
and controls the pan and tilt servos.

Previous prototype configuration included:

- PCA9685 I2C address: 0x40
- Pan servo channel: 0
- Tilt servo channel: 1
- I2C SDA: GPIO 21
- I2C SCL: GPIO 22
- Serial baud rate: 115200

Servo travel limits and PWM calibration
must be checked against the installed motors.

## Servo Safety

The tracking system should include:

- Restricted pan and tilt angles
- Command validation
- Smooth position transitions
- Dead-band filtering
- Safe startup positioning
- Protection against cable twisting

Do not operate servos with unverified
PWM limits or mechanical end stops.

## Thermal Sensor Integration

Status: PLANNED

The thermal sensor has not yet been
installed in the physical prototype.

Future software development may include:

- Thermal sensor communication
- Thermal frame acquisition
- RGB and thermal alignment
- Multi-sensor tracking experiments

These capabilities are not currently
claimed as operational.

## Current Repository Status

This document describes the prototype
software architecture.

Verified source files, configuration,
and hardware test results should be
added separately.

The architecture diagram is not proof
that every subsystem has passed
end-to-end validation.
```
