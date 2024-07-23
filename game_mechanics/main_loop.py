"""
The tkinker calls this function every few seconds to run the game.
"""

import setup
import phases
import copy
import random

def setup_mock_game():
    # Create players
    players = []
    for i in range(2):
        player = setup.player_object()
        player.id = i
        player.name = "player "+str(i)
        random.seed(player.id)
        random.shuffle(player.draw_deck.cards)
        zero_mana = True
        while zero_mana:
            player.hand = setup.draw_start_hand(player.draw_deck)
            for card in player.hand:
                if card.type == "mana":
                    zero_mana = False
                    break
            if zero_mana:
                for i in range(5):
                    player.graveyard.append(player.hand.pop(0))

        players.append(player)
    
    players.append(0)
    players.append(1)

    return players


def turn_order(players):
    # Identify, who is the player and who is opponent
    player = players[0]
    opponent = players[1]

    # Switch order. After player 1 has played, turn counter rises by one.
    if players[2] == 0:
        players[2] == 1
    else: 
        players[2] = 0
        players[3] += 1
    players[0] = opponent
    players[1] = player

    return players


def game(players):
    player = players[0]
    
    # Player phases
    phases.untap_phase(player)

    phases.sort_hand(player)

    play_cards(players)

    phases.action(players)

    phases.discard_phase(player)

    phases.draw_cards(player)

    return turn_order(players)
     

def play_cards(players):
    player = players[0]
    has_played_mana = False
    
    temp_hand = copy.copy(player.hand)
    for card in player.hand:
        temp_pool = copy.copy(player.manapool)
        temp_pool = copy.copy(player.manapool)
        temp_cost = copy.copy(card.cost)
        if card.type == "mana":
            if not has_played_mana:
                card.tapped = True
                player.table.append(card)
                has_played_mana = True
                temp_hand.remove(card)
                player.manapool = temp_pool
                print("Plays card", card.name)
                continue
            else:
                continue
        for cost_mana in card.cost:
            if cost_mana in temp_pool:
                temp_pool.remove(cost_mana)
                temp_cost.remove(cost_mana)
            elif cost_mana == "any" and temp_pool != []:
                temp_pool.pop(0)
                temp_cost.pop(0)
            else:
                break

        if temp_cost == []:
            if card.type == "enchantment" and phases.enchantment_validity(players):
                if opponent_interrupt():
                    pass
                temp_hand.remove(card)
                player.manapool = temp_pool
                print("Plays enchantment", card.name)
                continue
            
            if opponent_interrupt():
                pass
            card.tapped = True
            player.table.append(card)
            temp_hand.remove(card)
            player.manapool = temp_pool
            print("Plays card", card.name)
    player.hand = temp_hand


def opponent_interrupt():
    return False



if __name__ == "__main__":
    setup_mock_game()