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