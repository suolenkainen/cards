"""
Setup UI to watch the game play out.

This is not the game loop but to set up the correct layout that enables visualization of the game.
This also creates the UI for following card values in stock market.

"""

from tkinter import *
from tkinter import font
import setup
from main_loop import setup_mock_game, game, reset_game
import csv

# Check that cards are present
mock_deck = setup.create_draw_deck(1, "PoC")
mock_hand = setup.draw_start_hand(mock_deck)

# Create a csv file of saving the statistics
with open('test_record.csv', 'w', newline='') as file:
    writer = csv.writer(file)

# Create window
root = Tk()
root.title("Cardgame")
canvas = Canvas(root)

# Dimensions
card_size = 100, 140
left_buffer = 40
table_card_row = 120
hand_card_row = 320

# canvas = Canvas(width=440, height= 500)
canvas = Canvas(width=8 * card_size[0], height= 4 * card_size[1])
canvas.pack()

# Set fonts
text_font = "Calibri "
header_font_size = "24 bold"
subheader_font_size = "20"
card_font_size = "9"

header_font = text_font + header_font_size
subheader_font = text_font + subheader_font_size
card_text_font = text_font + card_font_size


# Create hand cards to UI
# The table cards can be used with these coordinates: (40, 120, 140, 260, fill='blue')
def create_card_to_UI(players):
    # Clear Canvas
    canvas.delete("all")

    player_hand = players[0].hand
    player_table = players[0].table
    
    # If too many cards on the table, they are moved closer
    shrink_factor = 1
    if len(player_table) > 6:
        shrink_factor = len(player_table)* (card_size[0] +20) / 700

    # Draw titles to canvas
    canvas.create_text(left_buffer, 20, text=players[0].name, font=header_font, anchor="nw")
    canvas.create_text(left_buffer, 80, text="Table cards", font=subheader_font, anchor="nw")
    canvas.create_text(left_buffer, 280, text="Hand cards", font=subheader_font, anchor="nw")
    canvas.create_text(left_buffer, 500, text="Health: " + str(players[0].health), font=card_text_font, anchor="nw")
    canvas.create_text(left_buffer + 100, 500, text="Hand size: " + str(players[0].hand_size), font=card_text_font, anchor="nw")



    for i, table_card in enumerate(player_table):

        # Set sizes and coordinations for elements
        t_start_x = left_buffer + i * (card_size[0] +20) / shrink_factor
        t_end_x =  t_start_x + card_size[0]
        t_start_y = table_card_row
        t_end_y = t_start_y + card_size[1]

        # Draw the rectangles to the canvas
        rect_coords = t_start_x, t_start_y, t_end_x, t_end_y
        if table_card.color == "colourless":
            table_card.color = "grey"
        
        width = 3
        if table_card.type == "mana":
            width = 6

        # Turn card 90 degrees if tapped
        if table_card.tapped:
            t_start_x = left_buffer-20 + i * (card_size[0] +20) / shrink_factor
            t_end_x =  t_start_x+40 + card_size[0]
            t_start_y = table_card_row+20
            t_end_y = t_start_y + card_size[1]-40
            rect_coords = t_start_x, t_start_y, t_end_x, t_end_y
            canvas.create_rectangle(rect_coords, fill="light grey", outline="dark "+table_card.color, width=width)

        else:
            canvas.create_rectangle(rect_coords, fill="white", outline=table_card.color, width=width)

        # Add card cost and name to cards
        cost_coords = t_start_x-5, t_start_y+5, t_start_x+5, t_start_y+15
        create_icons_for_cost(table_card.cost, cost_coords)
        
        text_coords = t_start_x+5, t_start_y+17
        card_name = align_text_and_row(table_card.name)
        canvas.create_text(text_coords, text=card_name, font=card_text_font, anchor="nw")

        # Add card combat score, if any
        if table_card.type not in ["mana","enchantment"]:
            combat_coords = t_start_x+95, t_start_y+115
            if not table_card.attack: table_card.attack = 0
            if not table_card.defence: table_card.defence = 0
            combat_text = str(table_card.attack) + " / " + str(table_card.defence)
            canvas.create_text(combat_coords, text=combat_text, font=card_text_font, anchor="ne")


    # Reveal the cards in the player's hand
    for j, hand_card in enumerate(player_hand):
        
        # Set sizes and coordinations for elements
        h_start_x = left_buffer + j * (card_size[0] +20)
        h_end_x =  h_start_x + card_size[0]
        h_start_y = hand_card_row
        h_end_y = h_start_y + card_size[1]

        width = 3
        if hand_card.type == "mana":
            width = 6

        # Draw the rectangles to the canvas
        rect_coords = h_start_x, h_start_y, h_end_x, h_end_y
        if hand_card.color == "colourless":
            hand_card.color = "grey"
        canvas.create_rectangle(rect_coords, fill="white", outline=hand_card.color, width=width)

        # Add card cost and name to cards, and attack & defence
        cost_coords = h_start_x-5, h_start_y+5, h_start_x+5, h_start_y+15
        create_icons_for_cost(hand_card.cost, cost_coords)

        text_coords = h_start_x+5, h_start_y+17
        card_name = align_text_and_row(hand_card.name)
        canvas.create_text(text_coords, text=card_name, font=card_text_font, anchor="nw")

        # Add card combat score, if any
        if hand_card.type not in ["mana","enchantment"]:
            combat_coords = h_start_x+95, h_start_y+115
            if not hand_card.attack: hand_card.attack = 0
            if not hand_card.defence: hand_card.defence = 0
            combat_text = str(hand_card.attack) + " / " + str(hand_card.defence)
            canvas.create_text(combat_coords, text=combat_text, font=card_text_font, anchor="ne")


    # Create an image for the deck
    for x in range(5):
        canvas.create_rectangle(h_start_x + 140 + 3*x, h_start_y + 3*x, h_end_x + 140 + 3*x, h_end_y + 3*x, fill="light blue")
    canvas.create_text(h_start_x + 154, h_start_y+14, text="Draw deck", font=card_text_font, anchor="nw")
    


def create_icons_for_cost(cost, coords):
    if cost:
        if isinstance(cost, str): cost = [cost]
        for icon in cost:
            coords = coords[0] + 12, coords[1], coords[2] + 12, coords[3]
            if icon == "any":
                icon = "grey"
            canvas.create_oval(coords, fill=icon)



def align_text_and_row(text):
    max_width = 90
    text_object = font.Font(family=text_font, size=9)
    width_in_pixels = text_object.measure(text)
    if width_in_pixels > max_width:
        text = text.replace(" ", "\n")
    return text


players = setup_mock_game()

# create_card_to_UI(players)

def time_print():
    games = 5
    game(players)
    create_card_to_UI(players)
        
    with open('test_record.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        data = [
            [players[0].__dict__],
            [players[1].__dict__]
            ]
        writer.writerows(data)

    if players[1].health <= 0 or len(players[1].draw_deck.cards) == 0:
        print(players[0].name, "WINS!")
        reset_game(players)
        games -= 1
    if players[0].health <= 0 or len(players[0].draw_deck.cards) == 0:
        print(players[1].name, "WINS!")
        reset_game(players)
        games -= 1
    if games == 0:
        root.destroy()
        return

    root.after(200, time_print)

# Run UI
time_print()
root.mainloop()

