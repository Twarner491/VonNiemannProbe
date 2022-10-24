#(c) Teddy Warner & Jack Hollingsworth - 2022

#This work may be reproduced, modified, distributed, performed, and displayed
#for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
#Copyright is retained and must be preserved. The work is provided as is;
#no warranty is provided, and users accept all liability.

import serial
from time import sleep

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM4'
ser
ser.open()
openBool = ser.is_open
print("Serial Open: " + str(openBool))

testString = "encoding test"
testStringBytes = str.encode(testString)
print(type(testStringBytes))
testStringDecoded = testStringBytes.decode()
print(type(testStringDecoded))

    