from flask import Flask, render_template, request

from chat import *

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')  # get message from user <= HTML

    user_msg = Chat().chat_analyze(user_text)  # start analyze chat.py

    # user_text2 = user_text  # this is only for test, remove before upload / only for dev
    return user_msg


if __name__ == '__main__':
    app.run()
