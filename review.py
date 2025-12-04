# Q18:
def  validate_password(password):
    if not password:
        return False, "Empty Password!"
    if len(password) < 8:
        return False, "Too short"
    return True, "Valid"

print(validate_password(""))
print(validate_password("abc"))
print(validate_password("secure123"))
    
    
# Q19:
def create_inventory(item_name, *quantities, location = "Warehouse"):
    return {
        "item name": item_name,
        "quantity": sum(quantities),
        "location": location
    }
print(create_inventory("Widget", 10, 20, 15))

# Q20:
def safe_list_access(item, index):
    try: 
        # if index < len(item):
        #     return item[index], True
        value = item[index]
        return value
    except IndexError:
        return None, False
    
print(safe_list_access([10,20,30], 1))
print(safe_list_access([10,20,30], 10))