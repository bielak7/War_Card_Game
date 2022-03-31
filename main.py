from Card import Card

__name__ == "__main__"
# Card = Card()

two_of_clubs = Card('Clubs', 'Two')
three_of_clubs = Card('Clubs', 'Three')

print(two_of_clubs.value < three_of_clubs.value)