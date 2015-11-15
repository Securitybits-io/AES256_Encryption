def getBlock(filename):
    """
    Method to convert a file containing blockdata in byteform to integer array
    :param filename: input the filename containing string to convert to block
    :return: Integer array from blockfile
    """
    blockFile = open(filename, 'r')
    str = blockFile.read()
    tempArray = []
    for i in range(0, (len(str)),2):
        tempArray.append(int(str[i:i+2],16))
    blockArray = tempArray
    return blockArray

def getLargeBlock(filename):
    blockFile = open(filename, 'r')
    str = blockFile.read()
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
            if (len(tempArray) < 16):
                arr = [0]*16
                n = 0
                for item in tempArray:
                    arr[n] = tempArray[n]
                    n += 1
                blockArray.append(arr)

    return blockArray