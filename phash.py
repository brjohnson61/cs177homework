from Crypto.Hash import MD5
import binascii

def hash(msg):
    # pad message to 16 bytes
    if len(msg) < 16:
        msg = msg + (16 - len(msg)) * 'A'
        
    # pick first 16 bytes
    msg = msg[:16]
    
    # converts message to upper case
    msg = msg.upper()

    # create MD5 objects
    h1 = MD5.new()
    h2 = MD5.new()

    # hash two parts of message separately
    h1.update(msg[:8])
    h2.update(msg[8:16])

    # concatenate the two hashes
    h = h1.digest() + h2.digest()
    return h
    
print(binascii.hexlify(hash("Hello, this is a great passphrase, and I am wondering if anyone can crack it")))

