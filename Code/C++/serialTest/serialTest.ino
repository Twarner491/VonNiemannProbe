//(c) Teddy Warner & Jack Hollingsworth - 2022

//This work may be reproduced, modified, distributed, performed, and displayed
//for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
//Copyright is retained and must be preserved. The work is provided as is;
//no warranty is provided, and users accept all liability.

//testing serial in new vscode environment, not sure why it's not working

#include <Arduino.h> //Arduino Parent Lib

void setup(){
    Serial.begin(9600);
    Serial.println("test");
}

void loop(){
    Serial.println("test");
    delay(5000);
}