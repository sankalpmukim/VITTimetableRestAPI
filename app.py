from flask import Flask, jsonify, request
from calendarGenerator import generate_calendar

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to main home page"


@app.route('/json', methods=['GET', 'POST'])
def json():
    if request.method == 'GET':
        print("GET")
        return jsonify({"RESPONSE": "GET method used. use POST(JSON)"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify(generate_calendar(data['timetable']))
    else:
        return "INVALID REQUEST"


if __name__ == '__main__':
    app.run(debug=True)
