#################################################################
#   Author: Christoffer Claesson | Git: Helix88                 #
#   Project Name: pyCrypter                                     #
#   Date of creation: 2015-11-12                                #
#   School: Hogskolan Dalarna Borlange                          #
#   Description: Project created for Course: Cryptology DT2017, #
#               as a project of creating a python program,      #
#               to encrypt text and files in AES-256            #
#   Liscence: GNU Open Source                                   #
#################################################################
#!/usr/bin/python

from readKeyFile import *
from readBlockFile import *
from RowShifter import *
from ColumnMixer import mixColumns, mixInvColumns
from SubBytes import subBytes,subBytesInv
from keyManager import expandKey,createRoundKey
from AddRoundKey import addRoundKey
from myUtils import *
from AES256 import encrypt,decrypt

key = getKey("testKey")
block = getBlock("testBlock")
karlBlock = convertToKarlBlock(block)

shiftedBlock = shiftRows(block)
unShiftedBlock = shiftRowsInv(shiftedBlock)

mixBlock = mixColumns(block)
unMixedBlock = mixInvColumns(mixBlock)

varSubBytes = subBytes(block)
varSubInvBytes = subBytesInv(varSubBytes)

expandedKey = expandKey(key)
roundKey0 = createRoundKey(expandedKey,0)

addedRoundKeyToBlock = addRoundKey(block, roundKey0)

encryptedBlock = encrypt(block,key)
decryptedBlock = decrypt(encryptedBlock, key)
print("Key:             "),
print key

print "\n"+"#"*91
print("Original Block:  "),
print(block)
print("Karl Block:      "),
print(karlBlock)
print("Karl Block Inv:  "),
print convertFromKarlBlockInv(karlBlock)
print ("-"*91)
print("Shifted Block:   "),
print(shiftedBlock)
print("Unshifted Block: "),
print(unShiftedBlock)
print ("-"*91)
print("Mixed Block:     "),
print(mixBlock)
print("UnMixed Block:   "),
print(unMixedBlock)
print ("-"*91)
print("SubBytes:        "),
print(varSubBytes)
print("SubBytes Inverse:"),
print(varSubInvBytes)
print("-"*91)
print("Expanded Key:    "),
print expandedKey
print("Round 0 Key:     "),
print roundKey0
print("-"*91)
print("Added RoundKey:  "),
print(addedRoundKeyToBlock)
print ("-"*91)
print("Encrypted block: "),
print(encryptedBlock)
print("Decrypted block: "),
print(decryptedBlock)
print "#"*91