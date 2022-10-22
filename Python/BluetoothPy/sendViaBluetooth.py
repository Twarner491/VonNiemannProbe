#basic sending program to determine whether hc-06 can function well with python

import serial

ser = serial.Serial("COM4", 9600, timeout = 1) #Change your port name COM... and your baudrate

def retrieveData():
    ser.write(b'1')
    data = ser.readline().decode('ascii')
    return data

while(True):
    uInput = input("Retrieve data? ")
    if uInput == '1': #send 69 in bytes when input of 1 received 
        ser.write(b'69')
    else:
        ser.write(b'0') #send bad data if input not 1