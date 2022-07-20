from flask import Flask, request, jsonify
from flask_cors import CORS

import sys

sys.path.insert(1, '../db')

from dbOps import get_teams, get_team, get_players, get_player

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/teams", methods=["GET"])
def api_get_teams():
    return jsonify(get_teams())

@app.route("/api/team/<id>", methods=["GET"])
def api_get_team(id):
    return jsonify(get_team(id))

@app.route("/api/players", methods=["GET"])
def api_get_players():
    return jsonify(get_players())

@app.route("/api/player/<id>", methods=["GET"])
def api_get_player(id):
    return jsonify(get_player(id))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app