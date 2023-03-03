import pyAesCrypt


# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024


# encrypt
def AESsave (original, encrypted, key, bufferSize):
    pyAesCrypt.encryptFile(original, encrypted, key, bufferSize)

    pass

# decrypt
def AESopen (raw, decrypted, key, bufferSize):
    pyAesCrypt.decryptFile(raw, decrypted, key, bufferSize)

    pass

#encrypt
#pyAesCrypt.encryptFile("texts/data.txt", "texts/data.txt.aes", w, bufferSize)
# decrypt
#pyAesCrypt.decryptFile("texts/data.txt.aes", "texts/dataout.txt", w, bufferSize)