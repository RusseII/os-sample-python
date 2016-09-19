from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hello")
def hello1():
    return "Hello d!"
    
@application.route("/hello1")
def hell2o1():
    return "Hellodssd d!"
    
if __name__ == "__main__":
    application.run()
