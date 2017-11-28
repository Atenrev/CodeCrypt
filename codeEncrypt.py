import sys
import base64
from codeUtilities import *

usage = "Uso: {0} {1}".format(sys.argv[0], '[archivo]')

class codeEncrypt(object):
    
    def __init__(self, data, key):
        self.data = data
        self.key = key
    
    def encryptFile(self):
        ext = self.data.split(".")[len(self.data.split("."))-1]
        inputFile = open(self.data,"rb")
        finalFile = open("{0}.{1}".format("crypt",ext),"wb")
        arrayBlock = []
        # Read file in binary in blocks of 32 bytes
        for l in inputFile:
            for w in l:
                if len(arrayBlock) < 32:
                    arrayBlock += [w]
                else:
                    # Write the encrypted block in base64
                    finalFile.write( self.encryptBlock(arrayBlock) )
                    arrayBlock = [w]
        # Add padding if needed and write the last block
        while len(arrayBlock) < 32:
                arrayBlock += [0]
        finalFile.write( self.encryptBlock(arrayBlock) )
        inputFile.close()
        finalFile.close()
    # Encrypt a block of 32 bytes and encode it
    def encryptBlock(self, block):
        return base64.b64encode(codeUtilities.operate(block,self.key))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print ("\n\t---- Welcome to CodeCrypt 1.1 ----")
        e = codeEncrypt(sys.argv[1], codeUtilities.generateKey(sys.argv[2]))
        print ("\nProceeding to encrypt...")
        e.encryptFile()
        print ("\nSuccess")
    else:
        print (usage)
