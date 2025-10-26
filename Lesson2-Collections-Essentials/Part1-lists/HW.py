#problem 1:
def remove_duplicate(items):
    new_list = []
    for i in range(0,len(items)):
        if items[i] != items[i-1]:
            new_list.append(items[i]) 
    return new_list
print(remove_duplicate([1,2,2,3,4,5]))
#problem 2:
def find_common(list1, list2):
    common = []
    for char in list1:
        if char in list2 and char not in common:
            common.append(char)
    return common
print(find_common([1,2,4, 4], [4,2, 1]))
#problem 3:
def reverse_sublists(data, size):
    list = []
    for i in range(0, len(data), size):
        chunk = data[i:i+size]
        list.extend(chunk[::-1])
    return list
print(reverse_sublists([1, 2, 3, 4, 5, 6], 2))
# problem 4
def rotate_list(items, positions):
    if not items:
        return items

    n = len(items)
    positions = positions % n  
    return items[-positions:] + items[:-positions]

# You need to print the result to see it:
print(rotate_list([1, 2, 3, 4, 5], 2))