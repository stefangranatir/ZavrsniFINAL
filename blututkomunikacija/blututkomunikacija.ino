#include <SoftwareSerial.h>
#include <AccelStepper.h>


SoftwareSerial serial_connection(2, 3);
#define BUFFER_SIZE 64
char inData[BUFFER_SIZE];
char inChar=-1;
int count=0;
int i=0;
String inputS;


//steppers
#define lDir 4
#define lStep 5

#define rDir 6
#define rStep 7

#define motorInterfacetype 1

AccelStepper lStepper(motorInterfacetype, lStep, lDir);
AccelStepper rStepper(motorInterfacetype, rStep, rDir);


int turnSteps=450;
void setup()
{
  Serial.begin(9600);
  serial_connection.begin(9600);
  Serial.println("Started");


  lStepper.setMaxSpeed(2000);
  lStepper.setAcceleration(2000);
  lStepper.setSpeed(2000);

  rStepper.setMaxSpeed(2000);
  rStepper.setAcceleration(2000);
  rStepper.setSpeed(2000);
}

/*void runStep(){
  lStepper.move(400);
  while(lStepper.distanceToGo()!=0){
    lStepper.run();
  }
}*/

void loop()
{
  byte byte_count=serial_connection.available();
  if(byte_count)
  {
    Serial.println("Incoming Data");
    int first_bytes=byte_count;
    int remaining_bytes=0;
    if(first_bytes>=BUFFER_SIZE-1)
    {
      remaining_bytes=byte_count-(BUFFER_SIZE-1);
    }
    for(i=0;i<first_bytes;i++)
    {
      inChar=serial_connection.read();
      inData[i]=inChar;
    }
    inData[i]='\0';

    inputS=String(inData);
    
    Serial.println(inputS);
    if(inputS=="l" ||inputS=="r"){
      serial_connection.println(rotate(inData[0]));
    }
    else if(inData[0]=='f'){
      serial_connection.println(moveForward(returnNumber(inputS)+200));
    }

  }
  delay(500);
}
int returnNumber(String command){
  int indexF=command.indexOf('f');
  String number=command.substring(indexF+1, command.length());
  return number.toInt();
}
String moveForward(int distance){
  lStepper.move(distance);
  rStepper.move(distance);
  while((lStepper.distanceToGo() != 0 || lStepper.distanceToGo() != 0)&&(rStepper.distanceToGo() != 0 || rStepper.distanceToGo() != 0)){
    lStepper.run();
    rStepper.run();
  }
  return "done";
}
String rotate(char dir){
  if(dir=='r'){
    lStepper.move(turnSteps);
    rStepper.move(-turnSteps);
  }
  else if(dir=='l'){
    lStepper.move(-turnSteps);
    rStepper.move(turnSteps);
  }
  while((lStepper.distanceToGo() != 0 || lStepper.distanceToGo() != 0)&&(rStepper.distanceToGo() != 0 || rStepper.distanceToGo() != 0)){
    lStepper.run();
    rStepper.run();
  }
  return "finished";
}