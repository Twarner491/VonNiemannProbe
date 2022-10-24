//testing serial in new vscode environment, not sure why it's not working

void setup(){
    Serial.begin(9600);
    Serial.println("test");
}

void loop(){
    Serial.println("test");
    delay(5000);
}