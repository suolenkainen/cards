"""
Read the contents of a csv file and create a deck based on that.
The deck_object() class is also used to create graveyard deck.

To chose the source of data, uncomment which ever file is needed
"""

from csv import DictReader
import random


# with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards.csv', 'r') as file:
# with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards_test.csv', 'r') as file:
with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards_test_short.csv', 'r') as file:
    reader = DictReader(file, delimiter=';')
    list_of_card_dicts = [row for row in reader]

# Remove unnecessary variables
del reader, file



class player_object():
    def __init__(self):
        self.id = 0
        self.name = "player 0"
        self.create_deck()
        self.hand = []
        self.table = []
        self.manapool = []
        self.strategy = None
        self.graveyard = []
        self.health = 100
        self.hand_size = 5
        self.next_draw_amount = 5
        self.actions = []

    def create_deck(self):
        self.draw_deck = create_draw_deck()
        self.draw_deck.id = 0
        self.draw_deck.deck_owner = ""
        self.draw_deck.deck_purpose = "draw deck"



def create_draw_deck(id=0, owner="player 1"):
    # Create Deck-object
    player_deck = deck_object()
    player_deck.id = id
    player_deck.deck_owner = owner

    # Create cards from test file
    for card_dict in list_of_card_dicts:
        player_deck.cards.append(card_object(card_dict))
    
    #Shuffle deck
    random.seed(player_deck.id)
    random.shuffle(player_deck.cards)
    
    return player_deck



class card_object():
    def __init__(self, data):
        # Create a card containing relevant information
        # Parse the data to be readable
        self.parse(data)

        # Add values to attributes
        self.id = int(self.parsed_data["#"])
        self.name = self.parsed_data["name"]
        self.color = self.parsed_data["color"]
        self.type = self.parsed_data["type"]
        self.keywords = self.parsed_data["keywords"]
        self.rarity = self.parsed_data["rarity"]
        self.cost = self.parsed_data["cost"]
        self.attack = self.parsed_data["att"]
        self.defence = self.parsed_data["def"]
        self.abilities = self.parsed_data["abilities"]
        self.tapped = None
        self.priority = 0

        # Remove redundant attribute from object
        del self.parsed_data

    def parse(self, data):        
        # Parse data from csv
        # Will be updated as the data becomes more refined
        self.parsed_data = {}
        abilities = []
        for key, value in data.items():
            if key != "":
                key = key.lower().rstrip(',')                
                value = value.lower()
                value = list(filter(None, value.split(',')))
                if len(value) == 1: value = value[0]
                if not value: value = None
                self.parsed_data[key] = value
            if key[:-1] == "ability" and value:
                abilities.append((value))
        self.parsed_data["abilities"] = abilities



class deck_object():
    def __init__(self):
        self.id = 0
        self.deck_owner = ""
        self.deck_purpose = "draw deck"
        self.cards = []



def draw_start_hand(player_deck):
    hand = []
    for x in range(5):
        hand.append(player_deck.cards.pop(0))

    return hand



if __name__ == "__main__":
    player_deck = create_draw_deck(0, "player 1")
    hand_cards = draw_start_hand(player_deck)
    player = player_object
    print()