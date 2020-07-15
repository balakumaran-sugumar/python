# this is the classic game that who ever has the highest card will win the game and once all the cards are exhausted
# the player who has the highest number of cards wins the game
# declaring global values variable about card assignment
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 6, "9": 9, "10": 10,
          "J": 11, "Q": 12, "K": 13, "A": 14}

suites = ("❤", "♠", "♦", "♣")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")


class Card:

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        capitalized_value = rank.capitalize()
        self.value = values[capitalized_value]

    def __str__(self):
        return self.rank + " " + self.suite
