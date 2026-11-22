
# Vayu Astra — MG996R Servo Setup

## Hardware

- Raspberry Pi
- ESP32
- PCA9685 PWM servo driver
- MG996R pan servo
- MG996R tilt servo
- External regulated 5–6V servo supply

## PCA9685 to ESP32

| PCA9685 | ESP32 |
|---|---|
| VCC | 3.3V |
| GND | GND |
| SDA | GPIO 21 |
| SCL | GPIO 22 |

VCC powers the PCA9685 logic, not the servos.

## Servo Connections

| Component | Connection |
|---|---|
| Pan servo signal | PCA9685 channel 0 |
| Tilt servo signal | PCA9685 channel 1 |
| Servo power | External regulated 5–6V |
| Servo ground | External supply ground |
| PCA9685 V+ | External servo supply positive |
| PCA9685 GND | Common ground with ESP32 |

Use a supply rated for the combined servo
current, including startup and stall loads.

Never power both MG996R servos directly
from the ESP32.

## Movement Safety

- Do not assume 90 degrees is mechanically safe.
- Verify each servo without an attached linkage.
- Calibrate PWM limits for each servo.
- Keep cables clear of moving parts.
- Use small movements during initial tests.
- Add software travel limits.
- Stop testing if a servo stalls or overheats.
- Provide a way to disconnect servo power.

## Current Firmware

software/esp32/servo_controller.ino

Status: Serial command validation only.

The current reference firmware does not
produce servo PWM signals.

## Next Development Stage

1. Verify electrical connections.
2. Calibrate one servo at a time.
3. Establish safe physical travel limits.
4. Implement restricted PCA9685 control.
5. Integrate Raspberry Pi tracking commands.

## Thermal Sensor

Status: Planned, not physically integrated.
