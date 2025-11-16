# Using keyword arguments
def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile."""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }
player1 = create_gamer(username="BTStudent", 
                           level=25,
                           rank="Gold",
                           xp=10000,
                           online= True)

print(player1)

def send_message(sender, recipient, message, urgent):
    return f"{sender} -> {recipient}: {message} (Urgent: {urgent})"

Messenger = send_message(sender="Alex", 
                         recipient="Jordan",
                         message= "Check Discord",
                         urgent=True)

print(Messenger)


def post_content(username, text, likes=0, retweets=0):
    return f"{username}: {text} |❤️  {likes} ♻️  {retweets}"
content = post_content(username="@techguru", text="Python is amazing", likes=0, retweets=0)
print(content)


# *args - Accept Any Number of values

def sum_scores(*scores):
    """Sum ANY Number of scores"""
    total = 0
    for score in scores:
        total += scores
    return total

result1 = sum_scores(10,20,30)
result1 = sum_scores(10,20,30, 55, 68)