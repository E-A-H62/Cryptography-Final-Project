# Cryptography Final Project

This project implements a secure communication system between two parties using encryption (RSA + AES) with message authentication. The system encrypts messages using AES, encrypts the AES key with RSA, and appends a MAC for authentication. Communication is simulated through local files rather than actual network sockets.

## Setup

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Generate RSA key pairs for both parties**
   ```bash
   python generate_keys.py
   ```
   This will create the following files:
   - `sender_private.pem` - Sender's private RSA key
   - `sender_public.pem` - Sender's public RSA key
   - `receiver_private.pem` - Receiver's private RSA key
   - `receiver_public.pem` - Receiver's public RSA key

2. **Prepare your message**
   Create a text file containing the message you want to send (e.g., `message.txt`)

3. **Send the message**
   ```bash
   python sender.py
   ```
   When prompted, enter the filename of your message file (e.g., `message.txt`).
   This will create `transmitted_data.txt` containing:
   - Encrypted message (AES-encrypted)
   - Encrypted AES key (RSA-encrypted)
   - MAC (HMAC-SHA256)
   - Nonce and tag (for AES EAX mode)

4. **Receive and decrypt the message**
   ```bash
   python receiver.py
   ```
   The receiver will:
   - Decrypt the AES key using their private RSA key
   - Decrypt the message using the AES key
   - Verify the MAC
   - Display the decrypted message and MAC verification status

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