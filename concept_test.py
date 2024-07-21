import random, copy
#for tests
random.seed(0)

#cards
#status can be "deck", "table tapped", "table untapped", "hand", "graveyard"

cards = {
    0: {
        "id": "ABC-000",
        "color": "blue",
        "cost": ["blue"], 
        "name": "Blue monster",
        "type": "monster",
        "rarity": "common",
        "attack": 1,
        "defence": 1,
        "abilities": [],
        "keywords": ["monster", "elf", "blue"],
        "status": "deck",
        "priority": 0},
    1: {
        "id": "ABC-001",
        "color": "blue",
        "cost": ["blue"], 
        "name": "Blue enchantment",
        "type": "enchantment",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        # "abilities": [("tap_untap", ["tap/untap", "owner", "color", "type", "subtype", "condition"])]
        "abilities": [("untap", {"target": "player", "keywords": "blue, monster", "priority": "highest"})],
        "keywords": ["enchantment", "control", "blue"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    2: {
        "id": "ABC-002",
        "color": "blue",
        "cost": [], 
        "name": "Blue mana",
        "type": "mana",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        "abilities": [],
        "keywords": ["mana", "blue"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    3: {
        "id": "ABC-002",
        "color": "blue",
        "cost": [], 
        "name": "Blue mana",
        "type": "mana",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        "abilities": [],
        "keywords": ["mana", "blue"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    4: {
        "id": "ABC-003",
        "color": "red",
        "cost": ["red"], 
        "name": "Red monster",
        "type": "monster",
        "rarity": "common",
        "attack": 1,
        "defence": 1,
        "abilities": [],
        "keywords": ["monster", "goblin", "red"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    5: {
        "id": "ABC-004",
        "color": "red",
        "cost": ["red"], 
        "name": "Red enchantment",
        "type": "enchantment",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        "abilities": [("damage", {"damage": 1, "target": "opponent"})],
        "keywords": ["enchantment", "damage", "red"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    6: {
        "id": "ABC-005",
        "color": "red",
        "cost": [], 
        "name": "Red mana",
        "type": "mana",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        "abilities": [],
        "keywords": ["mana", "red"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    7: {
        "id": "ABC-005",
        "color": "red",
        "cost": [], 
        "name": "Red mana",
        "type": "mana",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        "abilities": [],
        "keywords": ["mana", "red"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    8: {
        "id": "ABC-000",
        "color": "blue",
        "cost": ["blue"], 
        "name": "Blue monster",
        "type": "monster",
        "rarity": "common",
        "attack": 1,
        "defence": 1,
        "abilities": [],
        "keywords": ["monster", "elf", "blue"],
        "status": "deck",
        "priority": 0},
    9: {
        "id": "ABC-004",
        "color": "blue",
        "cost": ["blue", "blue"], 
        "name": "Blue monster 2",
        "type": "monster",
        "rarity": "common",
        "attack": 2,
        "defence": 2,
        "abilities": [],
        "keywords": ["monster", "elf", "blue"],
        "status": "deck",
        "priority": 0},
    10: {
        "id": "ABC-001",
        "color": "blue",
        "cost": ["blue"], 
        "name": "Blue enchantment",
        "type": "enchantment",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        # "abilities": [("tap_untap", ["tap/untap", "owner", "color", "type", "subtype", "condition"])]
        "abilities": [("untap", {"target": "player", "keywords": "blue, monster", "priority": "highest"})],
        "keywords": ["enchantment", "control", "blue"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    11: {
        "id": "ABC-004",
        "color": "red",
        "cost": ["red", "red"], 
        "name": "Red enchantment 2",
        "type": "enchantment",
        "rarity": "common",
        "attack": 0,
        "defence": 0,
        "abilities": [("damage", {"damage": 2, "target": "opponent"})],
        "keywords": ["enchantment", "damage", "red"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
    12: {
        "id": "ABC-003",
        "color": "red",
        "cost": ["red", "red"], 
        "name": "Red blocker monster",
        "type": "monster",
        "rarity": "common",
        "attack": 1,
        "defence": 2,
        "abilities": [],
        "keywords": ["monster", "goblin", "red", "opportunist"],
        "status": "deck",
        "status": "deck",
        "priority": 0},
}

class player():
    def __init__(self, name, strategy):
        self.name = name
        self.health = 5
        self.hand_limit = 3
        self.cards = copy.deepcopy(cards)
        self.deck = self.shuffle()
        self.graveyard = []
        self.hand = []
        draw_cards(self)
        self.table = []
        self.manapool = []
        self.strategy(strategy)
    
    def shuffle(self):
        deck = list(self.cards.keys())
        # print(deck)

        random.shuffle(deck)
        # print(deck)

        return deck
    
    def strategy(self, strategy):
        self.cards = strategies(strategy, self.cards)
    

def strategies(strategy, player_cards):
    if strategy[0] == "red":
        for key, value in player_cards.items():
            if "red" in value["keywords"]:
                player_cards[key]["priority"] += 1
                
    if strategy[0] == "blue":
        for key, value in player_cards.items():
            if "blue" in value["keywords"]:
                player_cards[key]["priority"] += 1
        
    if strategy[1] == "monster":
        for key, value in player_cards.items():
            if "monster" in value["keywords"]:
                player_cards[key]["priority"] += 1

    if strategy[1] == "enchantment":
        for key, value in cards.items():
            if "enchantment" in value["keywords"]:
                player_cards[key]["priority"] += 1

    if strategy[2] == "control":
        for key, value in player_cards.items():
            if "control" in value["keywords"]:
                player_cards[key]["priority"] += 1

    if strategy[2] == "damage":
        for key, value in player_cards.items():
            if "damage" in value["keywords"]:
                player_cards[key]["priority"] += 1
    
    return player_cards
    

def draw_cards(player):
    while len(player.hand) < player.hand_limit and len(player.deck) > 0:
        player.cards[player.deck[0]]["status"] = "hand"
        player.hand.append(player.deck.pop(0))


def sort_hand(player):
    # arrange cards in priority play order
    temp_hand = []
    priority = 4
    while True:
        for i, card in enumerate(player.hand):
            if player.cards[card]["priority"] > priority:
                temp_hand.append(player.hand.pop(i))
        priority -= 1
        if len(player.hand) == 0: 
            player.hand = temp_hand
            break


def play(player, opponent):
    
    temp_hand = copy.copy(player.hand)
    for i in player.hand:
        temp_pool = copy.copy(player.manapool)
        current_card = player.cards[i]
        temp_pool = copy.copy(player.manapool)
        temp_cost = copy.copy(current_card["cost"])
        for mana in current_card["cost"]:
            if mana in temp_pool:
                temp_pool.remove(mana)
                temp_cost.remove(mana)
            else:
                break
        if temp_cost == []:
            if player.cards[i]["type"] == "enchantment":
                for ability, parameters in player.cards[i]["abilities"]:
                    result = globals()[ability](opponent, player, parameters)
                    if result:
                        player.cards[i]["status"] = "graveyard"
                        player.graveyard.insert(i, 0)
                        temp_hand.remove(i)
                # player.cards[i]["status"] = "table untapped"
                continue
            else:
                player.cards[i]["status"] = "table tapped"
            player.table.append(i)
            temp_hand.remove(i)
            player.manapool = temp_pool
            print("Plays card", player.cards[i]["name"])
    player.hand = temp_hand


def action(player, opponent):
    list_untapped = []
    for card in player.table:
        if player.cards[card]["status"] == "table untapped" and player.cards[card]["type"] != "mana":
            list_untapped.append(card)
    for card in list_untapped:
        for ability, parameters in player.cards[card]["abilities"]:
            result = globals()[ability](opponent, player, parameters)
            # jos ability maksaa, se pitää merkata
        if player.cards[card]["type"] == "monster" and "blocker" not in player.cards[card]["keywords"]:
            attacked = attack(card, player, opponent)
            if attacked:
                if player.cards[card]["status"] == "graveyard":
                    player.table.remove(card)
                else:
                    player.cards[card]["status"] == "table tapped"


def attack(card, player, opponent):
    opponent_blockers = []
    for opp_card in opponent.table:
        if opponent.cards[opp_card]["status"] == "table untapped" and opponent.cards[opp_card]["type"] == "monster":
            opponent_blockers.append(opp_card)
    if opponent_blockers == []:
        opponent.health -= player.cards[card]["attack"]
        print(player.cards[card]["name"], "attacked", opponent.name, "reducing its health to", opponent.health)
        return True
    if "opportunist" in player.cards[card]["keywords"] and opponent_blockers != []:
        return False
    
    attacker_HP = player.cards[card]["defence"]
    while opponent_blockers != [] or attacker_HP <= 0:
        blocker_id = opponent_blockers.pop()
        blocker_HP = opponent.cards[blocker_id]["defence"]
        blocker_HP -= player.cards[card]["attack"]
        if blocker_HP <= 0:
            opponent.cards[blocker_id]["status"] = "graveyard"
            opponent.table.remove(blocker_id)
            print(player.cards[card]["name"], "attacked", opponent.cards[blocker_id]["name"], "destroying it")
        else:
            attacker_HP -= opponent.cards[blocker_id]["attack"]
            print(player.cards[card]["name"], "attacked", opponent.cards[blocker_id]["name"], "destroying it")
        if attacker_HP <= 0:
            player.cards[card]["status"] = "graveyard"

    return True
    

def damage(opponent, player, parameters):
    if parameters["target"] == "opponent":
        opponent.health -= parameters["damage"]
        print(player.name, "damages with spell", opponent.name, "reducing its health to", opponent.health)
        return True


def untap(opponent, player, parameters): 
    if parameters["target"] == "player":
        target_card = identify_card(parameters, player)
        if target_card == None:
            return False
        player.cards[target_card]["status"] = "table untapped"
    else:
        target_card = identify_card(parameters, opponent)
        if target_card == None:
            return False
        opponent.cards[target_card]["status"] = "table untapped"
    return True


def identify_card(parameters, target):
    for card in target.table:
        allpresent = all(criterion in target.cards[card]["keywords"] for criterion in parameters["keywords"])
        if allpresent:
            pass # check priority, if there is
        else:
            return None




#game
def game(players):
    turn_counter = 20
    while turn_counter > 0:
        player = players[0]
        opponent = players[1]
        
        # Untap phase
        untap_phase(player)
        sort_hand(player)

        play(player, opponent)

        action(player, opponent)
        if opponent.health <= 0:
            print(player.name, "WINS!")
            break

        discard_phase(player)

        draw_cards(player)
        players = [opponent, player]

        turn_counter -= 1
        print()


def discard_phase(player):
    if len(player.hand) == player.hand_limit:
        player.graveyard.append(player.hand.pop())


def untap_phase(player):

    print(player.name)
    player.manapool = []
    for card in player.cards:
        if player.cards[card]["status"] == "table tapped":
            player.cards[card]["status"] = "table untapped"
        if player.cards[card]["type"] == "mana" and player.cards[card]["status"] == "table untapped":
            player.manapool.append(cards[card]["color"])



if __name__ == "__main__":
    players = []
    random.seed(4)
    players.append(player("player 1", ["red", "monster", "damage"]))
    random.seed(3)
    players.append(player("player 2", ["blue", "enchantment", "control"]))

    game(players)