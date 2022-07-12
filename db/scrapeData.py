from nba_api.stats.static import teams, players

def getTeams():
    all_teams = teams.get_teams()
    return [i['full_name'] for i in all_teams]

# all_players = players.get_active_players()

# for i in all_players:
#     print(i['full_name'])
