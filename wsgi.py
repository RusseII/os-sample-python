from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hello")
def hello1():
    return "Hello World!"
    
if __name__ == "__main__":
    application.run()
