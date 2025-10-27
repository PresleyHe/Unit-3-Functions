def format_course_code(code):
    trimmed = code.strip()
    print(f"After strip: '{trimmed}'")
    
    uppercased = trimmed.upper()
    print(uppercased)
    return uppercased
print(format_course_code("skldfklajdf"))

# ---------------------------------------
def count_hashtags(post):
    words = post.split()
    
    count = 0
    
    for word in words:
        if word.startswith("#"):
            count += 1
    return count
#testing
post1 = "Great game today! #BergenTech #GoGamrz #pride"
post2 = "Meeting tomorrow in room 205"
post3 = "#Robotics team wins #StateChampionship! #STEM #BergenTech"
print(count_hashtags(post1))

# .endswith() method