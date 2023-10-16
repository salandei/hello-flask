from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome_message():
    return "Hello world"

@app.route("/fizzbuzz")
def fizzbuzz():
    

if __name__ == '__main__':
    app.run(debug=True)