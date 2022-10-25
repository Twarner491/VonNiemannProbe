#(c) Teddy Warner & Jack Hollingsworth - 2022

#This work may be reproduced, modified, distributed, performed, and displayed
#for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
#Copyright is retained and must be preserved. The work is provided as is;
#no warranty is provided, and users accept all liability.

#basic sending program to determine whether hc-06 can function well with

import serial; import re

ser = serial.Serial("COM4", 9600, timeout = 1) #Change your port name COM... and your baudrate

while(True):
    uInput = input("Retrieve data? ")
    uInput = re.sub("[ ]", "9", uInput) #replace spaces with something that will never appear in a chess move, 9 in this case
    #print(uInput) #print input with spaces replaced with 9
    for char in uInput:
        tempChar = char.encode() #creative tempChar string that carries encoded char
        ser.write(tempChar) #send encdoed char via bluetooth
    '''if uInput == '1': #send 69 in bytes when input of 1 received 
        ser.write(b'6')
    elif uInput == '0':
        ser.write(b'0') #send bad data if input not 1
    else:
        ser.write('''