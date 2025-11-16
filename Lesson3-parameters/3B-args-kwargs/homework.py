# Q1:

def combine_values(*values):
    total = 1
    if not values:
        return total
    for value in values:
        total *= value
    return total
        
print(combine_values(2, 3, 4))
print(combine_values(5))
print(combine_values())

# Q2:
def merge_details(label, **description):
    details = {"label": label}
    details.update(description)
    return details

print(merge_details("ItemA", size="Large", cost=12.50))
# → {"label": "ItemA", "size": "Large", "cost": 12.50}

print(merge_details("UserX"))
# → {"label": "UserX"}

# Q3:
# 1. total = v(3) * rate(2) + v(1) * rate(2) = 8
# Rate wasn't specified so it was kept at the default value of 2.d
# 2. total = v(2) * rate(5) = 10
# Rate was specified as 5
# 3. 0
# Nothing was assigned a value so it returned 0

# Q4:
# 1. {"name": "Alpha", "x=1", "y=2", count: 2}
# it prints the name and updates record with **info and then adds in "count" to count how many items are in **info which is 2 --> "x=1", "y=2"
# 2. {"name": "Beta", count: 0}
# It prints the name, but since **info is empty, it still adds the "count" but its zero since theres nothing