#(c) Teddy Warner & Jack Hollingsworth - 2022

#This work may be reproduced, modified, distributed, performed, and displayed
#for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
#Copyright is retained and must be preserved. The work is provided as is;
#no warranty is provided, and users accept all liability.

testString = "encoding test"
testStringBytes = str.encode(testString)
print("Encoded String Type: " + str(type(testStringBytes)))
testStringDecoded = testStringBytes.decode()
testByteArray = bytearray(testStringBytes)
print(testByteArray)
print(memoryview(b'encoding test').tolist())

    