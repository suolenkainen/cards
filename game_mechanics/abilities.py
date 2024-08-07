import operator
from copy import copy
from typing import List



def call_abilities(card, players, **kwargs):
    for ability in card.abilities:
        parameter_list = ability[1:]
        parameters = {}
        for parameter in parameter_list:
            key, value = parameter.split(":")
            value = value.split("&")
            parameters[key] = value
        print(ability)
        return globals()[ability[0]](players, parameters, card=card, variables=kwargs)



def untap(players, parameters, **kwargs):
    # Set target for untap
    action_target = players[0]
    if parameters["target"] == "opponent":
        action_target = players[1]
    
    # Identify cards in table
    target_cards = copy(action_target.table)
    for keyword in parameters["keywords"]:
        for card in action_target.table:
            if keyword not in card.keywords or card.tapped == False:
                if card in target_cards:
                    target_cards.remove(card)
    if target_cards == []:
        return False
    
    # Sort cards based on the
    target_cards = sorted(target_cards, reverse=True, key=create_key_function(parameters["sort"]))

    # Untap target card(s)
    if "amount" not in parameters:
        parameters["amount"] = 1
    amount = copy(parameters["amount"])
    if "upto" in parameters:
        if len(target_cards) < parameters["amount"]:
            amount = len(target_cards)
    for i in range(amount):
        target_cards[i].tapped = False

    return True



def counter(players, parameters, **kwargs):
    # Counter a card played by the opponent
    variables = kwargs["variables"]
    target_card = variables["played_card"]
    interrupt_card = variables["interrupt_card"]

    for keyword in parameters["keywords"]:
        if keyword not in target_card.keywords:
            return False
    
    # If the counter is successful, remove both target and countering card
    players[0].hand.remove(target_card)
    players[0].graveyard.append(target_card)
    players[1].hand.remove(interrupt_card)
    players[1].graveyard.append(interrupt_card)

    return True



def first_strike(players, parameters, **kwargs):
    # Check if the played card is a monster
    # Later there might be monsters that grant abilities
    if parameters["target"] == "self":
        return False

    # Set target to give an ability
    action_target = players[0]
    
    # Identify cards in table and make sure the target doesn't have the ability already
    target_cards = copy(action_target.table)
    for keyword in parameters["keywords"]:
        for card in action_target.table:
            if keyword not in card.keywords or card.type != "monster":
                if card in target_cards:
                    target_cards.remove(card)
                    continue
            for ability in card.abilities:
                if ability[0] == "first_strike" and card in target_cards:
                    target_cards.remove(card)
                    continue
    if target_cards == []:
        return False
    
    # Sort cards based on the "sort" parameter. If there are many attributes, it will go them in order
    target_cards = sorted(target_cards, reverse=True, key=create_key_function(parameters["sort"]))

    # Add ability
    if "amount" not in parameters:
        parameters["amount"] = 1
    amount = copy(parameters["amount"])
    if "upto" in parameters:
        if len(target_cards) < parameters["amount"]:
            amount = len(target_cards)
    for i in range(amount):
        target_cards[i].abilities.append(["first_strike", "target:self", "keywords:self", "priority:0"])

    return True


# This list of abilities is a place holder for upcoming ability descriptions. They are filled as they come relevant.
# This point they are just place holders to avoid errors
def blocker(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def draw_card(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def pounce(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def trample(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def psychic(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def enchant_creature(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def control(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def psychic_blast(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def front_line(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def bull_rush(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def ranged(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def sunder(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def shatter(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def charge(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def ready(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def defender(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass

def tap(players, parameters, **kwargs):
    # Don't remove card if not an instant
    pass



# Create a list of sorting keywords. This returns either one parameter or more
def create_key_function(attrs: List[str]):
    return operator.attrgetter(*attrs)