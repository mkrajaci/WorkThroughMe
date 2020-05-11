from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "This site represents God's works through me!"


if __name__ == '__main__':
    app.run()
