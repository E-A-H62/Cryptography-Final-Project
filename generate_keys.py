# references:
    # https://qwiet.ai/appsec-resources/securing-python-applications-with-pycrypto/
    # https://www.pycrypto.org
    # https://pycryptodome.readocs.io/en/latest/src/examples.html

# importing Crypto library to generate RSA key pair
import Crypto
from Crypto.PublicKey import RSA

# receiver generates own RSA key pair and saves to files
receiver_rsa_key = RSA.generate(2048) # 2048 bits recommended for security
receiver_private = receiver_rsa_key.export_key() # exports private key to PEM format
receiver_public = receiver_rsa_key.publickey().export_key() # exports public key to PEM format
with open('receiver_private.pem', 'wb') as f: # saves private key to file
    f.write(receiver_private)
with open('receiver_public.pem', 'wb') as f: # saves public key to file
    f.write(receiver_public)

# sender generates own RSA key pair and saves to files
sender_rsa_key = RSA.generate(2048) # 2048 bits recommended for security
sender_private = sender_rsa_key.export_key() # exports private key to PEM format
sender_public = sender_rsa_key.publickey().export_key() # exports public key to PEM format
with open('sender_private.pem', 'wb') as f: # saves private key to file
    f.write(sender_private)
with open('sender_public.pem', 'wb') as f:
    f.write(sender_public)