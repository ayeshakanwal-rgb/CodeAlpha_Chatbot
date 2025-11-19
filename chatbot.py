def chatbot():
    print("Welcome to CodeAlpha Basic Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi there!")
        
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks for asking!")
        
        elif user_input in ["bye", "exit", "quist"]:
            print("Bot: Goodbye! Have a great day!")
            break
        
        elif user_input == "":
            print("Bot: Please type something...")
        
        else:
            print("Bot: Sorry, I don't understand that.")
            

# Run the chatbot
chatbot()
