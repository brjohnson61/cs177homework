# CS177 -- padding oracle attacks This code is (unfortunately) meant
# to be run with Python 2.7.10 on the CSIL cluster
# machines. Unfortunately, cryptography libraries are not available
# for Python3 at present, it would seem.
from Crypto.Cipher import AES
import binascii
import sys

def check_enc(text):
    nl = len(text)
    val = int(binascii.hexlify(text[-1]), 16)
    if val == 0 or val > 16:
        return False

    for i in range(1,val+1):
        if (int(binascii.hexlify(text[nl-i]), 16) != val):
            return False
    return True
                                 
def PadOracle(ciphertext):
    if len(ciphertext) % 16 != 0:
        return False
    
    tkey = 'Sixteen byte key'

    ivd = ciphertext[:AES.block_size]
    dc = AES.new(tkey, AES.MODE_CBC, ivd)
    ptext = dc.decrypt(ciphertext[AES.block_size:])

    return check_enc(ptext)


##### MY FUNCTIONS #####
def organizeIntoBlocksOfBytes(text):
    blockList = []
    i=0
    while(i < len(text)):
        block = []
        j=0
        while(j < 32):
            k = j+2
            block.append(text[i+j:i+k])
            j=k
        blockList.append(block)
        i = i+32
    return blockList


# Padding-oracle attack comes here

if len(sys.argv) > 1:
    myfile = open(sys.argv[1], "r")
    ctext=myfile.read()
    myfile.close()


# complete from here. The ciphertext is now (hopefull) stored in
# ctext as a string. Individual symbols can be accessed as
# ord(ctext[i]). Some more hints will be given on the Piazza
# page.

    asciiText = binascii.b2a_hex(ctext)
    blockArray = organizeIntoBlocksOfBytes(asciiText)
    blockArray1 = blockArray
    numBlocks = len(blockArray)
    blockSize = len(blockArray[0])

    #for j in range(numBlocks-1):
        #for k in range(blockSize):
    newBlock = ""
    for i in range(len(blockArray1)):
        newBlock += "".join(blockArray1[i])

    for i in range(255):
        oldByte = int(blockArray[numBlocks-2][blockSize-1],16)
        tryByte = int(blockArray[numBlocks-2][blockSize-1],16) ^ 1 ^ i
        if(i < 16):
            blockArray1[numBlocks-2][blockSize - 1] = str(hex(tryByte)).replace("x", "")
        else:
            blockArray1[numBlocks-2][blockSize - 1] = str(hex(tryByte)).replace("0x", "")
        newBlock = ""
        for i in range(len(blockArray1)):
            newBlock += "".join(blockArray1[i])
        if(PadOracle("".join(blockArray1[numBlocks-2][blockSize - 1])+"".join(blockArray1[numBlocks-1][blockSize - 1]))):
            print(newBlock)
            print(i)
            print(hex(tryByte))
            print(hex(oldByte))
            print(str(hex(i)))
    #print(blockArray)
    
    # end completing here, leave rest unchanged.
else:
    print("You need to specify a file!")
    

