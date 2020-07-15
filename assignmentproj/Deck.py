# add all the cards to the deck, the deck should have 52 cards in all
import random

from assignmentproj.Card import Card, suites, ranks


class Deck:
    card_deck = []

    # create combination of 52 cards and add it to the deck
    def __init__(self):
        for suite in suites:
            for rank in ranks:
                created_card = Card(suite, rank)
                self.card_deck.append(created_card)

    def __repr__(self):
        return '{card:' + self.card_deck + '}'

    def shuffle(self):
        random.shuffle(self.card_deck)

    def deal_one(self):
        return self.card_deck.pop()
