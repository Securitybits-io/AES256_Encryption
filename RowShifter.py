def convertToMatrixBlock(inBlock):
    tempBlock = []
    for i in range(0,len(inBlock),4):
        tempBlock.append(inBlock[i:i+4])
    return tempBlock

def convertFromMatrixBlock(inBlock):
    tempList = []
    for row in inBlock:
        for i in range(0,len(row)):
            tempList.append(row[i])
    return tempList

def shiftRows(block):
    outBlock = convertToMatrixBlock(block)
    for i in range(0,len(outBlock)):
        outBlock[i] = outBlock[i][i:]+outBlock[i][:i]
    outBlock = convertFromMatrixBlock(outBlock)
    return outBlock

def shiftRowsInv(inBlock):
    outBlock = convertToMatrixBlock(inBlock)
    for i in range(0, len(outBlock)):
        outBlock[i] = outBlock[i][-i:]+outBlock[i][:-i]
    outBlock = convertFromMatrixBlock(outBlock)
    return outBlock