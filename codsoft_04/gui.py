import tkinter as tk
import random
from PIL import Image, ImageTk


def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    update_score_label()

def reset_score():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score_label()

def update_score_label():
    score_label.config(text=f"User: {user_score}  |  Computer: {computer_score}")


# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("600x400")  # Changed window size to 600x400
root.configure(bg="#222")



# Define colors
button_color = "#3498db"
button_hover_color = "#2980b9"
button_radius = 10
button_font_color = "#ffffff"
text_color = "#ffffff"

# Create a frame for vertical centering and distribution
center_frame = tk.Frame(root, bg="#222")
center_frame.pack(expand=True, fill=tk.BOTH)

# Create labels and buttons inside the center frame
title_label = tk.Label(center_frame, text="Choose Rock, Paper, or Scissors:", bg="#222", fg=text_color, font=("Helvetica", 20))
title_label.pack(pady=(50, 10))  # Adjusted top padding and removed bottom padding

# Frame to contain buttons
button_frame = tk.Frame(center_frame, bg="#222")
button_frame.pack()

rock_button = tk.Button(
    button_frame,
    text="Rock",
    command=lambda: play_game("Rock"),
    bg=button_color,
    activebackground=button_hover_color,
    font=("Helvetica", 14),
    fg=button_font_color,
    padx=20,
    pady=10,
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    relief="ridge",
    cursor="hand2"
)
paper_button = tk.Button(
    button_frame,
    text="Paper",
    command=lambda: play_game("Paper"),
    bg=button_color,
    activebackground=button_hover_color,
    font=("Helvetica", 14),
    fg=button_font_color,
    padx=20,
    pady=10,
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    relief="ridge",
    cursor="hand2"
)
scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    command=lambda: play_game("Scissors"),
    bg=button_color,
    activebackground=button_hover_color,
    font=("Helvetica", 14),
    fg=button_font_color,
    padx=20,
    pady=10,
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    relief="ridge",
    cursor="hand2"
)

rock_button.pack(side="left", padx=20)  # Increased space between buttons and adjusted padding
paper_button.pack(side="left", padx=20)
scissors_button.pack(side="left", padx=20)

result_label = tk.Label(center_frame, text="", bg="#222", fg=text_color, font=("Helvetica", 14))
result_label.pack(pady=20)  # Added more space below the result label

score_label = tk.Label(center_frame, text="", bg="#222", fg=text_color, font=("Helvetica", 16))
score_label.pack(pady=(20, 50))  # Adjusted top and bottom padding

reset_button = tk.Button(
    center_frame,
    text="Reset Score",
    command=reset_score,
    bg=button_color,
    activebackground=button_hover_color,
    font=("Helvetica", 14),
    fg=button_font_color,
    padx=20,
    pady=10,
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    relief="ridge",
    cursor="hand2"
)
reset_button.pack()

# Initialize scores
user_score = 0
computer_score = 0
update_score_label()

# Start the GUI main loop
root.mainloop()
