//(c) Teddy Warner & Jack Hollingsworth - 2022

//This work may be reproduced, modified, distributed, performed, and displayed
//for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
//Copyright is retained and must be preserved. The work is provided as is;
//no warranty is provided, and users accept all liability.

//basic function for receiving from bluetooth

#include <Arduino.h> //Arduino Parent Lib
#include <SoftwareSerial.h> //software serial library, native in base installation of ide

SoftwareSerial HC06(10, 11); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

int buzzerPin = 8; //pin of buzzer/vibrator
int ledPin = 13;
String fullString = ""; // 
int dotLength = 1000; //establish length of 1 dot
int dashLength = 3 * dotLength; //establish proportion of dots to dashes

void setup() {
  HC06.begin(9600); //Baudrate 9600 , Choose your own baudrate 
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
}

void loop(){

  if(HC06.available() > 0) //When HC06 receive something
  {
    char receive = HC06.read(); //Read from Serial Communication
    if(receive =='.'){
      digitalWrite(buzzerPin, HIGH);
      digitalWrite(ledPin, HIGH);
      delay(dotLength); //delay for dotlength
      digitalWrite(buzzerPin, LOW);
      digitalWrite(ledPin, LOW);
      delay(dotLength); //dotlength delay between next character
    }
    if(receive == '-')
    {
    digitalWrite(buzzerPin, HIGH);
    digitalWrite(ledPin, HIGH);
    delay(dashLength);
    digitalWrite(buzzerPin, LOW);
    digitalWrite(ledPin, LOW);
    delay(dotLength); //dot length delay between next character
    }
    if(receive =='9'){
      digitalWrite(buzzerPin, LOW);
      digitalWrite(ledPin, LOW);
      delay(dotLength * 2); //delay for another 2 seconds if space, gives 3 seconds total division between letters - make proportional to actual thing
    }
    else {
      digitalWrite(buzzerPin, LOW);
      digitalWrite(ledPin, LOW);
      delay(5);
    }
  }

}
