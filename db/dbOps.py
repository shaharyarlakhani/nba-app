import sqlite3

def connect_to_db():
    conn = sqlite3.connect('../db/nbadata.db')
    return conn


def get_teams():
    teams = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nba_teams")
        allTeams = cur.fetchall()

        for i in allTeams:
            team = {}
            team["id"] = i["id"]
            team["name"] = i["name"]
            team["api_id"] = i["api_id"]
            teams.append(team)
    except:
        teams = []

    return teams


def get_team(id):
    team = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nba_teams WHERE api_id = ?", (id,))
        toRet = cur.fetchone()

        team["id"] = toRet["id"]
        team["name"] = toRet["name"]
        team["api_id"] = toRet["api_id"]

        teamPlayers = []
        cur.execute("SELECT * FROM nba_players WHERE api_team_id = ?", (id,))
        allPlayers = cur.fetchall()

        for i in allPlayers:
            player = {}
            player["id"] = i["id"]
            player["name"] = i["name"]
            player["api_id"] = i["api_id"]
            player["api_team_id"] = i["api_team_id"]
            player["jersey"] = i["jersey"]
            teamPlayers.append(player)

        team["team_players"] = teamPlayers
    except:
        team = {}

    return team


def get_players():
    players = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nba_players")
        allPlayers = cur.fetchall()

        for i in allPlayers:
            player = {}
            player["id"] = i["id"]
            player["name"] = i["name"]
            player["api_id"] = i["api_id"]
            player["api_team_id"] = i["api_team_id"]
            player["jersey"] = i["jersey"]
            players.append(player)
    except:
        players = []
        
    return players


def get_player(id):
    player = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nba_players where api_id = ?", (id,))
        toRet = cur.fetchone()

        player["id"] = toRet["id"]
        player["name"] = toRet["name"]
        player["api_id"] = toRet["api_id"]
        player["api_team_id"] = toRet["api_team_id"]
        player["jersey"] = toRet["jersey"]
    except:
        player = {}
        
    return player


# def get_team_players(team_id):
#     players = []
#     try:
#         conn = connect_to_db()
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM nba_players WHERE api_team_id = ?", (team_id,))
#         allPlayers = cur.fetchall()

#         for i in allPlayers:
#             player = {}
#             player["id"] = i["id"]
#             player["name"] = i["name"]
#             player["api_id"] = i["api_id"]
#             player["api_team_id"] = i["api_team_id"]
#             player["jersey"] = i["jersey"]
#             players.append(player)
#     except:
#         players = []
        
#     return players