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


def convertToKarlBlock(block):
    tempArray = block
    blockArray = []
    for row in range(0,4):
        for column in range(0,len(tempArray),4):
            blockArray.append(tempArray[column+row])
    return blockArray


def convertFromKarlBlockInv(block):
    tempArray = block
    blockArray = []
    for row in range(0,4):
        for column in range(0,len(tempArray),4):
            blockArray.append(tempArray[column+row])
    return blockArray