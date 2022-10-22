//basic function for receiving from bluetooth

#include <SoftwareSerial.h>
SoftwareSerial HC06(10, 11); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

int buzzerPin = 13; //pin of buzzer/vibrator
String fullString = ""; // 
int dotLength = 1000; //establish length of 1 dot
int dashLength = 3 * dotLength; //establish proportion of dots to dashes

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
  }

}