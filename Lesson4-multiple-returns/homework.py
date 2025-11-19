# Q1:
database = ["john", "admin"]

def search_user_database(query):
    if not query:
        return None, "No search query", False
    if query.strip() == "":
        return None, "No search query", False
    if not query.isalpha():
        return False, "Invalid characters", False
    if query not in database:
        return 0, "No users found", True
    if query in database:
        return 1, "User found", True

result, message, success = search_user_database("user@email")
print(result) # False
print(message) # "Invalid characters"
print(success) # False

# Q2:

def analyze_book_pages(pages):
    if not pages:
        return "N"
    count = len(pages)
    total = sum(pages)
    avg = total / count
    avg = round(avg, 2)
    has_long = False
    for page in pages:
        if page > 500:
            has_long = True
    return count, total, avg, has_long

# TEST 1: Mixed collection with one long book
count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count) # 4
print(total) # 1360
print(avg) # 340.0
print(has_long) # True (because 620 > 500)

# TEST 2: No long books
count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(count) # 3
print(total) # 650
print(avg) # 216.67 (approximately) 67
print(has_long) # False (all books ≤ 500)