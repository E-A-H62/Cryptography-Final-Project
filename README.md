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

The application includes an interactive menu system that provides an interface for all operations. First run:
```bash
   python communication_system.py
   ```
Then choose from the provided options in the menu to use the communication system.
1. **Send a message**
   - Select option `1` to send a message and enter your message when prompted
   - The system will:
     - Save your message to `message.txt`
     - Encrypt the message using AES
     - Encrypt the AES key using the receiver's RSA public key
     - Generate a MAC (HMAC-SHA256) for authentication
     - Save all data to `transmitted_data.txt`

2. **Receive and decrypt the message**
   - Select option `2` to receive a message
   - This will:
     - Decrypt the AES key using the receiver's private RSA key
     - Decrypt the message using the AES key
     - Verify the MAC
     - Display the decrypted message and MAC verification status

3. **Generate RSA key pairs for both parties**
   - Select option `3` to generate new RSA key pairs. This will create:
      - `sender_private.pem` - Sender's private RSA key
      - `sender_public.pem` - Sender's public RSA key
      - `receiver_private.pem` - Receiver's private RSA key
      - `receiver_public.pem` - Receiver's public RSA key

4. **Exit the communication system**
   - Select option `4` to exit the program


## Project Structure
- `communication_system.py` - Main interactive menu system that provides a unified interface for sending, receiving, and key generation
- `sender.py` - Contains the `sending()` function that encrypts messages using AES and RSA
- `receiver.py` - Contains the `receiving()` function that decrypts messages and verifies MAC
- `generate_keys.py` - Contains the `generate_keys()` function that creates RSA key pairs for both parties
- `message.txt` - Text file containing the message to be sent (created automatically by the interactive system)
- `transmitted_data.txt` - Binary file containing encrypted message, encrypted AES key, MAC, nonce, and tag (serialized using pickle)
- `sender_private.pem` / `sender_public.pem` - Sender's RSA key pair
- `receiver_private.pem` / `receiver_public.pem` - Receiver's RSA key pair

## Technical Details
- **Encryption**: AES-128 in EAX mode (provides authenticated encryption)
- **Key Exchange**: RSA-2048 with PKCS1_OAEP padding
- **Message Authentication**: HMAC-SHA256
- **Data Serialization**: Python pickle (for preserving binary data in transmitted_data.txt)

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