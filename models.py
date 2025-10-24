"""
For the Paragraph class:

Think about what attributes you need: id, content (treść), and choices (opcje wyboru)
For the choices, consider using a dictionary where keys might be the text shown to the player and values are the IDs of paragraphs they lead to
The play() method should use print() to display things nicely - maybe number the choices like "1. Go left", "2. Go right"
To create a Paragraph from data (like from JSON), think about using the __init__ method with parameters, or maybe a @classmethod that takes a dictionary

"""
import json


class Paragraph:
    def __init__(self, id, text, choices):
        self.id = id
        self.text = text
        self.choices = choices


    def play(self):
        print(self.text)
        for choice in self.choices:
            print(" - ", choice)


class Hero:
    def __init__(self, name, current_paragraph):
        self.name = name
        self.current_paragraph = current_paragraph


    def save(self):
        try:
            with open("getout_save_game.json", "r") as file:
                all_heroes = json.load(file)
        except FileNotFoundError:
            all_heroes = {}

        all_heroes[self.name] = {
            "current_paragraph": self.current_paragraph
        }


        with open("getout_save_game.json", "w") as file:
            json.dump(all_heroes, file)

    @classmethod
    def load(cls, name):
        try:
            with open("getout_save_game.json", "r" ) as file:
                all_heroes = json.load(file)
        except FileNotFoundError:
            print("No saved games found")



        if name in all_heroes:
            return all_heroes[name]["current_paragraph"]
        else:
            print("Create your hero")


#







