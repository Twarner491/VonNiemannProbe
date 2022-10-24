testString = "encoding test"
testStringBytes = str.encode(testString)
print("Encoded String Type: " + str(type(testStringBytes)))
testStringDecoded = testStringBytes.decode()
testByteArray = bytearray(testStringBytes)
print(testByteArray)
print(memoryview(b'encoding test').tolist())

    