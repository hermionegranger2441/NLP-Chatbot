from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm good, thanks!", "I'm doing well, how about you?"]],
    ["what is your name", ["I'm a chatbot.", "I don't have a name."]],
    ["bye|goodbye", ["Goodbye!", "Have a great day!"]],
]

chatbot = Chat(pairs, reflections)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/send', methods=['POST'])
def send():
    user_input = request.json['user_input']
    response = chatbot.respond(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
