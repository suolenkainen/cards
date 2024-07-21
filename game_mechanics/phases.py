"""
This describes the different phases in game
"""


def untap_phase(player):
    print(player.name)
    player.manapool = []
    for card in player.table:
        if card.tapped:
            card.tapped = False
        if not card.tapped and card.type == "mana":
            player.manapool.append(card.color)

def sort_hand(player):
    # arrange cards in priority play order
    temp_hand = []
    priority = 4
    while True:
        for i, card in enumerate(player.hand):
            if card.priority > priority:
                temp_hand.append(player.hand.pop(i))
        priority -= 1
        if len(player.hand) == 0: 
            player.hand = temp_hand
            break


def discard_phase(player):
    while len(player.hand) >= player.hand_size:
        player.graveyard.append(player.hand.pop())
    player.next_draw_amount = 1


def draw_cards(player):
    while player.next_draw_amount > 0 or len(player.hand) < player.hand_size:
        player.hand.append(player.draw_deck.cards.pop(0))
        player.next_draw_amount -= 1