name = None
health = None
dodge = None
attack = None
speech = None
charisma = None
exp = None
money = None


def create_character(character_name, character_class):
    global name, health, dodge, attack, speech, charisma, exp, money
    name = character_name
    health = 100
    exp = 0
    money = 0
    if character_class == 'soldier':
        dodge = 3
        attack = 10
        speech = 1
        charisma = 3
    elif character_class == 'engineer':
        dodge = 1
        attack = 3
        speech = 8
        charisma = 4
    elif character_class == 'adept':
        dodge = 7
        attack = 5
        speech = 2
        charisma = 1
    else:
        pass
