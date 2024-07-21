"""
Setup UI to watch the game play out.

This is not the game loop but to set up the correct layout that enables visualization of the game.
This also creates the UI for following card values in stock market.

NOTE: Check Clear Code website for stock market tracker
"""

from tkinter import *

# Create window
root = Tk()
root.title("Cardgame")
canvas = Canvas(root)



canvas = Canvas(width=440, height= 500)
canvas.pack()


# Create label texts for the UI
canvas.create_text(40, 20, text="Player 1", font="Calibri 24 bold", anchor="nw")
canvas.create_text(40, 80, text="Table cards", font="Calibri 20", anchor="nw")
canvas.create_text(40, 280, text="Hand cards", font="Calibri 20", anchor="nw")


# Create cards to canvas
canvas.create_rectangle(40, 120, 140, 260, fill='blue')
canvas.create_rectangle(160, 120, 260, 260, fill='purple')
canvas.create_rectangle(300, 120, 400, 260, fill='green')
canvas.create_rectangle(40, 320, 140, 460, fill='red')
canvas.create_rectangle(160, 320, 260, 460, fill='orange')
canvas.create_rectangle(300, 320, 400, 460, fill='yellow')

# Create descriptors for rectangles
canvas.create_text(45, 125, text="Player 1", font="Calibri 12 bold", anchor="nw")
canvas.create_text(165, 125, text="Player 1", font="Calibri 12 bold", anchor="nw")
canvas.create_text(305, 125, text="Player 1", font="Calibri 12 bold", anchor="nw")
canvas.create_text(45, 325, text="Player 1", font="Calibri 12 bold", anchor="nw")
canvas.create_text(165, 325, text="Player 1", font="Calibri 12 bold", anchor="nw")
canvas.create_text(305, 325, text="Player 1", font="Calibri 12 bold", anchor="nw")


# Run UI
root.mainloop()



# Add items
# Add widgets??

# Layout

# 

# Fetch data

# Draw pictures

