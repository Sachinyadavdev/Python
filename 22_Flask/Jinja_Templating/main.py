from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {"Rohan":90, "Sohan":80, "Mohan":70}
    return render_template("index.html", marks=marks)



app.run(debug=True)