# # Q18:
# def  validate_password(password):
#     if not password:
#         return False, "Empty Password!"
#     if len(password) < 8:
#         return False, "Too short"
#     return True, "Valid"

# print(validate_password(""))
# print(validate_password("abc"))
# print(validate_password("secure123"))
    
    
# # Q19:
# def create_inventory(item_name, *quantities, location = "Warehouse"):
#     return {
#         "item name": item_name,
#         "quantity": sum(quantities),
#         "location": location
#     }
# print(create_inventory("Widget", 10, 20, 15))

# # Q20:
# def safe_list_access(item, index):
#     try: 
#         # if index < len(item):
#         #     return item[index], True
#         value = item[index]
#         return value
#     except IndexError:
#         return None, False
    
# print(safe_list_access([10,20,30], 1))
# print(safe_list_access([10,20,30], 10))


    
# def long_str(lst):
#     longest = ""
#     for str in lst:
#         if len(str) > len(longest):
#             longest = str
#     return longest

# print(long_str(["123", "jump", "apples"]))



#----------------------------------UNIT REVIEW ----------------------------


#--------------------------------LESSON 1--------------------------
#instr:
#function that takes a password
# password has to be atleast 8 characters long
#passworld must include a digit and a letter
print("--------------------LESSON 1---------------")
def validate_password(password):
    valid = True
    isdigit = False
    isletter = False
    if not password: 
        valid = False
    for char in password:
        if char.isdigit():
            isletter = True
            break
    for char in password:
        if char.isalpha():
            isdigit = True
            break
    if len(password) < 8:
        valid = False
    if isdigit == False:
        valid = False
    if isletter == False:
        valid = False
    return valid
    

# Corrections
testCase = validate_password("")
testCase1 = validate_password("16")
testCase2 = validate_password("passwordlongenoulgh")
testCase3 = validate_password("correctPassword123")
correct = True


print(validate_password("16"))
if testCase == False:
    print("correct!✅")
else:
    print("incorrect❌")
if testCase1 == False:
    print("correct!✅")
else:
    print("incorrect❌")
if testCase2 == False:
    print("correct!✅")
else:
    print("incorrect❌")
if testCase3 == True:
    print("correct!✅")
else:
    print("incorrect❌")
    
    
#-----------------------------Lesson2----------------------------
print("--------------------LESSON 2---------------")

#INSTR

def find_common(list1, list2):
    common = []
    if (list1 and list2) == []:
        return None 
    for char in list1:
        if char in list2 and char not in common:
            common.append(char)
    return common


# print(find_common([1,2,4, 4], [4,2, 1])) #1,2,4
print(find_common([], []))

testCase1 = find_common([1,2,4, 4], [4,2, 1])
testCase2 = find_common([], [])

if testCase1 == [1,2,4]:
    print("correct!✅")
else:
    print("incorrect❌")
if testCase2 == None:
    print("correct!✅")
else:
    print("incorrect❌")


def filter_trending_posts(likes_list):
    trending = []
    if likes_list == []:
        return None
    for i in likes_list:
        if i > 1000:
            trending.append(i)
    return trending
likes = [500, 1200, 800, 1500, 600]

# print(filter_trending_posts(likes))
# print(filter_trending_posts([]))
testCase1 = filter_trending_posts(likes)
testCase2 = filter_trending_posts([])
#corrections
if testCase1 == [1200, 1500]:
    print("correct!✅")
else:
    print("incorrect❌")
if testCase2 == None:
    print("correct!✅")
else:
    print("incorrect❌")

# ----------------------------Lesson3-----------------
print("--------------------LESSON 3---------------")
def sum_scores(*scores):
    """Sum ANY Number of scores"""
    score_list = []
    for score in scores:
        score_list.append(score)
    total = sum(score_list)
    return total

# result1 = sum_scores(10,20,30)
# result1 = sum_scores(10,20,30, 55, 68)
testCase1 = sum_scores(10,20,30)
testCase2 = sum_scores(10,20,30, 55, 68)
# print(testCase1)
# print(testCase2)

#corrections
if testCase1 == 60:
    print("correct!✅")
else:
    print("incorrect❌")
if testCase2 == 183:
    print("correct!✅")
else:
    print("incorrect❌")


#**KWARGS


def make_notification(user, *messages, urgent=False):
    notification = f"user: {user}"
    if urgent:
        notification += " URGENT - "
        notification += " ".join(messages)
        
    return notification

# print(make_notification("admin","Server down!", urgent=True))
# print(make_notification("user","Welcome","Check inbox"))

testCase1 = make_notification("admin","Server down!", urgent=True)
testCase2 = make_notification("user","Welcome","Check inbox")

if testCase1 == "user: admin URGENT - Server down!":
    print("correct!✅")
else:
    print("incorrect❌")
if testCase2 == "user: user":
    print("correct!✅")
else:
    print("incorrect❌")

#------------------------Lesson4-------------------
print("--------------------LESSON 4---------------")
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

if result == False:
    print("correct!✅")
else:
    print("incorrect❌")
if message == "Invalid characters":
    print("correct!✅")
else:
    print("incorrect❌")
if success == False:
    print("correct!✅")
else:
    print("incorrect❌")
    
    
#------------------------Lesson4-------------------
print("--------------------LESSON 5---------------")

