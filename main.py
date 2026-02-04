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

if new_situation_ids := set(history.keys()) - old_keys:
    for situation_id in new_situation_ids:
        summary = history[situation_id]["messageSummary"]["no"]
        print(f"{situation_id} | {summary}")

with open("history.json", "w") as f:
    json.dump(history, f, indent=2)

