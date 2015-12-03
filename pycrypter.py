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
#!C:\python27\python.exe
from argparse import *
import os.path
from datetime import datetime
from readKeyFile import *
from readBlockFile import *
from AES256 import encrypt,decrypt


def encryptFile(filename, keyfile, outputFile):
    plainBlock = getLargeBlock(filename)
    encryptedBlock = []
    boolWritten = False
    for i in range(len(plainBlock)):
        encryptedBlock.append(encrypt(plainBlock[i], getKey(keyfile)))

    boolWritten = writeToOutputHex(encryptedBlock, outputFile)
    if boolWritten == True:
        return "Successfully encrypted: " + filename + " with key: " + keyfile + " into: "+ outputFile
    else:
        return "Something went wrong, please check settings"


def decryptFile(filename, keyfile, outputFile):
    inputBlock = getLargeHexBlock(filename)
    boolWritten = False
    for i in range(len(inputBlock)):
        inputBlock[i] = decrypt(inputBlock[i], getKey(keyfile))

    boolWritten = writeToOutputPlain(inputBlock, outputFile)
    if boolWritten == True:
        return "Successfully decrypted: " + filename + " with: " + keyfile + " into: "+ outputFile
    else:
        return "Something went wrong, please check settings"



def writeToOutputPlain(block, outputFilename):
    outputFile = open(outputFilename, "w")
    k = 0
    while k < len(block):
        for j in range(0,len(block[k])):
            outputFile.write(chr(block[k][j]))
        k+=1
    outputFile.close()
    return True


def writeToOutputHex(block, outputFilename):
    outputFile = open(outputFilename,"w")
    k = 0
    while k < len(block):
        for j in range(0,len(block[k])):
            outputFile.write(hex(block[k][j])[2:].zfill(2))
        k+=1
    outputFile.close()
    return True


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def Main():
    parser = ArgumentParser(description='''
    #################################################################
    #   Author: Christoffer Claesson | Git: Helix88                 #
    #   Project Name: pyCrypter                                     #
    #   Date of creation: 2015-11-12                                #
    #   School: Hogskolan Dalarna Borlange                          #
    #   Description: Project created for Course: Cryptology DT2017, #
    #               as a project of creating a python program,      #
    #               to encrypt text and files in AES-256            #
    #   Liscence: GNU Open Source                                   #
    #################################################################''', formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('operation', metavar="operation", type=str, help="Either input (Encrypt/Decrypt) or (E/D)")
    parser.add_argument('filename', metavar="filename", type=lambda x: is_valid_file(parser, x), help="Filename for file to be encrypted ex: blockfile.txt")
    parser.add_argument('keyfile', metavar="keyfile", type=lambda x: is_valid_file(parser, x), help="Keyfile with 32 byte key ex: keyfile.txt")
    parser.add_argument('-o', '--output', metavar="filename", type=str, help="Output filename for encrypted or decrypted file default: output.txt")
    args = parser.parse_args()

    blockFile = args.filename
    keyFile = args.keyfile
    operation = str(args.operation).lower()
    status = ""

    if not args.output:
        output = "output.txt"
    else:
        output = args.output
    startTime = datetime.now()
    if operation == "encrypt" or operation == "e":
        status = encryptFile(blockFile, keyFile, output)
    elif operation == "decrypt" or operation == "d":
        status = decryptFile(blockFile, keyFile, output)
    executionTime = datetime.now() - startTime

    print status + "\nExecution time: " + str(executionTime)





























if __name__ == '__main__':
    Main()

'''
startTime = datetime.now()
key = getKey("testKey")

largeBlock = getLargeBlock("testtWotW.txt")
encryptedLargeBlock = []
decryptedLargeBlock = []
string = ""

print "\nencrypted done:"
for i in range(0,len(largeBlock)):
    encryptedLargeBlock.append(encrypt(largeBlock[i], key))
    #print(encryptedLargeBlock[i])

print "\ndecrypted done:"
for i in range(0,len(encryptedLargeBlock)):
    decryptedLargeBlock.append(decrypt(encryptedLargeBlock[i],key))
    #print(decryptedLargeBlock[i])

print "\nplain:"
for i in range(0,len(decryptedLargeBlock)):
    for j in range(0,16):
        string += chr(decryptedLargeBlock[i][j])

print string

print "Execution time: " + str(datetime.now() - startTime)
'''