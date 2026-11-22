
# Vayu Astra — Prototype Development Status

## Project Overview

Vayu Astra is an AI-assisted surveillance
and object-tracking prototype developed
for defence technology demonstrations
and hackathon evaluations.

The project explores camera-based target
tracking using embedded computing,
computer vision, and servo control.

## Current Development Stage

Status: Working physical prototype,
with ongoing integration and testing.

The prototype has undergone multiple
design and software iterations.

## Implemented Prototype Architecture

### Vision Processing

- Raspberry Pi computing platform
- Raspberry Pi Camera Module 3
- Python-based application architecture
- Picamera2 camera interface
- OpenCV image processing
- Browser-based video streaming

### Embedded Control

- ESP32 microcontroller
- PCA9685 PWM servo driver
- MG996R pan and tilt servos
- Serial communication architecture

### Mechanical Design

- Pan/tilt camera mounting assembly
- Prototype mounting platform
- Power distribution arrangement
- Iterative 3D prototype designs

## Software Verification Status

The repository contains reference code
for camera preview and ESP32 serial
command validation.

These uploaded reference files are
not yet documented as independently
tested, end-to-end tracking software.

The current ESP32 reference firmware
does not command servo movement.

## Latest 3D Design

Version: V14

Interactive model:

https://46-rossi.github.io/Vayu-Astra/3d-models/V14.html

The 3D design represents the evolving
prototype layout.

## Planned Hardware Upgrade

### Thermal Sensor

Status: Planned — Not Yet Installed

The V14 model includes a proposed
thermal sensor mounting position
outside the camera U-bracket.

Future development includes:

- Physical thermal sensor installation
- Thermal data acquisition
- RGB and thermal alignment
- Sensor fusion experiments
- Low-light detection evaluation

No thermal detection results are
claimed at this stage.

## Testing and Validation

Further documented validation is needed
for:

- Camera tracking accuracy
- Pan/tilt movement limits
- Servo power stability
- Tracking latency
- Target detection performance
- Continuous operating reliability

Test results should be published only
after measurements have been collected.

## Development Roadmap

1. Preserve existing prototype versions.
2. Organize hardware and software files.
3. Verify camera and ESP32 integration.
4. Validate restricted servo movement.
5. Document physical prototype tests.
6. Integrate and evaluate thermal sensing.
7. Publish measured performance results.

## Project Transparency

Vayu Astra is an evolving engineering
prototype, not a certified or deployed
counter-drone defence system.

Proposed capabilities and future
upgrades are distinguished from
implemented and tested functionality.
