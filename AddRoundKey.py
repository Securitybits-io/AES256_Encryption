def addRoundKey(inBlock, roundKey):
    outBlock = []
    for i in range(0,len(inBlock)):
        outBlock.append(inBlock[i]^roundKey[i])
    return outBlock