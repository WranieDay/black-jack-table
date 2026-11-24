from card_moves import card_value, starting_hand, dlr_starting_hand

#hitting function for player 
def hit(player_hand):
    suit = random.choice(card_deck)
    pulled_card = random.choice(suit)
    player_hand.append(pulled_card)
    return player_hand

def stand(player_hand):
    return player_hand
