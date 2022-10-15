import random

SUITES=["♠","\033[91m♥\033[0m","\033[92m♣\033[0m","\033[94m♦\033[0m"]
RANKS = ['A','2','3','4','5','6','7','8','9','X','J','Q','K']
VALUES = [11,2,3,4,5,6,7,8,9,10,10,10,10]

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[RANKS.index(rank)]

    def __str__(self):
        return ('┌───────┐\n│{0}      │\n│{1}      │\n│       │\n│       │\n│      {1}│\n│      {0}│\n└───────┘\n'.format(self.rank, self.suit))

class Deck(list):

    def __init__(self):
        self.add_cards()

    def add_cards(self):
        for s in SUITES:
            for r in RANKS:
                self.append(Card(s, r))

    def __str__(self):
        result = ""
        for card in self:
            result = result + str(card)
        return result

    def shuffle(self):
        random.shuffle(self)

    def deal(self):
        return self.pop()

class Hand(Deck):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_cards(self):
        print("No cards added")

    def __str__(self):
        return self.name + "\n" + super().__str__()

deck = Deck()
deck.shuffle()
player1 = Hand("Thomas")
player2 = Hand("Shan")
for i in range(4):
    player1.append(deck.deal())
    player2.append(deck.deal())

print(player1)
print(player2)