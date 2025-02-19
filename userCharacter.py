class userCharacter:
    def __init__(char, charClass = 'Druid', level = 1, exp = 0):
        char.charClass = charClass
        char.level = level
        char.exp = exp
    
    def __str__(char):
        return f" Character class: {char.charClass} \n Character Level: {char.level} \n Total character exp: {char.exp}"