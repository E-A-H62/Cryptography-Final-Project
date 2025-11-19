# Cryptography Final Project

In this project we are tasked to design and (partially) implement a secure communication system
between two parties.

## Requirements:
The requirements of the system include:
1. The two parties have each other’s RSA public key. Each of them holds his/her own RSA
private key.
2. Each party’s message (from a .txt file) is encrypted using AES before sending it to
another party.
3. The AES key used in Step 2 is encrypted using the receiver’s RSA public key. The encrypted
AES key is sent together with the encrypted message obtained from Step 2.
4. Message authentication code should be appended to data transmitted. You are free to
choose the specific protocol of MAC.
5. The receiver should be able to successfully authenticate, decrypt the message, and read
the original message.

There must be a program for each role (i.e., sender and receiver), although it is not required to
include actual socket programming in the code. As an alternative, local files can be used as the channel to
simulate the communication in the network.
- i.e.: To implement requirement 1 above, each party can locally generate a key pair and save each key in a corresponding file. The other
party will be able to know the public key by accessing the file
- We can create a file called
“Transmitted_Data”, which can include all data transmitted between sender and receiver (i.e.:
encrypted message, encrypted AES key, and the MAC). This file is written by the sender and read
by the receiver