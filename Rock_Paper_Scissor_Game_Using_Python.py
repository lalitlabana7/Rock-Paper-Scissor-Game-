import tkinter as tk
import random

# I Used Tkinter for the GUI

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Functon For Play
def play_game(player_choice):
    computer_choice = random.choice(choices)
    
    # Here i Have written The Condition For Winning
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Textview That Shows the message of Win Or Loss
    result_label.config(text=f"You chose {player_choice}, Computer chose {computer_choice}.\n{result}")

# Function to exit the game
def exit_game():
    window.quit()

# Main Window GUI
window = tk.Tk()
window.title("Rock, Paper, Scissors") #Header

# here it will automatically take screen width and height according to computer
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# here i am passing width and height to tkinter function i.e geometry()
window.geometry(f"{screen_width}x{screen_height}")

# background color
window.configure(bg="#f0f0f0")

# here i created result_label with border using tkinter GUI
result_label = tk.Label(window, text="Let's play Rock, Paper, Scissors!", bg="#f0f0f0", fg="#333333", font=("Arial", 18), borderwidth=2, relief="solid", padx=10, pady=10)
result_label.pack(pady=30)

# here i created frame for button
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=(80, 20))  # top margin 80 and button margin 20

# here i created buttons
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("rock"), bg="#ffa500", fg="white", padx=20, pady=10, font=("Arial", 14))
rock_button.grid(row=0, column=0, padx=10, pady=(10, 20))  # top padding 10 and botttom padding 20

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"), bg="#4169e1", fg="white", padx=20, pady=10, font=("Arial", 14))
paper_button.grid(row=0, column=1, padx=10, pady=(10, 20))  # top padding 10 and botttom padding 20

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"), bg="#9370db", fg="white", padx=20, pady=10, font=("Arial", 14))
scissors_button.grid(row=0, column=2, padx=10, pady=(10, 20))  # top padding 10 and botttom padding 20

# this is exit button 
exit_button = tk.Button(window, text="Exit", command=exit_game, bg="#ff6347", fg="white", padx=20, pady=10, font=("Arial", 14))
exit_button.pack(pady=20)

# it will start mainloop
window.mainloop()