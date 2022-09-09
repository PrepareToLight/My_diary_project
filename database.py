import datetime

entries = []

def add_entries(text):
    current_time = datetime.datetime.now()
    data = {"content": text, "date": str(current_time)}
    entries.append(data) 

def view_entries():
    return entries


print(datetime.datetime.now())