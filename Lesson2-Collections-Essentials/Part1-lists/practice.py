# def filter_events(numbers):
#     result = []
#     for num in numbers:
#         if num % 2 == 0:
#             result.append(num)
#     return result
# print(filter_events([1,2,3,4,5,6]))


def lists_stats(numbers):
    if not numbers:
        return None
    minimum = min(numbers)
    maximum = max(numbers)
    avg = sum(numbers) / len(numbers)
    return minimum, maximum, avg
print(lists_stats([10,20,30,40])) 