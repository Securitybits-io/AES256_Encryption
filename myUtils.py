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