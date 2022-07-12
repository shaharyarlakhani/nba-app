import sqlite3
from scrapeData import getTeams

connect = sqlite3.connect('nbadata.db')

cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS nba_teams")

teams_table = """ CREATE TABLE nba_teams (
                id int NOT NULL PRIMARY KEY,
                name varchar(255) NOT NULL
            ); """

cursor.execute(teams_table)

print("Table is Ready!")

# add_teams = """ INSERT INTO nba_teams VALUES (); """

connect.close()