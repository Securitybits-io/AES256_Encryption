def getKey(filename):
    '''
    Input filename containing bytestring of hexadecimal values to convert into a Integer Array
    :param filename: name of file containing bytestring
    :return: Integer Array
    '''
    keyFile = open(filename, 'r')
    str = keyFile.read()
    intArray = []
    for i in range(0, (len(str)),2):
        intArray.append(int(str[i:i+2],16))
    return intArray