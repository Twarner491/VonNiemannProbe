//(c) Teddy Warner & Jack Hollingsworth - 2022

//This work may be reproduced, modified, distributed, performed, and displayed
//for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
//Copyright is retained and must be preserved. The work is provided as is;
//no warranty is provided, and users accept all liability.

#include <Arduino.h> //Arduino Parent Lib
#include <SoftwareSerial.h> //software serial library, native in base installation of ide

SoftwareSerial HC06(0, 1); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

int buzzerPin = 2; //pin of buzzer/vibrating motor
String fullString = ""; // 
int dotLength = 200; //establish length of 1 dot

void setup() {
  HC06.begin(9600); //Baudrate 9600 , Choose your own baudrate 
  pinMode(buzzerPin, OUTPUT);
}

void loop(){

  if(HC06.available() > 0) //When HC06 receive something
  {
    char receive = HC06.read(); //Read from Serial Communication
    if(receive =='.'){
      digitalWrite(buzzerPin, HIGH);
      delay(dotLength); //delay for dotlength
      digitalWrite(buzzerPin, LOW);
      delay(dotLength); //dotlength delay between next character
    }
    if(receive =='9'){
      digitalWrite(buzzerPin, LOW);
      delay(dotLength * 2); //delay for another 2 seconds if space, gives 3 seconds total division between letters - make proportional to actual thing
    }
    else {
      digitalWrite(buzzerPin, LOW);
      delay(5);
    }
  }

}
