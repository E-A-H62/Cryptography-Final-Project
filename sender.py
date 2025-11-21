# references:
    # https://qwiet.ai/appsec-resources/securing-python-applications-with-pycrypto/
    # https://www.pycrypto.org
    # https://pycryptodome.readocs.io/en/latest/src/examples.html
    # https://pythonfolab.com/blog/storing-binary-data-and-serializing/
    # https://www.datacamp.com/tutorial/pickle-python-tutorial

# importing necessary libraries
import Crypto
import pickle
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import HMAC, SHA256

def sending():
    # sender reads receiver's public key from file
    with open('receiver_public.pem', 'rb') as f:
        receiver_public = RSA.import_key(f.read())
    # print(receiver_public)

    # sender has own message in text file
    # message = input("Enter filename of message: ")
    # with open(message, 'r') as f:
    #     message = f.read()
    message = open('message.txt', 'r').read()

    packet = [] # array to store packet

    # sender's message is encrypted with AES before sending to receiver
    aes_key = get_random_bytes(16) # generates random AES key
    nonce = get_random_bytes(16) # generates random nonce for EAX mode
    aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce) # creates new AES cipher in EAX mode
    encrypted_message, tag = aes_cipher.encrypt_and_digest(message.encode('utf-8')) # encrypts message and generates tag

    # AES key encrypted with receiver's RSA public key so it can be sent with encrypted message
    cipher_rsa = PKCS1_OAEP.new(receiver_public) # creates new RSA cipher
    encrypted_aes_key = cipher_rsa.encrypt(aes_key) # encrypts AES key with receiver's public key

    # MAC appended to data to be transmitted (can choose specific protocol of MAC)
    hmac = HMAC.new(aes_key, encrypted_message, digestmod=SHA256)

    # packet is created to store data to be transmitted
    packet.append(encrypted_message) # appends encrypted message to packet
    packet.append(encrypted_aes_key) # appends encrypted AES key to packet
    packet.append(hmac.digest()) # appends MAC to packet
    packet.append(nonce) # appends nonce to packet
    packet.append(tag) # appends tag to packet

    # encrypted message, encrypted AES key, and MAC sent to receiver
    # using pickle to serialize packet array to preserve binary data integrity
    with open('transmitted_data.txt', 'wb') as f:
        pickle.dump(packet, f)