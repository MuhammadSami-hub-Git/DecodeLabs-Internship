# DecodeLabs AI Internship
# Week 1 Project: Rule-Based AI Chatbot

print("=" * 50)
print("🤖 Welcome to the Rule-Based AI Chatbot")
print("Type 'bye' or 'exit' to end the conversation.")
print("=" * 50)

while True:
    user_input = input("\nYou: ").lower().strip()

  
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

   
    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "how are you":
        print("Bot: I am doing great! Thanks for asking.")

    
    elif user_input == "what can you do":
        print("Bot: I can respond to predefined commands using rule-based logic.")

 
    elif user_input == "help":
        print("Bot: You can try saying:")
        print("     - hi")
        print("     - how are you")
        print("     - what is your name")
        print("     - what can you do")
        print("     - bye")


    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that command.")