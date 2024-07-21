"""
Setup UI to watch the game play out.

This is not the game loop but to set up the correct layout that enables visualization of the game.
This also creates the UI for following card values in stock market.

"""

from tkinter import *
from tkinter import font
import setup_cards as cards

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
def create_card_to_UI(mock_hand):
    card = 0

    # Reveal the cards in the player's hand
    for hand_card in mock_hand:
        start_x = 40 + card * 120
        start_y = 320
        end_x =  140 + card * 120
        end_y = 460

        rect_coords = start_x, start_y, end_x, end_y
        cost_coords = start_x-5, start_y+5, start_x+5, start_y+15
        text_coords = start_x+5, start_y+17

        # Draw the rectangles to the canvas
        canvas.create_rectangle(rect_coords, fill="white")

        # Add card cost and name to cards
        create_icons_for_cost(hand_card.cost, cost_coords)

        # canvas.create_text(cost_coords, text=hand_card.cost, font="Arial 9", anchor="nw")
        input_text = align_text_and_row(hand_card.name)
        canvas.create_text(text_coords, text=input_text, font="Arial 9", anchor="nw")
        card += 1
    
    # Create an image for the deck
    for x in range(5):
        canvas.create_rectangle(start_x + 140 + 3*x, start_y + 3*x, end_x + 140 + 3*x, end_y + 3*x, fill="light blue")
    canvas.create_text(start_x + 154, start_y+14, text="Draw deck", font="Arial 9", anchor="nw")


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
    print(width_in_pixels)
    if width_in_pixels > max_width:
        text = text.replace(" ", "\n")
    print(text)
    return text


create_card_to_UI(mock_hand)

# Run UI
root.mainloop()


