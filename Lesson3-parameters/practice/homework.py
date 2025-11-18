# Q1:
def process_order(customer, *items, discount=0.0, **options):
    total = len(items) * 10 #each item costs 10(multiplies amount by 10)
    total -= total * discount #takes the total and subtracts it with the discount
    if options.get("express"):#If it contains express with a value of true,
        total += 5 #then it adds 5 to the total
    return round(total, 2) #rounds to 2 decimal places
# 18.0
# 15.0

# Q2:
def make_notification(user, *messages, urgent=False):
    notification = f"user: {user}"
    if urgent:
        notification += " URGENT - "
        notification += " ".join(messages)
        
    return notification

print(make_notification("admin","Server down!", urgent=True))
print(make_notification("user","Welcome","Check inbox"))

# Q3:
def build_query(table, *fields, where="", limit=10):
    field_str = ", ".join(fields) if fields else "*"#Takes the field and if there isn't adds a "*"
    query = f"SELECT {field_str} FROM {table}" #It adds the field_str into it wit SELECT *fields FROM table
    if where:
        query += f" WHERE {where}" #adds what they entered for where or just ""
    if limit:
        query += f" LIMIT {limit}"#adds what they enters for limit or it will be by default limit = 10
    return query

print(build_query("users","name","email")) #SELECT name, email FROM users LIMIT 10
print(build_query("logs", where="level='error'", limit=5))#SELECT * FROM logs WHERE level='error' LIMIT 5

# Q4:
def log_action(actor, *actions, timestamp=None, **context):
    action = f"{actor}: " +  ", ".join(actions)
    if context:
        ctx = ", ".join(f"{k}={v}" for k, v in context.items())
        action += " | " + ctx

    return action
print(log_action("bot","login","scan", source="API", ip="1.2.3.4"))