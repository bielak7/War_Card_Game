import random
from Class.Card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Deck:

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


new_deck = Deck()
first_card = new_deck.all_cards[1]
print(first_card)