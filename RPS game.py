import tkinter as tk
from tkinter import messagebox
import random
user_score = 0
comp_score = 0
tie_score = 0
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "tie"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        return "user"
    else:
        return "computer"
def play(user_choice):
    global user_score, comp_score, tie_score
    choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(choices)
    result = determine_winner(user_choice, comp_choice)
    
    if result == "tie":
        tie_score += 1
        result_text = f"Both select the {user_choice}. It's a tie!"
    elif result == "user":
        user_score += 1
        result_text = f"You select the {user_choice}. Computer select the {comp_choice}. You win!"
    else:
        comp_score += 1
        result_text = f"You select the {user_choice}. Computer select the {comp_choice}. You lose!"
    
    score_label.config(text=f"User: {user_score}  Computer: {comp_score}  Ties: {tie_score}")
    
    if user_score == 6 or comp_score == 6:
        if user_score == 6:
            result_text = "Congratulations! You won the best of 10!"
        else:
            result_text = "Sorry! The computer won the best of 10."
        
        messagebox.showinfo("Final Result", result_text)
        reset_game()
    else:
        messagebox.showinfo("Result", result_text)
def reset_game():
    global user_score, comp_score, tie_score
    user_score = 0
    comp_score = 0
    tie_score = 0
    score_label.config(text=f"User: {user_score}  Computer: {comp_score}  Ties: {tie_score}")
def exit_game():
    root.destroy()
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.config(bg="purple") 
tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg="purple").pack(pady=14)

frame = tk.Frame(root, bg="purple")
frame.pack(pady=14)

button_style = {
    "width": 14,
    "bg": "white",
    "fg": "black",
    "font": ("Times New Roman", 16),
    "relief": "sunken",
    "bd": 10
}

rock_button = tk.Button(frame, text="Rock", command=lambda: play("rock"), **button_style)
rock_button.pack(side="left", padx=6)

paper_button = tk.Button(frame, text="Paper", command=lambda: play("paper"), **button_style)
paper_button.pack(side="left", padx=6)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: play("scissors"), **button_style)
scissors_button.pack(side="left", padx=6)

score_label = tk.Label(root, text=f"User: {user_score}  Computer: {comp_score}  Ties: {tie_score}", bg="purple", pady=14)
score_label.pack()

reset_button = tk.Button(root, text="Play Again", command=reset_game, **button_style)
reset_button.pack(pady=6)

exit_button = tk.Button(root, text="Exit", command=exit_game, **button_style)
exit_button.pack(pady=6)

root.mainloop()
