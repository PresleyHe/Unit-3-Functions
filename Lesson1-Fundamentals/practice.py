# def calculate_discount(price, member_status):
#     if member_status == "premium":
#        return price * 0.7
#     elif member_status == "standard":
#        return price * 0.85
#     elif member_status == "guest":
#        return price * 1
# print(calculate_discount(100, "premium"))
# print(calculate_discount(100, "standard"))
# print(calculate_discount(100, "guest"))


# def count_vowels(text):
#     vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
#     count = 0
#     for char in text:
#         if char in vowels:
#             count+=1
#     return count
# print(count_vowels("Hello World"))


def validate_password(password):
    valid = False
    digit = False
    if len(password) >= 8:
        valid = True
    for char in password:
        if "0" <= char <= "9":
            valid=True
            break
    return valid
print(validate_password("16"))