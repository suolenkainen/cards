"""
Read the contents of a csv file and create a deck based on that.
The Deck() class is also used to create graveyard deck.

To chose the source of data, uncomment which ever file is needed
"""

from csv import DictReader
import random, re


# with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards.csv', 'r') as file:
# with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards_test.csv', 'r') as file:
with open('C:\\Users\\pmarj\\OneDrive\\Documents\\Cards\\cards\\game_mechanics\\cards_test_short.csv', 'r') as file:
    reader = DictReader(file, delimiter=';')
    list_of_card_dicts = [row for row in reader]

# Remove unnecessary variables
del reader, file



class Player():
    def __init__(self):
        self.id = 0
        self.name = "player 0"
        self.create_decks()
        self.hand = []
        self.table = []
        self.manapool = []
        self.strategy = None
        self.graveyard = []
        self.health = 100
        self.hand_size = 5
        self.next_draw_amount = 5
        self.actions = []

    def create_decks(self):
        self.player_deck = create_player_deck()
        self.player_deck.id = 0
        self.player_deck.deck_owner = ""
        self.player_deck.deck_purpose = "player deck"

        self.draw_deck = create_draw_deck(self.player_deck)
        self.draw_deck.id = 0
        self.draw_deck.deck_owner = ""
        self.draw_deck.deck_purpose = "draw deck"




def create_player_deck(id=0, owner="player 1"):
    # Create Deck-object
    player_deck = Deck()
    player_deck.id = id
    player_deck.deck_owner = owner

    # Create cards from test file
    for card_dict in list_of_card_dicts:
        player_deck.cards.append(Card(card_dict))
    
    player_deck.cards = player_deck.cards * 4

    random.seed(player_deck.id)
    random.shuffle(player_deck.cards)
    
    return player_deck



def create_draw_deck(player_deck):
    # Create Deck-object
    draw_deck = Deck()
    draw_deck.id = player_deck.id
    draw_deck.deck_owner = player_deck.deck_owner

    # Create cards from test file
    current_game = player_deck.cards[0].rounds

    random.seed(current_game + draw_deck.id)
    random.shuffle(player_deck.cards)
    draw_deck.cards = player_deck.cards[:32]

    #Shuffle deck
    random.seed(draw_deck.id)
    random.shuffle(draw_deck.cards)

    for playcard in draw_deck.cards:
        playcard.rounds = playcard.rounds + 1
        playcard.duplicates = 1
    
    return draw_deck



class Card():
    def __init__(self, data):
        # Create a card containing relevant information
        # Parse the data to be readable
        self.parse(data)

        # Add values to attributes
        self.id = self.parsed_data["#"]
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
        self.rounds = 0
        self.wins = 0
        self.win_average = 0
        self.duplicates = 0
        self.average_duplicates = 0

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
                value = self.check_if_integer(value)
                self.parsed_data[key] = value
            if key[:-1] == "ability" and value:
                abilities.append((value))
        self.parsed_data["abilities"] = abilities

    def check_if_integer(self, value):
        if isinstance(value, list) or not value:
            return value
        integer_pattern = re.compile(r'^-?\d+$')
        if bool(integer_pattern.match(value)):
            value = int(value)
        return value



class Deck():
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



def reset_game(players):
    # Reset game so that it can be run multiple times
    # This should be in the "setup.py" file

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

        player.draw_deck = create_draw_deck(player.player_deck)
        player.draw_deck.id = 0
        player.draw_deck.deck_owner = ""
        player.draw_deck.deck_purpose = "draw deck"
        zero_mana = True
        while zero_mana:
            player.hand = draw_start_hand(player.draw_deck)
            for card in player.hand:
                if card.type == "mana":
                    zero_mana = False
                    break
            if zero_mana:
                for i in range(5):
                    player.graveyard.append(player.hand.pop(0))



def setup_mock_game():
    # Create players and setup the first run of the game
    # This should be in the "setup.py" file
    players = []
    for i in range(2):
        player = Player()
        player.id = i
        player.name = "player "+str(i)
        random.seed(player.id)
        random.shuffle(player.draw_deck.cards)
        zero_mana = True
        while zero_mana:
            player.hand = draw_start_hand(player.draw_deck)
            for card in player.hand:
                if card.type == "mana":
                    zero_mana = False
                    break
            if zero_mana:
                for i in range(5):
                    player.graveyard.append(player.hand.pop(0))

        players.append(player)
    
    return players



if __name__ == "__main__":
    player_deck = create_player_deck(id=0, owner="player 1")
    draw_deck = create_draw_deck(player_deck)
    hand_cards = draw_start_hand(draw_deck)
    player = Player()
    print()