
#include <Wire.h>

#include "Adafruit_LEDBackpack.h"
String incomingByte = "";
String readString;
String str = "";
String motor_one_value = "";
String motor_two_value = "";


void setup() {
  Serial.begin(9600);
  Serial.println("HangBot");
}

void loop() {
  // serial read section
  while (!Serial.available()) {} // wait for data to arrive

  while (Serial.available())                           
  {
    delay(50);  //delay to allow buffer to fill 
    // Serial is looking for a string like "111.11>22.222" (two values split by '>' character)
    motor_one_value = Serial.readStringUntil('>');
    motor_two_value = Serial.readStringUntil('\n');
    
    Serial.print("Arduino Received: ");
    Serial.println(motor_one_value);
    Serial.println(motor_two_value);
    
    //Serial.flush();
  }
}
