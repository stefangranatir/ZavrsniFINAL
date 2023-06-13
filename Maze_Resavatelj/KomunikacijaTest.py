import serial
import time
import threading


def communication(path):
    ser = serial.Serial("COM5",9600)
    #ser.open()
    ser.reset_input_buffer()

    received=""

    '''while True:
        
        i=input()
        ser.write(bytes(str(i), 'utf_8'))
        time.sleep(0.5)
        input_data=""
        while(input_data==""):
            input_data = ser.readline()
            print(input_data.decode())
            input_data=""'''

    for p in range(len(path)):
        ser.write(bytes(str(path[p]),'utf_8'))
        time.sleep(0.5)
        input_data=""
        while(input_data==""):
            input_data=ser.readline()
            print(input_data.decode())



    ser.close()