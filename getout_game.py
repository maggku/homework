import json

with open("getout_game.json", "r") as f:
    scenes = json.load(f)

print(scenes)
