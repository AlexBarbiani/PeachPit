#this module houses classes/functions related to the player's character

class UserCharacter:
    def __init__(self, char_class = 'Druid', level = 1, exp = 0):
        self.char_class = char_class
        self.level = level
        self.exp = exp
    
    def __str__(self):
        return f" Character class: {self.char_class} \n Character Level: {self.level} \n Total character exp: {self.exp} \n"
    
    def add_exp(self, incoming_exp):
        self.exp += incoming_exp 
        while self.exp >= 100:    
            self.exp -= 100       
            self.level += 1

'''test_character = UserCharacter()  
print(test_character)
test_character.add_exp(850)
print(test_character)'''
    
    
    