from csv import DictReader
import random

"""
Read the contents of a csv file and create a deck based on that.
The deck() class is also used to create graveyard deck.

To chose the source of data, uncomment which ever file is needed
"""

# with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards.csv', 'r') as file:
# with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards_test.csv', 'r') as file:
with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards_test_short.csv', 'r') as file:
    reader = DictReader(file, delimiter=';')
    list_of_card_dicts = [row for row in reader]


def create_draw_deck(id, owner):
    # Create Deck-object
    player_deck = deck()
    player_deck.id = id
    player_deck.deck_owner = owner

    # Create cards from test file
    for card_dict in list_of_card_dicts:
        player_deck.cards.append(card(card_dict))
    
    #Shuffle deck
    random.seed(player_deck.id)
    random.shuffle(player_deck.cards)
    
    return player_deck


class card():
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
        self.abilities = self.parsed_data["ability"]

        # Remove redundant attribute from object
        del self.parsed_data

    def parse(self, data):
        # Parse data from csv
        # Will be updated as the data becomes more refined

        self.parsed_data = {}
        for key, value in data.items():
            if key != "":
                key = key.lower().rstrip(',')                
                value = value.lower()
                value = list(filter(None, value.split(',')))
                if len(value) == 1: value = value[0]
                if not value: value = None
                self.parsed_data[key] = value


class deck():
    def __init__(self):
        self.id = 0
        self.deck_owner = ""
        self.deck_purpose = "draw deck"
        self.cards = []


if __name__ == "__main__":
    create_draw_deck(0, "player 1")
    print()