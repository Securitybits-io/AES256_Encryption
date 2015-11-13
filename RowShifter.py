from myUtils import convertToMatrixBlock,convertFromMatrixBlock


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