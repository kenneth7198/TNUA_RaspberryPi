import processing.net.*;

Client c;
String input;
int data[];

void setup() 
{
  size(450, 255);
  background(204);
  c = new Client(this, "192.168.3.4", 1688); 
}

void draw() 
{
  if (c.available() > 0) {
    input = c.readString();
    println(input);
  } 
}