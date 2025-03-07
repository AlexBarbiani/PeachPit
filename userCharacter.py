# this module houses classes/functions related to the player's character
import json
import os

class UserCharacter:
    def __init__(self, char_class:str ="Druid", level:int=1, exp:int=0):
        self._char_class = char_class
        self._level = level
        self.exp = exp

    def to_dict(self):
        return {"char_class": self._char_class, "level": self._level, "exp": self.exp}

    @classmethod
    def from_dict(cls, data):
        return cls(data["char_class"], data["level"], data["exp"])

    def __str__(self):
        return f" Character class: {self._char_class} \n Character Level: {self._level} \n Total character exp: {self.exp} \n"

    def add_exp(self, incoming_exp):
        self.exp += incoming_exp
        while self.exp >= 100:
            self.exp -= 100
            self._level += 1
            print(f"You levelled up! You have reached level {self._level}!")
        save_character(character, character_filename)


# test adding exp and levelling up
"""test_character = UserCharacter()  
print(test_character)
test_character.add_exp(850)
print(test_character)"""


character_filename = "character.json"

def initialize_character():
    global character
    character = load_character()
    if character is None:
        character = UserCharacter()
        save_character(character, character_filename)


def print_user_character():
    print(character)

def load_character(filename="character.json"):
    if not os.path.exists(filename):
        return None  # raise an exception?
    with open(filename, "r") as file:
        data = json.load(file)
        return UserCharacter.from_dict(data)
    file.close()


def save_character(character, filename="character.json"):
    with open(filename, "w") as file:
        json.dump(character.to_dict(), file, indent=4)
    file.close()
