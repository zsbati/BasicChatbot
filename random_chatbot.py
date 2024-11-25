import random

# Define a dictionary with chatbot responses
responses = {
    'hello': ['Hi!', 'Hello!', 'Hey!'],
    'how are you': ['I\'m good, thanks!', 'I\'m doing great!', 'I\'m just a chatbot, I don\'t have feelings, but thanks for asking!'],
    'what is your name': ['My name is Basic Chatbot', 'I\'m just a chatbot, I don\'t have a personal name', 'You can call me Chatbot!'],
    'default': ['I didn\'t understand that', 'Can you please rephrase?', 'Sorry, I\'m not sure what you mean']
}

# Define a function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses['default'])

# Define a main function to run the chatbot
def main():
    print("Welcome to the Basic Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print('Good bye!')
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the main function
if __name__ == "__main__":
    main()
