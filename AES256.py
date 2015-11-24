from keyManager import expandKey,createRoundKey
from AddRoundKey import addRoundKey
from SubBytes import subBytes
from RowShifter import shiftRows
from ColumnMixer import mixColumns
from myUtils import convertToKarlBlock

def encrypt(inBlock, key):
        outBlock = inBlock

        #Initialize
        expandedKey = expandKey(key)

        #First Round
        outBlock = addRoundKey(outBlock,createRoundKey(expandedKey,0))

        #Round 1->13
        for n in range(1,14):
            outBlock = subBytes(outBlock)
            outBlock = shiftRows(outBlock)
            outBlock = mixColumns(outBlock)
            outBlock = addRoundKey(outBlock,createRoundKey(expandedKey,n))

        #Round 14
        outBlock = subBytes(outBlock)
        outBlock = shiftRows(outBlock)
        outBlock = addRoundKey(outBlock,createRoundKey(expandedKey,14)) #Add roundKey

        return outBlock


def test():
    str = "6353e08c0960e104cd70b751bacad0e7"
    tempTest = []
    for i in range(0, (len(str)),2):
           tempTest.append(int(str[i:i+2],16))
    print tempTest

test()