import sys
import base64
from codeUtilities import *

usage = "Uso: {0} {1}".format(sys.argv[0], '[archivo]')

class codeDecrypt(object):
    
    def __init__(self, data, key):
        self.data = data
        self.key = key

    # Decrypt a block of 32 bytes
    def decryptBlock(self, block):
        return codeUtilities.operate( base64.b64decode(block),self.key )

    def decryptText(self):
        message = "\nMessage: "
        arrayBlock = ""
        
        for b in self.data:
                if len(arrayBlock) < 44:
                    arrayBlock += b
                else:
                    message += self.decryptBlock(arrayBlock).decode("utf-8")
                    arrayBlock = b

        message += self.decryptBlock(arrayBlock).decode("utf-8")                     
        print(message)
    
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
        

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        print ()
        print ("\t---- Welcome to CodeCrypt 1.1 ----")
        e = codeDecrypt(sys.argv[1], codeUtilities.generateKey(sys.argv[2]))
        print ("\nProceeding to decrypt...")
        if (len(sys.argv) > 3 and sys.argv[3].lower() == "file"):
            e.decryptFile()
        else:
            e.decryptText()
        print ("\nSuccess")
    else:
        print (usage)
