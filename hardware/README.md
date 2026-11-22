
# Vayu Astra — Hardware

## Overview

Vayu Astra is a working physical prototype
for AI-assisted visual object tracking and
surveillance demonstrations.

The hardware architecture combines a
Raspberry Pi for vision processing with
an ESP32 for servo control.

## Prototype Components

| Component | Purpose |
|---|---|
| Raspberry Pi | Vision processing |
| Raspberry Pi Camera Module 3 | Camera input |
| ESP32 | Servo control |
| Pan servo | Horizontal camera movement |
| Tilt servo | Vertical camera movement |
| Pan-tilt bracket | Camera mounting |
| PCA9685 servo driver | PWM servo control |
| Power distribution system | Component power |
| Mounting platform | Prototype assembly |

## Additional Components

The evolving prototype design also includes
a laser pointer, buzzer, and power switch.

Their final wiring and operational status
must be verified against the physical build.

## Planned Upgrade

### Thermal Sensor

Status: PLANNED — NOT YET INSTALLED

The next hardware upgrade is a thermal
sensor mounted near the camera tracking
assembly.

Planned objectives:

- Capture thermal observations
- Explore low-light detection capabilities
- Investigate thermal and RGB data fusion
- Evaluate sensor alignment

No thermal detection performance is claimed
until integration and testing are completed.

## Safety and Validation

Before operating the prototype:

- Verify power supply voltages
- Check servo travel limits
- Prevent cable twisting
- Confirm camera mounting stability
- Test the emergency power switch
- Avoid directing the laser toward people,
  vehicles, or aircraft

## Development Status

The physical prototype is operational.

This document describes the hardware
architecture and planned upgrades.
It does not claim that every proposed
surveillance capability has been validated.
