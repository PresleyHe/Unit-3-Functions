def format_phone_number(phone):
    # phone.replace(" ", "").replace("-", "").replace("()", "")
    phoney = phone.replace(" ", "").replace("-", "").replace("()", "")
    area = phoney[:3]
    middle = phoney[3:6]
    last = phoney[6:]
    if len(phoney) == 10 and phoney.isdigit():
        return f"({area}) {middle}-{last}"
    else: 
       return "Invalid"
   
print(format_phone_number("555-123-4567"))

# problem 2
def sanitize_filename(filename):
    clean_Fileneame = filename.lower().replace(" ", "_")
    special = "._-"
    for char in clean_Fileneame:
        if not char.isdigit():
            if not char.isalpha():
                if not char in special:
                    clean_Fileneame = clean_Fileneame.replace(char, "")
        if not clean_Fileneame[-4:] == ".text":
            clean_Fileneame += ".txt"
        if len(clean_Fileneame) > 50:
            return "character maximum exceeded(50 character max)!"
        return clean_Fileneame
    
print(sanitize_filename("notes"))