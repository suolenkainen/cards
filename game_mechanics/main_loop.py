"""
The tkinker calls this function every few seconds to run the game.
"""

import setup, phases, copy, random, operator
import abilities as ab

def reset_game(players):
    # Create players

    for i in range(2):
        player = players[i]
        player.hand = []
        player.table = []
        player.manapool = []
        player.strategy = None
        player.graveyard = []
        player.health = 100
        player.hand_size = 5
        player.next_draw_amount = 5
        player.actions = []
        player.draw_deck = None
        player.draw_deck = setup.create_draw_deck()
        player.draw_deck.id = 0
        player.draw_deck.deck_owner = ""
        player.draw_deck.deck_purpose = "draw deck"
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
    
    return players



def game(players):
    player = players[0]
    
    # Player phases
    phases.untap_phase(player)

    # Sort hand for the cards in player hand based on the propability them being 
    player.hand = sorted(player.hand, reverse=True, key=operator.attrgetter("priority"))

    play_cards(players)

    phases.action(players)

    phases.discard_phase(player)

    phases.draw_cards(player)

    # Switch order. After player 1 has played, turn counter rises by one.
    players.append(players.pop(0))

     


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

                # Check if there is an interrupt to be played by the opponent
                interrupt, cancel = opponent_interrupt(players, card)
                if interrupt:
                    if cancel:
                        continue
                temp_hand.remove(card)
                player.manapool = temp_pool
                print("Plays enchantment", card.name)
                continue
            
            if opponent_interrupt(players, card):
                pass
            card.tapped = True
            player.table.append(card)
            temp_hand.remove(card)
            player.manapool = temp_pool
            print("Plays card", card.name)
    player.hand = temp_hand



def opponent_interrupt(players, card, **kwargs):
    # receive opponent card that was played

    ## Create counter ability first
    if any("interrupt" in card.keywords for card in players[1].hand):
        for interrupt_card in players[1].hand:
            if "interrupt" in interrupt_card.keywords:
                break
        
        # UGLY IMPLEMENTATION
        ab.call_abilities(interrupt_card, players, played_card=card, interrupt_card=interrupt_card)
        #remove played interrupt
        print("JIIHAA")
    
        cancel_play()

    return False, False

def cancel_play():
    pass

if __name__ == "__main__":
    setup_mock_game()