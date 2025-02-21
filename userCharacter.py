class userCharacter:
    def __init__(self, charClass = 'Druid', level = 1, exp = 0):
        self.charClass = charClass
        self.level = level
        self.exp = exp
    
    def __str__(self):
        return f" Character class: {self.charClass} \n Character Level: {self.level} \n Total character exp: {self.exp}"