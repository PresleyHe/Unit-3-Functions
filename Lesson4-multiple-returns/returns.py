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