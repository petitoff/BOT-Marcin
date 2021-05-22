from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    print(user_text)
    user_text2 = user_text
    return user_text2


if __name__ == '__main__':
    app.run()
