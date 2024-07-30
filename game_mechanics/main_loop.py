import setup, phases, copy, operator
import abilities as ab




def game(players):
    # Play one round of game with the different phases
    player = players[0]
    
    # Player phases
    phases.untap_phase(player)

    # Sort hand for the cards in player hand based on the propability them being 
    player.hand = sorted(player.hand, reverse=True, key=operator.attrgetter("priority"))

    # Play cards from hand based on priority
    play_cards(players)

    # Play out actions set in the untap phase 
    phases.action(players)

    # Discard cards to be able to draw new cards each turn
    phases.discard_phase(player)

    # Draw cards to the maximum of hand limit
    phases.draw_cards(player)

    # Switch order. After player 1 has played, turn counter rises by one.
    players.append(players.pop(0))

     


def play_cards(players):
    # Play cards from hand to table or as enchantments
    # This function is quite difficult to understand and requires refactoring
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
    # Placeholder for interrupting playing a card
    pass



if __name__ == "__main__":
    setup.setup_mock_game()