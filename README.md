# CodeCrypt
Encrypt your files with a single command.

## How does it work?
CodeEncrypt uses a symmetric algorithm based on XOR operation. 

The arguments that accept are the data that the user wants to encrypt/decrypt and the key with which the operations will be done.

It first does a SHA-256 hash of the passed key and divides the bytes of the file in blocks of 32 bytes. If the last block is smaller than 32 bytes, it adds padding until the number is reached. Then it does the XOR operations to every block with the key and puts the result in a single bytearray. Finally, it encodes the bytearray to Base64 and writes the file.

## HowTo
To run CodeEncrypt use a command like this:

	.\codeEncrypt.py 'PATH\FILE.EXT' KEY
	
where .\codeEncrypt is the python script, 'PATH\FILE.EXT' is the path to the file that you want to encrypt and KEY is the symmetric key that you will use.
