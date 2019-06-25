import json

with open("OWLmatches.json", "r") as read_file:
    data = json.load(read_file)
    
print(data)