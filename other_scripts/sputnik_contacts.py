import json

with open('sputnik.json', 'r') as f:
    contacts = f.read()
    a = json.load(contacts)