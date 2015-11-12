def shiftRows(block):
    inBlock = block
    outBlock = []
    for i in range(0,len(inBlock),4):
        outBlock.append(inBlock[i:i+4])

    print(outBlock)
    for i in range(0,len(outBlock)):
        outBlock[i] = outBlock[i][i:]+outBlock[i][:i]
    return outBlock