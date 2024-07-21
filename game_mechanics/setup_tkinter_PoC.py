"""
Setup UI to watch the game play out.

This is not the game loop but to set up the correct layout that enables visualization of the game.
This also creates the UI for following card values in stock market.

"""

from tkinter import *
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

        # Draw the rectangles to the canvas
        canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="white")

        # Add card cost and name to cards
        canvas.create_text(start_x+5, start_y+5, text=hand_card.cost, font="Arial 9", anchor="nw")
        canvas.create_text(start_x+5, start_y+17, text=hand_card.name, font="Arial 9", anchor="nw")
        card += 1
    
    # Create an image for the deck
    canvas.create_rectangle(start_x + 140, start_y, end_x + 140, end_y, fill="light blue")
    canvas.create_rectangle(start_x + 143, start_y + 3, end_x + 143, end_y + 3, fill="light blue")
    canvas.create_rectangle(start_x + 146, start_y + 6, end_x + 146, end_y + 6, fill="light blue")
    canvas.create_rectangle(start_x + 149, start_y + 9, end_x + 149, end_y + 9, fill="light blue")
    canvas.create_text(start_x + 154, start_y+14, text="Draw deck", font="Arial 9", anchor="nw")

create_card_to_UI(mock_hand)

# Run UI
root.mainloop()



# Add items
# Add widgets??

# Layout

# 

# Fetch data

# Draw pictures

