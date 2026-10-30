// Classic ESP32-WROOM development board, INA219 with 0.1 ohm shunt.
// USB-powered ESP32. INA219 VCC=3V3, GND=GND, SDA=21, SCL=22.
// Initial test: 5V supply, 30mA current limit, 330 ohm load.
#include <Wire.h>
#include <Adafruit_INA219.h>
#include <math.h>

constexpr int SDA_PIN = 21;
constexpr int SCL_PIN = 22;
constexpr uint8_t ADDRESS = 0x40;
Adafruit_INA219 ina219(ADDRESS);
uint32_t lastSample = 0;

bool readBusStatus(uint16_t &value) {
  Wire.beginTransmission(ADDRESS);
  Wire.write(uint8_t(0x02));
  if (Wire.endTransmission(false) != 0) return false;
  if (Wire.requestFrom(ADDRESS, uint8_t(2)) != 2) return false;
  value = (uint16_t(Wire.read()) << 8) | uint16_t(Wire.read());
  return true;
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  Wire.begin(SDA_PIN, SCL_PIN);
  Wire.setClock(100000);
  if (!ina219.begin(&Wire)) {
    while (true) {
      Serial.println("# INA219 not found: check 3V3/GND/SDA/SCL/address; reset after fixing");
      delay(1000);
    }
  }
  // Library calibration assumes a 0.1 ohm shunt.
  // '32V' names an ADC range; chip inputs MUST remain below 26V.
  // This project target is <=12V, <=1A on suitable wiring, not breadboard rails.
  ina219.setCalibration_32V_2A();
  if (!ina219.success()) {
    while (true) {
      Serial.println("# INA219 configuration failed; reset after checking wiring");
      delay(1000);
    }
  }
  delay(10);
  Serial.println("time_ms,load_V,current_A,power_W");
}

void loop() {
  if (uint32_t(millis() - lastSample) < 100) return;
  lastSample = millis();
  float voltage = ina219.getBusVoltage_V();
  bool valid = ina219.success();
  float current = ina219.getCurrent_mA() / 1000.0f;
  valid = ina219.success() && valid;
  uint16_t status = 0;
  valid = readBusStatus(status) && valid;
  if (!valid || !isfinite(voltage) || !isfinite(current)) {
    Serial.println("# I2C read failed: sample omitted");
    return;
  }
  if (status & 1) {
    Serial.println("# INA219 math overflow: switch off supply and check load");
    return;
  }
  // Diagnostic only: firmware cannot disconnect or protect the load.
  if (voltage > 20.0f || fabsf(current) > 1.05f) {
    Serial.println("# Project range exceeded: switch off supply");
    return;
  }
  Serial.print(lastSample); Serial.print(',');
  Serial.print(voltage, 4); Serial.print(',');
  Serial.print(current, 6); Serial.print(',');
  Serial.println(voltage * current, 6);
}
