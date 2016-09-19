from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hef34232dsfld!"
    
@app.route("/hi")
def hello23():
    return "Hewef34232dsfld!"

if __name__ == "__main__":
    app.run()
