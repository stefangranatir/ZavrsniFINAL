#include <SoftwareSerial.h>

SoftwareSerial serial_con(3,2);
#define BUFFER_SIZE 64
char inData[BUFFER_SIZE];
char inChar=-1;
int count=0;
int i=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  serial_con.begin(9600);
  serial_con.print("spremno");
  Serial.println("spremno");
}

void loop() {
  // put your main code here, to run repeatedly:
  byte byte_count=serial_con.available();
  if(byte_count){
    for(i=0;i<byte_count;i++){
      inChar=serial_con.read();
      inData[i]=inChar;
    }
    inData[i]='\0';
  }
  Serial.println(inData);

}
