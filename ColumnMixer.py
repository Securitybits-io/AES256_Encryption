from myUtils import convertToMatrixBlock,convertFromMatrixBlock
from mixColTables import getTable,getVector
from copy import copy

def mixColumn(column):
    tempCol = copy(column)
    outColumn = []

    for i in range(0,len(tempCol)):
        xorCol = []
        for j in range(0,4):
            value = column[j]
            table = getVector(i,j)
            xorCol.append(getTable(value,table))

        outColumn.append(xorCol[0] ^ xorCol[1] ^ xorCol[2] ^ xorCol[3])
    return outColumn

def mixColumns(block):
    inBlock = convertToMatrixBlock(block)
    mixBlock = []
    for i in range(0,len(inBlock)):
        mixBlock.append(mixColumn(inBlock[i]))
    return convertFromMatrixBlock(mixBlock)