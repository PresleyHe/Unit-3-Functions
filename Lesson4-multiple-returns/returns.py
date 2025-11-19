def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)

#1 Return Type - None - "No Value"
# Meaning: Absense of value, not set, not found
# Use for: Missing Data, search failures, optional parameters
result = None
print(result is None) # True - identify check
print(result == None) # - equality check
print(not result) #True - falsy check

# 2 Return type - False = Boolean False
#Meaning: Explicit false conditions, validation failure, negative result
# Use for:  result, boolean operations, sucessfailure status
print(result == 0) #True - falsy check

# 3 Return zero - A Valid Number
# ZERO is VALID numberic value, not absense of value!
result = 0
print(result == 0) #True - numberic equality
print(not result) #True - (falsy in boolean context
print(result is None) # False - different objects
print(result is False) #False - different types

# Multiple returns - python packs multiple returns into a tuple!
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

result = calculate_room(10, 5)
print(result)
print(type(result))
print(type((42)))#Int
print(type((42,)))# Tuple for a single item
no_parathentheses = 1, 2, 3
print(type(no_parathentheses))


# Unpacking tuple
area_result, perimeter_result = calculate_room(20,6)
print(f"Area: {area_result}")
print(f"perimeter: {perimeter_result}")

def analyze_grades(grades):
    if not grades:
        return 0,0,0,False
    passfail = True
    minimum = min(grades)
    maximum = max(grades)
    avg = sum(grades) / len(grades)
    if avg <= 60:
        passfail = False
    return maximum, avg, minimum, passfail

print(analyze_grades([85, 92, 78, 90]))
print(analyze_grades([]))
print(analyze_grades([80, 80, 80]))