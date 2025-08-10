import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"i need some help",
        ["Sure!what do you need help with."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a nice day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that."]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()