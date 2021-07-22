from flask import Flask, jsonify, redirect, request
from flask.helpers import send_file
from calendarGenerator import generate_calendar
import os

app = Flask(__name__)


# @app.route("/")
# def index():
#     return redirect("https://documenter.getpostman.com/view/15245880/TzCTZk7J", code=302)


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "GET":
        print("GET")
        return jsonify({"RESPONSE": "GET method used. use POST(JSON)"})
    elif request.method == "POST":
        data = request.get_json()
        return jsonify(generate_calendar(data))
    else:
        return "INVALID REQUEST"

@app.route("/download/<filename>", methods=["GET"])
def download(filename=None):
    dirname = './icsfiles/'
    try:
        return send_file(dirname+filename+'.ics')
    except FileNotFoundError:
        return filename+' does not exist (anymore). Please try again'

@app.route("/delete/<filename>",methods=["GET"])
def delete(filename):
    dirname = './icsfiles/'
    if os.path.exists(dirname+filename+'.ics'):
        os.remove(dirname+filename+'.ics')
        return jsonify({"found":True})
    return jsonify({"found":False})

if __name__ == "__main__":
    app.run(debug=True)
