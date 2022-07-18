from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonteamroster
import requests

def getTeams():
    all_teams = teams.get_teams()
    toRet = []
    j = 0
    for i in all_teams:
        toRet.append((j, i['full_name'], i['id']))
        j += 1
    return toRet

# print(teams.get_teams()[0])

def getPlayers():
    all_players = players.get_active_players()
    toRet = []
    j = 1
    for i in all_players:
        toRet.append((j, i['full_name'], i['id']))
        j += 1
    return toRet

# print(players.get_active_players()[0])

def getPlayers2():
    toRet = []
    k = 1
    for i in getTeams():
        temp = commonteamroster.CommonTeamRoster(i[2]).get_normalized_dict()
        for j in temp['CommonTeamRoster']:
            toRet.append((k, j['PLAYER'], j['PLAYER_ID'], j['TeamID'], j['NUM']))
            k += 1
    return toRet

# temp = commonteamroster.CommonTeamRoster(1610612737).get_normalized_dict()
# for i in temp['CommonTeamRoster']:
#     print(i)
