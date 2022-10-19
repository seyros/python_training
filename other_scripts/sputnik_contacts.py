import json

with open('data/sputnik.json', 'r') as f:
    contacts = f.read()
    a = json.load(contacts)