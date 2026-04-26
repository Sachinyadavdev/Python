from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {"Rohan":90, "Sohan":80, "Mohan":70}
    return jsonify(marks)
    

app.run(debug=True)