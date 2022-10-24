//(c) Teddy Warner & Jack Hollingsworth - 2022

//This work may be reproduced, modified, distributed, performed, and displayed
//for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
//Copyright is retained and must be preserved. The work is provided as is;
//no warranty is provided, and users accept all liability.

//only for learning a-h and 1-8 of morse

#include <Arduino.h> //Arduino Parent Lib

int outputPin = 13; //pin of whatever output does morse
int index;
String letters = "abcdefgh";
String numbers = "12345678";
String randomString = ""; //placeholder string to be filled with morse
String morseString = ""; //placeholder for morse converted string


void setup(){
    pinMode(outputPin, OUTPUT);
    Serial.begin(9600); //initizalize serial at 9600 baud
    Serial.print("morse code practice");
}

void loop(){
    randomString = "";
    index = random(0, 7); //takes random value between indexes 0 and 7 of numbers and letters strings
    randomString += letters.substring(index, index); //take one char from letters string add to random string
    index = random(0,7);
    randomString += numbers.substring(index, index);
    index = random(0,7);
    randomString += letters.substring(index,index);
    index = random(0,7);
    randomString += letters.substring(index, index);





}

char receive = HC06.read(); //Read from Serial Communication
    if(receive =='.'){
      digitalWrite(buzzerPin, HIGH);
      delay(dotLength); //delay for dotlength
      digitalWrite(buzzerPin, LOW);
      delay(dotLength); //dotlength delay between next character
    }
    if(receive == '-')
    {
    digitalWrite(buzzerPin, HIGH);
    delay(dashLength);
    digitalWrite(buzzerPin, LOW);
    delay(dotLength); //dot length delay between next character
    }
    if(receive =='9'){
      digitalWrite(buzzerPin, LOW);
      delay(2000); //delay for another 2 seconds if space, gives 3 seconds total division between letters
    }
    else {
      delay(5);
    }