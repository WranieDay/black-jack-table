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

