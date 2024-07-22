
def call_abilities(card, players):
    for ability in card.abilities:
        parameter_list = ability[1:]
        parameters = {}
        for parameter in parameter_list:
            key, value = parameter.split(":")
            value = value.split("&")
            parameters[key] = value
        print(ability)
        result = globals()[ability[0]](players, parameters)

def untap(players, parameters):
    print(parameters)


def first_strike(players, parameters):
    print(parameters)


def pounce(players, parameters):
    print(parameters)