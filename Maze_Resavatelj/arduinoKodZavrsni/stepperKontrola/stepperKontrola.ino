// Define pin connections & motor's steps per revolution
// Include the AccelStepper Library
#include <AccelStepper.h>

// Define pin connections
const int dirPin = 4;
const int stepPin = 5;

const int dirPin2 = 6;
const int stepPin2 = 7;

// Define motor interface type
#define motorInterfaceType 1

// Creates an instance
AccelStepper myStepper(motorInterfaceType, stepPin, dirPin);
AccelStepper myStepperDesni(motorInterfaceType, stepPin2, dirPin2);

void setup() {
    
  // set the maximum speed, acceleration factor,
  // initial speed and the target position
  myStepper.setMaxSpeed(1000);
  myStepper.setAcceleration(50);
  myStepper.setSpeed(250);
  myStepper.moveTo(800);

  myStepperDesni.setMaxSpeed(1000);
  myStepperDesni.setAcceleration(50);
  myStepperDesni.setSpeed(250);
  myStepperDesni.moveTo(800);

}

void loop() {
  // Change direction once the motor reaches target position
  if (myStepper.distanceToGo() == 0) 
    myStepper.moveTo(-myStepper.currentPosition());

  // Move the motor one step
  
  if (myStepperDesni.distanceToGo() == 0) 
    myStepperDesni.moveTo(-myStepperDesni.currentPosition());

  // Move the motor one step
  myStepper.run();
  //delay(10);
  myStepperDesni.run();
}
