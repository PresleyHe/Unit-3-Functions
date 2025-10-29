# Q1:

#normalized would convert email to all 
# lower case. username would split on "@" and gets the characters after the "@"
# username would be "@gmail.com". domain would be splitting username at the "@" and starts after the "@"
# It would print john.smith gmail.com

# Q2:
# words would split the text into ["The", "Quick", "Brown", "Fox"]
# the for loop would iterate through each character in words and add them to initials as lowercase from index 0 of words
# It would print tqbf

# Q3:
def extract_domain(email):
    atA = email.count("@")
    if atA != 1:
        return "invalid email"
    parts = email.lower().split("@")
    domain = parts[1]
    return domain

# Q4:
# The digits would be a empty string
# The for loop would iterate for every character in message and add a digit to the digits
# if the character is a digit then it adds it to the empty string digits
# it would print 123456

#Q5:
#  filename would be "my-document.txt"
# the name_only would replace the ".txt" with nothing
# safe_name would be filename replacing the - with a _
# The result would be safe_name in all capital case
# it would print MY_DOCUMENT

#Q6:
# items would split each item in data to a list ["apple", "banana", "cherry", "date"]
# longest would be the item of index 0 of items
# the for loop would iterate for if the length of item is greater than longest
# if so then longest would be assigned the value of item
# it should print banana

#Q7:
def filter_numbers(text):
    result = ""
    for char in text:
        if not char.isdigit():
            result += char
    return result

#Q8:
#parts would be url split into a list ["https:", "", "example.com", "users", "profile"]
# protocol would index 0 of parts which is "https:"
# domain is index 2o f parts which is "example.com"
# path would be "/" jointed with parts of slice from 3 to the end
#  it would print https://example.com/users/profile
 
#  Q9
def count_character_types(text):
    letters = 0
    digits = 0
    spaces = 0
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char == " ":
            spaces += 1
    return {"letters": letters, "digits": digits, "spaces": spaces}
            