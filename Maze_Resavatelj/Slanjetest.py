import serial
import time
import threading

ser=serial.Serial("COM4", 38400, timeout=1)



while True:
    salji=input("posalji:")
    ser.write(bytes((salji), 'utf_8'))
    time.sleep(1)
    if ser.in_waiting>0:
        received_data=ser.read(ser.in_waiting)
        print(f"Received data:{received_data}")

ser.close()