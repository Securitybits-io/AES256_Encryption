def getBlock(filename):
    """
    Method to convert a file containing blockdata in byteform to integer array
    :param filename: input the filename containing string to convert to block
    :return: Integer array from blockfile
    """
    blockFile = open(filename, 'r')
    str = blockFile.read()
    intArray = []
    for i in range(0, (len(str)),2):
        intArray.append(int(str[i:i+2],16))
    return intArray