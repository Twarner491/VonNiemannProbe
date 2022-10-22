//basic receiving code to turn on led when "passcode" received from a parallel python program running locally

#include <SoftwareSerial.h>
SoftwareSerial HC06(10, 11); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

int LED = 13; //Use whatever pins you want 
String fullString = ""; //built as bytes come

void setup() {
  HC06.begin(9600); //Baudrate 9600 , Choose your own baudrate 
  pinMode(LED, OUTPUT);
}

void loop(){

  if(HC06.available() > 0) //When HC06 receive something
  {
    char receive = HC06.read(); //Read from Serial Communication
    if(receive == '6') //If received data is 1, turn on the LED and send back the sensor data
    {
      digitalWrite(13, HIGH); 
      delay(5000);
      digitalWrite(13, LOW)
    }
    else digitalWrite(13, LOW);//If received other data, turn off LED
  }

}