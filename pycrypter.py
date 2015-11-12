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

key = getKey("testKey")
block = getBlock("testBlock")

shiftedBlock = shiftRows(block)
unShiftedBlock = shiftRowsInv(shiftedBlock)
print("Original Block:  "),
print(block)
print("Shifted Block:   "),
print(shiftedBlock)         # Shifted and un-shifted will present the same values
print("Unshifted Block: "),
print(unShiftedBlock)       # as they are referenced to the same memory region
