# try:
#     # Try something risky
#     score = int(input("Enter score: "))
# except:
#     # Runs if it Failed
#     print("Invalid score!")
# else:
#     # Runs if it succeeded
#     print(f"✅Valid score entered: {score}")
    


def parse_command(message):
    """Parse a Discord command like: !ban PlayerName 7days"""
    try:
        parts = message.split() #["!ban", "PLayerName", "7days"]
        command = parts[0] #"!ban"
        target = parts[1] #"PlayerName"
        duration = parts[2] #"7days"
    except IndexError:
        print("❌Invalid command format-missing parts!")
        return None
    else:
        print("✅Command parse successfully!")
        if command.startswith("!"):
            print(f"⚡Executing: {command}")
        return command, target, duration
    finally: #Runs no matter what
        print("This block runs regardless")
result = parse_command("!ban PlayerName 7days")
print(result)
result2 = parse_command("!ban")
print(result2)