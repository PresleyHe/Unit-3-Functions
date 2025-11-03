# Q2:
def find_top_players(players, min_score):
    top_players = []
    for player in players:
        if player.get("score") >= min_score:
            top_players.append(player["username"])
    return top_players
    pass


players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)
# Q3:
playlists = {
    "Workout Mix": ["Eye of the Tiger", "Stronger", "Lose Yourself"],
    "Study Vibes": ["Lofi Beat 1", "Chill Piano", "Rain Sounds"],
    "Party Hits": ["Uptown Funk", "Levitating", "Blinding Lights"]
}

all_songs = []

for playlist_name, songs in playlists.items():
    for song in songs:
        all_songs.append(song.upper())

print(f"Total songs: {len(all_songs)}")
print(f"First song: {all_songs[0]}")
print(f"Last song: {all_songs[-1]}")

# Q4:
def calculate_cart_total(cart):
    total_cost = 0
    for item in cart:
        total_cost += item["price"] * item["quantity"]
    return total_cost
    pass

cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3}
]

total = calculate_cart_total(cart)
print(f"Total: ${total:.2f}")
