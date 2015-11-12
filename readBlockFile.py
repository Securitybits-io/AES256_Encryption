def getBlock(filename):
    blockFile = open(filename, 'r')
    str = blockFile.read()
    intArray = []
    for i in range(0, (len(str)),2):
        intArray.append(int(str[i:i+2],16))
    return intArray