# Q 3:
def get_phone_number(contacts, name):
    try:
        return contacts[name]
    except KeyError:
        return "contact not found"
# Q 4:
def get_song(playlist, position):
    try:
        return playlist[position]
    except IndentationError:
        return "Position out of range"
    except TypeError:
        return "Position must be an integer"
# Q 5:
def calculate_test_average(scores):
    try:
        avg = sum(scores) / len(scores)
        return round(avg, 2)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "Invalid score data"