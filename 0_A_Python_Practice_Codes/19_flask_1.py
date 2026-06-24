from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page"


@app.route("/contact")
def contact():
    return "This is the Contact Page"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!, Welcome to the Users page"

if __name__ == "__main__":
    app.run(debug=True)

