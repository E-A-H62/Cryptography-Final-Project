# references:
    # https://qwiet.ai/appsec-resources/securing-python-applications-with-pycrypto/
    # https://www.pycrypto.org

# importing necessary libraries
import Crypto
import pickle
from Crypto.PublicKey import RSA
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP

# receiver reads sender's public key from file
with open('sender_public.pem', 'rb') as f:
    sender_public = RSA.import_key(f.read())
# print(sender_public)

# receiver reads own private key from file
with open('receiver_private.pem', 'rb') as f:
    receiver_private_key = RSA.import_key(f.read())

# receiver reads packet from file
with open('transmitted_data.txt', 'rb') as f:
    packet = pickle.load(f)
encrypted_message = packet[0] # extracts encrypted message from packet
encrypted_aes_key = packet[1] # extracts encrypted AES key from packet
hmac = packet[2] # extracts MAC from packet
nonce = packet[3] # extracts nonce from packet
tag = packet[4] # extracts tag from packet

# receiver decrypts AES key with receiver's private key
cipher_rsa = PKCS1_OAEP.new(receiver_private_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)
# receiver creates new AES cipher in EAX mode with nonce
aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
decrypted_message = aes_cipher.decrypt_and_verify(encrypted_message, tag)
print(decrypted_message.decode('utf-8'))

# receiver verifies MAC
try:
    hmac_verify = HMAC.new(aes_key, encrypted_message, digestmod=SHA256) # creates new HMAC object
    if hmac_verify.digest() != hmac: # checks if MAC is correct
        raise ValueError("MAC verification failed") # raises error if MAC is incorrect
    print("MAC verification successful") # prints success message if MAC is correct
except ValueError as e:
    print(e) # prints error message if MAC is incorrect
    exit(1) # exits program if MAC is incorrect