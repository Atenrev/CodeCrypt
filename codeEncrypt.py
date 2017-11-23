import sys
import base64
from codeUtilities import *

usage = "Uso: {0} {1}".format(sys.argv[0], '[archivo]')

class codeEncrypt(object):
    
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.byteArray = []
        self.encryptedByteArray = bytearray()
    
    def readFile(self):
        file = open(self.data,"rb")
        arrayBlock = []
        # Read file in binary in blocks of 32 bytes
        for l in file:
            for w in l:
                if len(arrayBlock) < 32:
                    arrayBlock += [w]
                else:
                    self.byteArray.append(arrayBlock)
                    arrayBlock = [w]
        # Add padding if needed
        if len(arrayBlock) < 32: 
            while len(arrayBlock) < 32:
                arrayBlock += [0]
        self.byteArray.append(arrayBlock)
        file.close()

    def encryptFile(self):
        for i in self.byteArray:
            self.encryptedByteArray += ( codeUtilities.operate(i,self.key) )

    def writeFile(self):
        file = open("{0}.{1}".format("result","crypt"),"wb")
        file.write(base64.b64encode(self.encryptedByteArray))
        file.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print ()
        print ("\t---- Welcome to CodeCrypt 1.0 ----")
        e = codeEncrypt(sys.argv[1], codeUtilities.generateKey(sys.argv[2]))
        print ()
        print ("Reading file...")
        e.readFile()
        print ()
        print ("Proceeding to encrypt...")
        e.encryptFile()
        print ("Done")
        print ()
        print ("Writing file...")
        e.writeFile()
        print ("Success")
    else:
        print (usage)
