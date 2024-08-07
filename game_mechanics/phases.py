from abilities import call_abilities

def untap_phase(player):
    # Untap all the tapped cards on the table
    # This also resets the manapool and recreates it based on the mana cards the player has
    player.manapool = []
    for card in player.table:
        if card.tapped:
            card.tapped = False
            if card.type == "monster":
                player.actions.append(card)
        if not card.tapped and card.type == "mana":
            player.manapool.append(card.color)



def discard_phase(player):
    # player discards cards from hand in a way that it is one less than the hand limit.
    # If the hand size is already less than hand size, they won't discard
    # The discarding allows rotation of cards in hand to not be stuck with a handful of bad cards
    while len(player.hand) >= player.hand_size:
        player.graveyard.append(player.hand.pop())
    player.next_draw_amount = 1



def draw_cards(player):
    # Draw cards to hand so that it is either to the amount of hand size or specifically determined amount
    while player.next_draw_amount > 0 or len(player.hand) < player.hand_size:
        if len(player.draw_deck.cards) >= 1:
            player.hand.append(player.draw_deck.cards.pop(0))
            player.next_draw_amount -= 1
        else:
            break



def action(players):
    # Check if the player has action pending and go through them 
    player = players[0]

    for card in player.actions:
        if card.abilities:
            # Check and play all abilities the action might have
            call_abilities(card, players)
        if card.type == "monster":
            # Check and play all attacks a monster might have
            attack(card, players)

    # Remove cards that have performed an action
    player.actions = []



def enchantment_validity(players):
    # Todo: When attack is OK, make this
    return True



def attack(monster, players):
    # The monsters that are set to make actions calcultate their attacks based on rules
    player = players[0]
    opponent = players[1]
    opponent_blockers = []

    # If attacker is a blocker, it will not attack but wait for the opportunity to block
    if "blocker" in monster.keywords:
        return
    
    # Add all monster cands to potential blockers
    for opp_card in opponent.table:
        if opp_card.type == "monster":
            if opp_card.tapped == False:
                opponent_blockers.append(opp_card)
    
    # If there are no blocking monsters, the attacker causes damage directly to the opponent player
    if opponent_blockers == []:
        opponent.health -= monster.attack
        monster.tapped = True
        return
    
    # If there are blockers, the attacker and blocker attack at the same time, unless "first strike" ability dictates otherwise
    attacker_HP = monster.defence
    while opponent_blockers != [] and monster.defence > 0:
        # Set up combatants
        blocker = opponent_blockers.pop()
        blocker_HP = blocker.defence

        monster.tapped = True
        blocker.tapped = True
        blocker_dies = False
        monster_dies = False
        
        # Check if there are "first strikes". If both have first strike, the attacker uses it first
        if "first_strike" in monster.keywords:
            blocker_dies = wounding_opposing_monster(monster, blocker)
        elif "first_strike" in blocker.keywords:
            monster_dies = wounding_opposing_monster(blocker, monster)
        else:
            blocker_dies = wounding_opposing_monster(monster, blocker)
            monster_dies = wounding_opposing_monster(blocker, monster)

        # If combatants die, they are put to graveyard
        if blocker_dies:
            opponent.graveyard.append(blocker)
            opponent.table.remove(blocker)
            if blocker in opponent.actions:
                opponent.actions.remove(blocker)

        if monster_dies:
            player.graveyard.append(monster)
            player.table.remove(monster)

        blocker.defence = blocker_HP

    monster.defence = attacker_HP



def wounding_opposing_monster(attacker, defender):
    # Does the defender die?
    defender.defence -= attacker.attack

    if defender.defence <= 0:
        return True
    return False
