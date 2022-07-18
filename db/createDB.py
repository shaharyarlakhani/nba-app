import sqlite3
from scrapeData import getPlayers2
from scrapeData import getTeams

connect = sqlite3.connect('nbadata.db')

cursor = connect.cursor()

# ----- nba teams table -----

# cursor.execute("DROP TABLE IF EXISTS nba_teams")
# teams_table = """ CREATE TABLE nba_teams (
#                 id int NOT NULL PRIMARY KEY,
#                 name varchar(255) NOT NULL,
#                 api_id int NOT NULL
#             ); """
# cursor.execute(teams_table)
# add_teams = "INSERT INTO nba_teams VALUES (?, ?, ?)"
# cursor.executemany(add_teams, getTeams())


# ----- nba players table -----

cursor.execute("DROP TABLE IF EXISTS nba_players")
players_table = """ CREATE TABLE nba_players (
                id int NOT NULL PRIMARY KEY,
                name varchar(255) NOT NULL,
                api_id int NOT NULL,
                api_team_id int NOT NULL,
                jersey int
            ); """
cursor.execute(players_table)
add_players = "INSERT INTO nba_players VALUES (?, ?, ?, ?, ?)"
cursor.executemany(add_players, getPlayers2())

# q = "SELECT * from nba_players WHERE api_team_id=1610612744"
# cursor.execute(q)
# print(cursor.fetchall())

connect.commit()

connect.close()