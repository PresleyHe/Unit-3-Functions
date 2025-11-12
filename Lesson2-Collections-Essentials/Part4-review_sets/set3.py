# Q1:
# [8, 10, 8]

# Q2: 
# NEXUS

# Q3:
player_base = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18}
}
def match_mvp(players):
    topkd = 0
    top_user = ""
    for player, stats in players.items():
        kd = stats["kills"] / stats["deaths"]
        if kd > topkd:
            topkd = kd
            top_user = player
    return top_user

print(match_mvp(player_base))