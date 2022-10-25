//testing serial in new vscode environment, not sure why it's not working

void setup(){
    Serial.begin(9600);
    Serial.println("test");
}

void loop(){
    digitalWrite(3, HIGH);
    delay(1000);
    digitalWrite(3, LOW);
    delay(1000);
}