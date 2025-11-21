from sender import sending
from receiver import receiving
from generate_keys import generate_keys

# global variables to track if message has been sent or received
message_sent = False
message_received = False

def send_message():
    """Sends a message to receiver."""
    # global keyword is used to access global variables
    global message_sent
    global message_received
    # checks if user wants to send a new message if previous message has been sent and not received
    if message_sent and not message_received:
        print("The message you sent previously has not been received yet.")
        print("If you send a new message, the previous message will be lost.")
        print("Would you like to send a new message anyway? (y/n): ")
        confirm = input()
        # if user wants to send a new message, previous message is lost
        if confirm == "y":
            print("Overwriting previous message...")
            message = input("Enter your message: ")
            print("Sending message...")
            with open('message.txt', 'w') as f: # writes message to file
                f.write(message)
            sending() # sends message
            message_sent = True # sets message_sent to True
            message_received = False # sets message_received to False
            print("Message sent successfully!")
        else:
            print("Message not sent.")
            return
    # if receiver has no new message received yet, sender can new message
    else:
        message = input("Enter your message: ")
        print("Sending message...")
        with open('message.txt', 'w') as f: # writes message to file
            f.write(message)
        sending() # sends message
        message_sent = True # sets message_sent to True
        message_received = False # sets message_received to False
        print("Message sent successfully!")

def receive_message():
    """Receives a message from sender."""
    # global keyword is used to access global variables
    global message_sent
    global message_received
    print("Receiving message...")
    # tries to receive message
    try:
        if message_sent: # if message has been sent, receives message
            receiving() # receives message
            message_sent = False # sets message_sent to False
            message_received = True # sets message_received to True
            print("Message received successfully!")
        else: # if message has not been sent, prints error message
            print("No message to receive.")
    except Exception as e: # if error occurs, prints error message
        print(f"Error receiving message: {e}") # prints error message

def main():
    """Main function to run the communication system."""
    # prints welcome message and options of system
    print("\nWelcome to the communication system!")
    print("1. Send a message")
    print("2. Receive a message")
    print("3. Generate keys")
    print("4. Exit")
    choice = input("Enter your choice: ") # user inputs choice
    # user can choose send message, receive message, generate keys, or exit system
    if choice == "1":
        send_message()
        main()
    elif choice == "2":
        receive_message()
        main()
    elif choice == "3":
        # if user wants to generate new keys, overwrites existing keys
        print("Warning: This will overwrite existing keys!")
        print("Messages encrypted with previous keys will be lost!")
        confirm = input("Are you sure you want to continue? (y/n): ")
        if confirm == "y":
            generate_keys()
            print("Keys generated successfully!")
            main()
        else:
            print("Keys not generated.")
            main()
    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

# runs main function
if __name__ == "__main__":
    main()
