"""
This describes the different phases in game
"""

import abilities as ab

def untap_phase(player):
    print(player.name)
    player.manapool = []
    for card in player.table:
        if card.tapped:
            card.tapped = False
            if card.type == "monster":
                player.actions.append(card)
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


def action(players):
    player = players[0]
    # scroll through the actions list and check for any possible actions
    for card in player.actions:
        if card.abilities:
            ab.call_abilities(card, players)
        if card.type == "monster":
            attack(card, players)
            player.actions.remove(card)


def enchantment_validity(players):
    # Todo: When attack is OK, make this
    return True


def attack(monster, players):
    player = players[0]
    opponent = players[1]

    opponent_blockers = []
    for opp_card in opponent.table:
        if opp_card.type == "monster":
            if "blocker" in monster.keywords:
                return
            if opp_card.tapped == False:
                opponent_blockers.append(opp_card)
    if opponent_blockers == []:
        opponent.health -= int(monster.attack)
        print(monster.name, "attacked", opponent.name, "reducing its health to", opponent.health)
        monster.tapped = True
        return
    
    attacker_HP = int(monster.defence)
    while opponent_blockers != [] or attacker_HP <= 0:
        blocker = opponent_blockers.pop()
        blocker_HP = int(blocker.defence)
        blocker_HP -= int(monster.attack)
        if blocker_HP <= 0:
            opponent.graveyard.append(blocker)
            opponent.table.remove(blocker)
            if blocker in opponent.actions:
                opponent.actions.remove(blocker)
            monster.tapped = True
            print(monster.name, "attacked", blocker.name, "destroying it")
            return
        else:
            attacker_HP -= int(blocker.attack)
            print(monster.name, "was attacked by", blocker.name, "destroying it", "destroying it")
        if attacker_HP <= 0:
            player.graveyard.append(monster)
            player.table.remove(monster)
