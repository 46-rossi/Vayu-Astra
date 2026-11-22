
/*
  Vayu Astra - ESP32 Servo Command Validator

  Reference firmware for serial protocol testing.

  Expected command:
  P90,T90

  SAFETY:
  This version does not initialize a servo driver
  or send any PWM signals to motors.
*/

#include <Arduino.h>

constexpr unsigned long BAUD_RATE = 115200;

// Software validation limits only.
// Not verified mechanical servo limits.
constexpr int PAN_MIN = 75;
constexpr int PAN_MAX = 105;
constexpr int TILT_MIN = 80;
constexpr int TILT_MAX = 100;

String inputBuffer = "";

bool parseCommand(const String &command,
                  int &pan,
                  int &tilt) {
  int parsedPan = 0;
  int parsedTilt = 0;
  char extra = '\0';

  int fields = sscanf(
    command.c_str(),
    "P%d,T%d %c",
    &parsedPan,
    &parsedTilt,
    &extra
  );

  if (fields != 2) {
    return false;
  }

  if (parsedPan < PAN_MIN ||
      parsedPan > PAN_MAX ||
      parsedTilt < TILT_MIN ||
      parsedTilt > TILT_MAX) {
    return false;
  }

  pan = parsedPan;
  tilt = parsedTilt;

  return true;
}

void setup() {
  Serial.begin(BAUD_RATE);
  inputBuffer.reserve(64);

  Serial.println("VAYU ASTRA ESP32 READY");
  Serial.println("MODE: VALIDATION ONLY");
  Serial.println("SERVOS: DISABLED");
}

void loop() {
  while (Serial.available()) {
    char incoming = Serial.read();

    if (incoming == '\n') {
      inputBuffer.trim();

      int pan = 0;
      int tilt = 0;

      if (parseCommand(inputBuffer, pan, tilt)) {
        Serial.printf(
          "ACCEPTED P%d,T%d\n",
          pan,
          tilt
        );
      } else {
        Serial.println("REJECTED");
      }

      inputBuffer = "";

    } else if (incoming != '\r') {
      if (inputBuffer.length() < 63) {
        inputBuffer += incoming;
      } else {
        inputBuffer = "";
        Serial.println("ERROR: COMMAND TOO LONG");
      }
    }
  }
}
