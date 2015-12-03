def getLargeHexBlock(filename):
    """
    Method to convert an encrypted file containing blockdata in Hex to integer array
    :param filename: input the filename containing string to convert to block
    :return: Integer array from blockfile
    """
    hexFile = open(filename, 'r')
    hexStr = hexFile.read()
    tempArray = []
    blockArray =[]

    for i in range(0,len(hexStr), 2):
        tempArray.append(int(hexStr[i:i+2],16))

    for j in range(0,len(tempArray), 16):
        blockArray.append(tempArray[j:j+16])
    return blockArray


def getLargeBlock(filename):
    '''
    Method for reading a file to be encrypted
    :param filename: Input of the filename to be encrypted
    :return: Integer Nested Array list with 16Byte blocks
    '''
    blockFile = open(filename, 'r')
    str = blockFile.read().encode("hex")
    tempArray = []
    blockArray = []

    for i in range(0,len(str),2):
        tempArray.append(int(str[i:i+2],16))

    if (len(tempArray)<16):
        arr = [0]*16
        n = 0
        for item in tempArray:
            arr[n] = tempArray[n]
            n += 1
        blockArray.append(arr)
    else:
        while(len(tempArray)>=16):
            blockArray.append(tempArray[0:16])
            tempArray = tempArray[16:]
            print "Reading file \r",
            if (len(tempArray) < 16 and len(tempArray) > 0):
                arr = [0]*16
                n = 0
                for item in tempArray:
                    arr[n] = tempArray[n]
                    n += 1
                blockArray.append(arr)

    return blockArray