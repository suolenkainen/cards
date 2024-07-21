import tkinter as tk
from tkinter import ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# Create window
window = tk.Tk()
window.title("Cardgame")
window.geometry("200x150")

# title
title_label = ttk.Label(master = window, text = "Player 1 table", font = "Calibri 24 bold")
title_label.pack()

# Input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Skip turn", command= convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# Ouput
output_string = tk.StringVar()
output_lable = ttk.Label(master= window, text= "Output", font = "Calibri 24", textvariable=output_string)
output_lable.pack()

# Run UI
window.mainloop()



# Add items
# Add widgets??

# Layout

# 

# Fetch data

# Draw pictures

