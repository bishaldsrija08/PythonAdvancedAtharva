# Chatbot using dictionary and string operations

responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you?": "I'm just a program, but thanks for asking!",
    "what is your name?": "I'm ChatBot, your virtual assistant.",
    "weather": "I can't check the weather yet, but I bet it's nice outside!",
    "help": "You can ask me things like 'how are you', 'what's your name', or say 'bye' to exit.",
    "bye": "Goodbye! Have a great day!"
}

print("Welcome to ChatBot! Type 'help' for assistance or 'bye' to exit.")

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input == "bye":
        print("ChatBot: " + responses["bye"])
        break
    
    if user_input == "help":
        print("ChatBot: " + responses["help"])
        continue
    
    matched = False # Flag to check if a response was found
    
    for key, value in responses.items():
        if key in user_input:
            print("ChatBot: " + value)
            matched = True
            break

    if not matched:
        print("ChatBot: I'm not sure how to respond to that. Try asking something else!")