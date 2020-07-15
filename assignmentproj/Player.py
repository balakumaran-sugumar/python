# this is for assigning the players with cards and name


class Player:

    def __init__(self, name):
        self.name = name
        self.cards_held = []

    def __str__(self):
        return "Player " + self.name + " holds " + str(len(self.cards_held))

    def remove_one(self):
        return self.cards_held.pop(0)

    def add_card(self, card):
        self.cards_held.extend(card)
