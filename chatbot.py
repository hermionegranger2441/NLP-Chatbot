import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm good, thanks!", "I'm doing well, how about you?"]],
    ["what is your name", ["I'm a chatbot.", "I don't have a name."]],
    ["bye|goodbye", ["Goodbye!", "Have a great day!"]],
]

chatbot = Chat(pairs, reflections)

def chat_with_user():
    print("Hello! I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_user()
