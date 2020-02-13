class Item:
    def __init__(self, name, attack, armor):
        self.name = name
        self.attack = attack
        self.armor = armor

    def __str__(self):
        return f'Item: {self.name}\n Attack: {self.attack} \n Armor: {self.armor}'
