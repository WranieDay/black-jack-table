import random

#making deck of cards
Hearts = ['2 ♡', '3 ♡', '4 ♡', '5 ♡', '6 ♡', '7 ♡', '8 ♡', '9 ♡', '10 ♡', 'J ♡', 'Q ♡', 'K ♡', 'A ♡']
Spades = ['2 ♠', '3 ♠', '4 ♠', '5 ♠', '6 ♠', '7 ♠', '8 ♠', '9 ♠', '10 ♠', 'J ♠', 'Q ♠', 'K ♠', 'A ♠']
Dimonds = ['2 ♦', '3 ♦', '4 ♦', '5 ♦', '6 ♦', '7 ♦', '8 ♦', '9 ♦', '10 ♦', 'J ♦', 'Q ♦', 'K ♦', 'A ♦']
Clubs = ['2 ♣', '3 ♣', '4 ♣', '5 ♣', '6 ♣', '7 ♣', '8 ♣', '9 ♣', '10 ♣', 'J ♣', 'Q ♣', 'K ♣', 'A ♣']

card_deck = [Hearts, Spades, Dimonds, Clubs]
#setting value of each card
rank_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11 or 1}

def card_value(card):
    rank = card.split()[0]
    return rank_values[rank]

def deck_values(card_deck):
    return [[card_value(card) for card in suit] for suit in card_deck]

#pulling 2 random cards for player and dealer

def starting_hand():
    plr_starting_hand = []
    for pulls in range(2):
        suit = random.choice(card_deck)
        pulled_card = random.choice(suit)
        plr_starting_hand.append(pulled_card)
    return plr_starting_hand
plr_starting_hand = starting_hand()
print('Your hand:', ', '.join(plr_starting_hand))

def dlr_starting_hand():
    d_starting_hand = []
    for pulls in range(2):
        suit = random.choice(card_deck)
        pulled_card = random.choice(suit)
        d_starting_hand.append(pulled_card)
    return d_starting_hand
d_starting_hand = dlr_starting_hand()
print('Dealer hand:', ', '.join(d_starting_hand))