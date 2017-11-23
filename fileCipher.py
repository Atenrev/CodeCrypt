import sys
import base64
from ccutilities import *

usage = "Uso: {0} {1}".format(sys.argv[0], '[archivo]')

class fileCipher(object):
    
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
            if len(arrayBlock) <= 32:
                arrayBlock += list(l)
            else:
                self.byteArray.append(arrayBlock)
                arrayBlock = list(l)
        # Add padding if needed
        if len(arrayBlock) < 32: 
            while len(arrayBlock) < 32:
                arrayBlock += [0]
        self.byteArray.append(arrayBlock)
        file.close()

    def encryptFile(self):
        for i in self.byteArray:
            self.encryptedByteArray += ( ccutilities.operate(i,self.key) )

    def writeFile(self):
        file = open(self.data.split(".")[0] + ".crypt","wb")
        file.write(base64.b64encode(self.encryptedByteArray))
        file.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        e = fileCipher(sys.argv[1], ccutilities.generateKey(sys.argv[2]))
        e.readFile()
        e.encryptFile()
        e.writeFile()
    else:
        print (usage)
