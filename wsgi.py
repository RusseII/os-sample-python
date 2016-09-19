from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Wor#@######@#234232dsfld!"

if __name__ == "__main__":
    application.run()
