from SubBytes import subBytes
from rcon import getRcon


def keyScheduleCore(inputWord, i):
    oWord = subBytes(inputWord[1:]+inputWord[:1])
    oWord[0] = oWord[0] ^ getRcon(i)
    return oWord


def expandKey(inputKey):
    cipherKeySize = len(inputKey)
    assert cipherKeySize == 32
    outputKey = []  #Container for expanded key
    currentSize = 0
    rconIteration = 1
    temp = [0]*4    #Temporary byte list to store 4 bytes at a time

    for i in range(cipherKeySize):
        outputKey.append(inputKey[i])
    currentSize += cipherKeySize

    while currentSize < 240:
        for i in range(4):
            temp[i] = outputKey[(currentSize -4)+i]

        if currentSize % cipherKeySize == 0:
            temp = keyScheduleCore(temp, rconIteration)
            rconIteration += 1

        if currentSize % cipherKeySize == 16:
            temp = subBytes(temp)

        for i in range(4):
            outputKey.append(((outputKey[currentSize-cipherKeySize]) ^ (temp[i])))
            currentSize +=1

    return outputKey


def createRoundKey(expandedKey, roundNumber):
    return expandedKey[(roundNumber * 16):(roundNumber*16+16)]