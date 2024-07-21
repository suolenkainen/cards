"""
Setup UI to watch the game play out.

This is not the game loop but to set up the correct layout that enables visualization of the game.
This also creates the UI for following card values in stock market.

"""

from tkinter import *
from tkinter import font
import setup as cards
from main_loop import setup_mock_game, game

# Check that cards are present
mock_deck = cards.create_draw_deck(1, "PoC")
mock_hand = cards.draw_start_hand(mock_deck)

# Create window
root = Tk()
root.title("Cardgame")
canvas = Canvas(root)

# canvas = Canvas(width=440, height= 500)
canvas = Canvas(width=800, height= 500)
canvas.pack()


# Create label texts for the UI
canvas.create_text(40, 20, text="Player 1", font="Calibri 24 bold", anchor="nw")
canvas.create_text(40, 80, text="Table cards", font="Calibri 20", anchor="nw")
canvas.create_text(40, 280, text="Hand cards", font="Calibri 20", anchor="nw")

# Create hand cards to UI
# The table cards can be used with these coordinates: (40, 120, 140, 260, fill='blue')
def create_card_to_UI(players):
    player_hand = players[0].hand
    player_table = players[0].table
    canvas.delete("all")

    t_card = 0
    h_card = 0

    shrink_factor = 1
    if len(player_table) > 6:
        shrink_factor = len(player_table)*120/700
        print(shrink_factor)

    for table_card in player_table:

        t_start_x = 40 + t_card * 120 / shrink_factor
        t_start_y = 120
        t_end_x =  140 + t_card * 120 / shrink_factor
        t_end_y = 260

        rect_coords = t_start_x, t_start_y, t_end_x, t_end_y
        cost_coords = t_start_x-5, t_start_y+5, t_start_x+5, t_start_y+15
        text_coords = t_start_x+5, t_start_y+17

        # Draw the rectangles to the canvas
        canvas.create_rectangle(rect_coords, fill="white")

        # Add card cost and name to cards
        create_icons_for_cost(table_card.cost, cost_coords)

        # canvas.create_text(cost_coords, text=hand_card.cost, font="Arial 9", anchor="nw")
        input_text = align_text_and_row(table_card.name)
        canvas.create_text(text_coords, text=input_text, font="Arial 9", anchor="nw")
        t_card += 1

    # Reveal the cards in the player's hand
    for hand_card in player_hand:
        h_start_x = 40 + h_card * 120
        h_start_y = 320
        h_end_x =  140 + h_card * 120
        h_end_y = 460

        rect_coords = h_start_x, h_start_y, h_end_x, h_end_y
        cost_coords = h_start_x-5, h_start_y+5, h_start_x+5, h_start_y+15
        text_coords = h_start_x+5, h_start_y+17

        # Draw the rectangles to the canvas
        canvas.create_rectangle(rect_coords, fill="white")

        # Add card cost and name to cards
        create_icons_for_cost(hand_card.cost, cost_coords)

        # canvas.create_text(cost_coords, text=hand_card.cost, font="Arial 9", anchor="nw")
        input_text = align_text_and_row(hand_card.name)
        canvas.create_text(text_coords, text=input_text, font="Arial 9", anchor="nw")
        h_card += 1
        # Reveal the cards in the player's hand


    # Create an image for the deck
    for x in range(5):
        canvas.create_rectangle(h_start_x + 140 + 3*x, h_start_y + 3*x, h_end_x + 140 + 3*x, h_end_y + 3*x, fill="light blue")
    canvas.create_text(h_start_x + 154, h_start_y+14, text="Draw deck", font="Arial 9", anchor="nw")


def create_icons_for_cost(cost, coords):
    if cost:
        if isinstance(cost, str): cost = [cost]
        for icon in cost:
            coords = coords[0] + 12, coords[1], coords[2] + 12, coords[3]
            if icon == "any":
                icon = "grey"
            canvas.create_oval(coords, fill=icon)


def align_text_and_row(text, front_text = ""):
    max_width = 90
    text_object = font.Font(family="Arial", size=9)
    width_in_pixels = text_object.measure(text)
    if width_in_pixels > max_width:
        text = text.replace(" ", "\n")
    return text


players = setup_mock_game()

create_card_to_UI(players)

def time_print():
    print("Timer tick")
    game(players)
    create_card_to_UI(players)
    root.after(1000, time_print)

# Run UI


time_print()
root.mainloop()


