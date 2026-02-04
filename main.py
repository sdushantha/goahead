import json
import requests

r = requests.get("https://api.gan.no/api/traffic-app/situations")
situations = r.json()

try:
    with open("history.json", "r") as f:
        history = json.load(f)
except FileNotFoundError:
    history = {}

old_keys  = set(history.keys())

for situation in situations:
    situation_id = situation.pop("situationId")
    history[situation_id] = situation

with open("history.json", "w") as f:
    json.dump(history, f, indent=2)

