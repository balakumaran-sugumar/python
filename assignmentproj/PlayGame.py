from assignmentproj.Deck import Deck
from assignmentproj.Player import Player

deck = Deck()
deck.shuffle()

player1 = Player("Computer1")
player2 = Player("Computer2")

for number in range(26):
    player1.cards_held.append(deck.deal_one())
    player2.cards_held.append(deck.deal_one())

num_rounds = 0
war_count = 0

round_begins = True

while round_begins:

    num_rounds += 1
    print(f"Round {num_rounds} Player1 has {len(player1.cards_held)} Player2 has {len(player2.cards_held)}")

    if len(player1.cards_held) == 0:
        print("Player 2 WINS !")
        break
    elif len(player2.cards_held) == 0:
        print("Player 1 WINS !")
        break

    player_one_card = [player1.remove_one()]

    player_two_card = [player2.remove_one()]

    at_war = True

    while at_war:

        if len(player1.cards_held) < 5:
            print("Player2 WINS")
            round_begins = False
            break
        if len(player2.cards_held) < 5:
            print("Player1 WINS")
            round_begins = False
            break

        if player_one_card[-1].value > player_two_card[-1].value:
            player1.add_card(player_one_card)
            player2.add_card(player_two_card)
            at_war = False
        elif player_one_card[-1].value < player_two_card[-1].value:
            player2.add_card(player_one_card)
            player2.add_card(player_two_card)
            at_war = False
        else:
            for num in range(5):
                player_one_card.append(player1.remove_one())
                player_two_card.append(player2.remove_one())
