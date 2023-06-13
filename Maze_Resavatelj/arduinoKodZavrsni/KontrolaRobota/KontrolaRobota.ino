#include <AccelStepper.h>
#include <SoftwareSerial.h>


//stepper initialization
#define Ldir 4
#define Lstep 5

#define Rdir 6
#define Rstep 7

#define motorInterfaceType 1

AccelStepper lStepper(motorInterfaceType, Ldir , Lstep);
AccelStepper rStepper(motorInterfaceType, Rdir, Rstep);

//bluetooth communication

SoftwareSerial serial_connection(2,3);
#define BUFFER_SIZE 64
char inData[BUFFER_SIZE];
char inChar=-1;
int count =0;
int i=0;

void setup() {
  // left stepper - initialization
  lStepper.setMaxSpeed(2000);
  lStepper.setAcceleration(1000);
  lStepper.setSpeed(2000);

  //right stepper - initialization
  rStepper.setMaxSpeed(2000);
  rStepper.setAcceleration(1000);
  rStepper.setSpeed(2000);

  Serial.begin(9600);

  //serial_communication - initialization
  serial_connection.begin(9600);
  serial_connection.println("ready");
}


String rotate(char direction){
  //counter clockwise
  if (direction=='L'){
    lStepper.move(-400);
    rStepper.move(400);
  }
  //clockwise
  else if (direction=='R'){
    lStepper.move(400);
    rStepper.move(-400);
  }
  lStepper.run();
  rStepper.run();
  return "finished";
 }

 //move forward
 String forward(int distance){
  lStepper.move(distance);
  rStepper.move(distance);
  lStepper.run();
  rStepper.run();
  return "finished";
 }

 
void loop() {
  // put your main code here, to run repeatedly:
  byte byte_count=serial_connection.available();
  if(byte_count){
    for(i=0;i<byte_count;i++){
      inChaar=serial_connection.read();
      inData[i]=inChar;
    }
    inData[i]='\0';
  }
  if(inData[0]=='L' || inData[0]=='R'){
    serial_connection.println(rotate(inData));
  }
  else if (inData[0]=='F'){
    //treba sloziti kaj sparsira F__ naredbu tak kaj zeme broja nakon slova F npr. F123 -> broj:123
  }
  delay(1000);
}
