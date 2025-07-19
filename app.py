from flask import Flask

app = Flask("saw-flask-ce11")

@app.route("/")
def hello_world():
    return "<p>Hello, Saw Gwe Aw!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
