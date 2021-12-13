from flask import Flask
app= Flask(__name__)

# Create Flask Route
@app.route("/")
def hello_world():
    return "Hello world "