import random
from enemy import Enemy

# Enemy(name, hp, attack, defense)

slime = Enemy('Slime', 10, 2, 0)
kobold = Enemy('Kobold', 20, 3, 5)

def get_random_enemy():
    chance = random.randint(0, 1)

    if chance == 0:
        return slime
    elif chance == 1:
        return kobold
    else:
        return slime
