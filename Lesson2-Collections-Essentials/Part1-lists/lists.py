""" 
Create: [1,2,3]
Add: .apend(val)
remove end: .pop()
insert: .insert(index, val)
length: len(list)
slice: [start:end], 
Index: [0]
"""
#creating lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "user123", True]
#accessing elements
first_day = daily_likes[0] #500
last_day = daily_likes[-1] #400
third_day = daily_likes[2] #750
# Slicing (like JavaScript slice())
first_three = daily_likes[0:3]
last_two = daily_likes[-2:] #[750, 400]


# Code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty!"

def format_usernames(handles):
    formatted = []
    for handle in handles:
        formatted.append("@" + handle)
    return formatted
print(format_usernames(["nasa", "tswift", "netflix"]))


likes = [500, 1200, 800, 1500, 600]
def filter_trending_posts(likes_list):
    for i in likes:
        trending = []
        if likes > 1000:
            trending.append(likes)
    return trending

print(filter_trending_posts(likes))