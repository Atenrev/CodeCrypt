import sys
import hashlib

class codeUtilities:
    
    # Generate the key from a passed string
    def generateKey (key):
        b = bytearray()
        b.extend(map(ord,key))
        sha = hashlib.sha256()
        sha.update(b)
        return sha.digest()
    
    # Applies a xor operation to the passed data using the passed key
    def operate (data, key):
        int_data = int.from_bytes(data, sys.byteorder)
        int_key = int.from_bytes(key, sys.byteorder)
        int_enc = int_data ^ int_key
        return int_enc.to_bytes(len(data), sys.byteorder)
