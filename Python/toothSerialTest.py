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

    