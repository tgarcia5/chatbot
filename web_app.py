from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os

# Creating a chatbot Instance
bot = ChatBot('Buddy',
            logic_adapters=[{ 'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Perdon, no entiendo',
            'maximum_similarity_threshold': 0.90}],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii'])

# locate training folder
directory = 'training_data'

for filename in os.listdir(directory):
    if filename.endswith(".txt"): # only pick txt file for training
        print('\n Chatbot training with '+os.path.join(directory, filename)+' file')
        training_data = open(os.path.join(directory, filename)).read().splitlines()
        trainer = ListTrainer(bot) # bot training
        trainer.train(training_data)
    else:
        continue

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return str(bot.get_response(user_input))


if __name__ == "__main__":
    app.run()
