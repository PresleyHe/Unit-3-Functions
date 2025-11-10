# Q1:
#  2300

# Q2:
#  "WOW WOW LFG"

# Q3:
donations = {
    "neon":250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

def find_top_donor(donations):
    top_name = ""
    top_amount = -1
    for name, amount in donations.items():
        if amount > top_amount:
            top_amount = amount
            top_name = name
    return top_name

print(find_top_donor(donations))