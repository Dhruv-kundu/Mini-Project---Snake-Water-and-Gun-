import tkinter as tk
import random

# --- Game Logic ---
def computer_choice():
    return random.choice(['Snake', 'Water', 'Gun'])

def find_winner(player, comp):
    if player == comp:
        return "It's a Tie!"
    elif (player == 'Snake' and comp == 'Water') or \
         (player == 'Water' and comp == 'Gun') or \
         (player == 'Gun' and comp == 'Snake'):
        return "You Win!"
    else:
        return "Computer Wins!"

# --- Button Event ---
def play(choice):
    global player_score, computer_score

    comp = computer_choice()
    result = find_winner(choice, comp)

    result_label.config(text=f"Computer chose: {comp}\n{result}")

    if result == "You Win!":
        player_score += 1
    elif result == "Computer Wins!":
        computer_score += 1

    score_label.config(text=f"Your Score: {player_score} | Computer Score: {computer_score}")

# --- Reset Game ---
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Your Score: 0 | Computer Score: 0")

# --- Window Setup ---
root = tk.Tk()
root.title("Snake Water Gun Game 🐍💧🔫")
root.geometry("400x400")
root.config(bg="#f0f0f0")

player_score = 0
computer_score = 0

# --- Labels ---
title_label = tk.Label(root, text="🐍 Snake • 💧 Water • 🔫 Gun", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), bg="#f0f0f0", fg="#444")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333")
score_label.pack(pady=10)

# --- Buttons ---
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=20)

snake_btn = tk.Button(btn_frame, text="🐍 Snake", width=10, font=("Arial", 12, "bold"),
                      bg="#a3d977", command=lambda: play("Snake"))
snake_btn.grid(row=0, column=0, padx=10)

water_btn = tk.Button(btn_frame, text="💧 Water", width=10, font=("Arial", 12, "bold"),
                      bg="#7fd0f0", command=lambda: play("Water"))
water_btn.grid(row=0, column=1, padx=10)

gun_btn = tk.Button(btn_frame, text="🔫 Gun", width=10, font=("Arial", 12, "bold"),
                    bg="#f09595", command=lambda: play("Gun"))
gun_btn.grid(row=0, column=2, padx=10)

# --- Reset Button ---
reset_btn = tk.Button(root, text="🔁 Reset Game", font=("Arial", 12, "bold"),
                      bg="#ffcc66", command=reset_game)
reset_btn.pack(pady=20)

# --- Run the App ---
root.mainloop()
