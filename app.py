from flask import Flask, jsonify, redirect, request
from calendarGenerator import generate_calendar

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("https://documenter.getpostman.com/view/15245880/TzCS6S6S", code=302)


@app.route("/vellore", methods=["GET", "POST"])
def vellore():
    if request.method == "GET":
        print("GET")
        return jsonify({"RESPONSE": "GET method used. use POST(JSON)"})
    elif request.method == "POST":
        data = request.get_json()
        return jsonify(generate_calendar(data["timetable"]))
    else:
        return "INVALID REQUEST"


if __name__ == "__main__":
    app.run(debug=True)
