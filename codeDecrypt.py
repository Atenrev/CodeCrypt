import sys
import base64
from codeUtilities import *

usage = "Uso: {0} {1}".format(sys.argv[0], '[archivo]')

class codeDecrypt(object):
    
    def __init__(self, data, key):
        self.data = data
        self.key = key
    
    def decryptFile(self):
        ext = self.data.split(".")[len(self.data.split("."))-1]
        inputFile = open(self.data,"r")
        finalFile = open("{0}.{1}".format("decrypt",ext),"wb")
        arrayBlock = ""
        # Read file in blocks of 32 bytes
        for l in inputFile:
            for b in l:
                if len(arrayBlock) < 44:
                    arrayBlock += b
                else:
                    # Write the decrypted block
                    finalFile.write( self.decryptBlock(arrayBlock) )
                    arrayBlock = b
        finalFile.write( self.decryptBlock(arrayBlock) )
        inputFile.close()
        finalFile.close()
    # Decrypt a block of 32 bytes
    def decryptBlock(self, block):
        return codeUtilities.operate( base64.b64decode(block),self.key )

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print ()
        print ("\t---- Welcome to CodeCrypt 1.1 ----")
        e = codeDecrypt(sys.argv[1], codeUtilities.generateKey(sys.argv[2]))
        print ("\nProceeding to decrypt...")
        e.decryptFile()
        print ("\nSuccess")
    else:
        print (usage)
