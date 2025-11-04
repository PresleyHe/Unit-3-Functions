# Q1:

# {"key_a": "value1", "key_b": 150, "key_d": 50}, "key_c":False

# Q2:

# 120, "val_z":60.0

# Q3.

def get_user_bio(user):
    bio = user.get("bio")
    if bio:
        return user["bio"]
    else:
        return "No bio available"
    
    
print(get_user_bio({"username": "coder", "bio": "Python enthusiast"})) # "Python enthusiast"

print(get_user_bio({"username": "newbie"}))

# Q4
# 60, 160

# Q5

# 1

# Q6

def get_total_engagement(post):
    if not post.get("likes"):
        post["likes"] = 0
    if not post.get("comments"):
        post["comments"] = 0
    if not post.get("shares"):
        post["shares"] = 0
    total = post["likes"] + post["comments"] + post["shares"]
    return total
    
print(get_total_engagement({"likes": 50,"comments": 5})) # 55

# Q7

# 3,3

# Q8

# {"key1": "value1", "key": 200}
# {"key1": "value1", "key2": 200, "key3": 50, "key4": True}

# Q9

def find_most_followed(users):
    if not users:
        return None
    most_followed = users[0]
    for user in users:
        if user["followers"] > most_followed["followers"]:
            most_followed = user
    return most_followed["username"]

users = [
{"username": "alex","followers": 1000},

{"username": "sam","followers": 5000},

{"username": "jordan","followers": 3000}
]
print(find_most_followed(users))