import sys
import hashlib

class ccutilities:
    # Generate the key from a string passed
    def generateKey (key):
        b = bytearray()
        b.extend(map(ord,key))
        sha = hashlib.sha256()
        sha.update(b)
        return sha.digest()
    # Applies an xor operation to the data passed using the key passed
    def operate (data, key):
        int_data = int.from_bytes(data, sys.byteorder)
        int_key = int.from_bytes(key, sys.byteorder)
        int_enc = int_data ^ int_key
        return int_enc.to_bytes(len(data), sys.byteorder)
