def calculate_engagement_rate(post):
    view = post.get("views",0)
    if view == 0:
        return 0
    comments = post.get("comments", 0)
    shares = post.get("shares", 0)
    likes = post.get("likes", 0)
    engagement = shares + comments + likes
    rate = (engagement / view) * 100
    return round(rate, 2) 
post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
print(calculate_engagement_rate(post))