#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd (0x27, 16, 2);
#define sensor A2
#define wet 0
#define dry 1023
 
void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
}
 
void loop() {
  int value = analogRead(sensor);
  Serial.println(value);
  lcd.setCursor(1, 0);
  lcd.print("Moisture Value");
  lcd.setCursor(3, 1);
  lcd.print(value);
  lcd.print(" ");
  lcd.setCursor(7,1);
  lcd.print("--");
  int pre = map(value, wet, dry, 100, 0);
  int pre = 
  lcd.setCursor(10, 1);
  lcd.print(pre);
  lcd.print("%");
  lcd.print(" ");
}
