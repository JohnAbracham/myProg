from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os

print("[!] This program use RSA algorithm\n")
print("[!] Before using this pogram you need have the public key and the private key\n")
print("[!] Booth keys you can generate using genKey.py")

# File name
data = input("Input filename or his dir\n")

# encrypt file
def encrypt(dataFile, publicKeyFile):

    # read data from file
    with open(dataFile, 'rb') as f:
        data = f.read()
    
    # convert data to bytes
    data = bytes(data)

    # read public key from file
    with open(publicKeyFile, 'rb') as f:
        publicKey = f.read()
    
    # create public key object
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    # encrypt the session key with the public key
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # encrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    []

    # save the encrypted data to file
    [ fileName, fileExtension ] = dataFile.split('.')
    encryptedFile = fileName + '_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]
    print('Encrypted file saved to ' + encryptedFile)
    
# decrypt file
def decrypt(dataFile, privateKeyFile):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''

    # read private key from file
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)


    # read data from file
    with open(dataFile, 'rb') as f:
        # convert data to bytes
        

        # read the session key
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

    
    # decrypt the session key
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # decrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # save the decrypted data to file
    [ fileName, fileExtension ] = dataFile.split('.')
    decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)


    print('Decrypted file saved to ' + decryptedFile)

cd 
def main():

    # Mode program
    mode = "0"

    print("Select options:\t[1] Enrypt\t[2] Decrypt")

    while(mode != "99"):

        mode = str(input("Mode is:"))

        if mode == "1":
            # Public key
            publicKey = input("[!] Input filename public key\n")
            encrypt( data, publicKey)
            print("[+] File is encrypt\n")
            mode = "99"
        elif mode == "2":
            # Private keydata
            privateKey = input("[!] Input filename private key\n")
            decrypt( data, privateKey)
            print("[+] File decrypt\n")
            mode = "99"
        else:
            print("Try again! This options not use!\n")

    print('Done\n')

if __name__ == "__main__":
    main()