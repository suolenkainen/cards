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
        return globals()[ability[0]](players, parameters, variables=kwargs)



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
    # target
    variables = kwargs["variables"]
    target_card = variables["played_card"]
    interrupt_card = variables["interrupt_card"]

    for keyword in parameters["keywords"]:
        if keyword not in target_card.keywords:
            return False
    
    players[0].hand.remove(target_card)
    players[0].graveyard.append(target_card)

    players[1].hand.remove(interrupt_card)
    players[1].graveyard.append(interrupt_card)

    return True



def draw_card(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)

def first_strike(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def pounce(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def trample(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def psychic(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def enchant_creature(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def control(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def psychic_blast(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def front_line(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def bull_rush(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def ranged(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def sunder(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def shatter(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def charge(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def ready(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def defender(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def blocker(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)


def tap(players, parameters, **kwargs):
    # Don't remove card if not an instant
    print(parameters)



# Util function 
def create_key_function(attrs: List[str]):
    return operator.attrgetter(*attrs)