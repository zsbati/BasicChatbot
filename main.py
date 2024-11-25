def greet(name):
    return f"Hello, {name}! How can I help you today?"

def respond(user_input):
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Greetings! How are you doing?"
    elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
        return "Farewell! Have a wonderful day."
    else:
        return "I'm still learning. I didn't understand that."

# Get the user's name
name = input("Please enter your name: ")
print(greet(name))

# Main interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break  # Exit the loop if the user types 'exit'
    print("Bot:", respond(user_input))

print("Thank you for chatting!")
