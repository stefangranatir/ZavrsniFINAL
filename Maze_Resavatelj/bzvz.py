import serial
import time
import threading

ser=serial.Serial("COM5",9600)
ser.reset_input_buffer()

while True:
    i=input()
    ser.write(bytes(str(i),"utf-8"))
    time.sleep(0.5)