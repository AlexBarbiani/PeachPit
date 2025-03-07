# this module houses random inspirational or video-game related quotes, to be selected and displayed in the application
import random

quote_list = [
    "If I have seen higher, it is by standing on the shoulders of giants.",
    "な問 がない !",
    "Most people are waiting to be told what to do. Are you one of those people?",
    "We're all gonna make it.",
    "A ship is safest in port... but that is not what a ship is for.",
    "We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields and in the streets... We shall never surrender!",
    "I ask not for lighter burdens, but for broader shoulders.",
    "Waste no more time arguing what a good man should be. Be one.",
    "Man cannot remake himself without suffering, for he is both the marble and the sculptor.",
    "I should have been the one to fill your dark soul with light!",
    "Handle it!",
    "Oh my God, he just ran in.",
]


def quote_picker():
    x = 0
    for quote in quote_list:
        x += 1

    chosen_quote = random.randint(0, x - 1)
    print(f'\n{quote_list[chosen_quote]}\n')
