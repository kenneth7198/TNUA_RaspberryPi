int inputAnalogData=0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  inputAnalogData = analogRead(A0);  
  Serial.println(inputAnalogData,DEC);
    delay(50);
  
}
