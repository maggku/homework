import json

with open("getout_game.json", "r") as f:
    scenes = json.load(f)

print(scenes)

scene_dict = {scene["id"]: scene for scene in scenes}

current_id = "start"

while True:
    scene = scene_dict[current_id]

    print(scene["text"])

    if not scene["choices"]:
        print("*** THE END ***")
        break

    print("Choices:")
    for choice in scene["choices"]:
        print("-", choice)

    player_choice = input("What do you do? ")

    if player_choice not in scene["choices"]:
        print("Invalid choice. Try again.")
        continue

    current_id = scene["choices"][player_choice]


