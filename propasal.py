import tkinter as tk
from tkinter import messagebox

def on_yes():
    messagebox.showinfo("Yay!", "I knew you'd say YES! ❤ Happy Valentine's Day!")
    root.destroy()

def on_no():
    no_button.place(x=random.randint(50, 350), y=random.randint(50, 250))

import random

# Create the main window
root = tk.Tk()
root.title("Valentine's Day Proposal")
root.geometry("400x300")
root.configure(bg="pink")

# Add a label with the proposal
label = tk.Label(root, text="Will you be my Valentine? 💖", font=("Helvetica", 16), bg="pink")
label.pack(pady=30)

# Add Yes and No buttons
yes_button = tk.Button(root, text="Yes 💘", font=("Helvetica", 14), command=on_yes, bg="lightgreen")
yes_button.place(x=100, y=150)

no_button = tk.Button(root, text="No 💔", font=("Helvetica", 14), command=on_no, bg="red")
no_button.place(x=200, y=150)

# Run the application
root.mainloop()