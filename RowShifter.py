def convertBlock(inBlock):
    tempBlock = []
    for i in range(0,len(inBlock),4):
        tempBlock.append(inBlock[i:i+4])
    return tempBlock

def shiftRows(block):
    outBlock = convertBlock(block)
    for i in range(0,len(outBlock)):
        outBlock[i] = outBlock[i][i:]+outBlock[i][:i]
    return outBlock

def shiftRowsInv(inBlock):
    #outBlock = convertBlock(inBlock)
    outBlock = inBlock
    for i in range(0, len(outBlock)):
        outBlock[i] = outBlock[i][-i:]+outBlock[i][:-i]
    return outBlock