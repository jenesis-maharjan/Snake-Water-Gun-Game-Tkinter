import tkinter as tk
import random

class SnakeWaterGunGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Water Gun Game")
        self.root.geometry("500x500")
        self.root.config(bg="#121212")

        # Scores
        self.user_score = 0
        self.comp_score = 0

        # Choices
        self.choices = ["Snake", "Water", "Gun"]

        self.create_widgets()

    # -------- Game Logic --------
    def get_winner(self, user, comp):
        if user == comp:
            return "Draw"

        if (user == "Snake" and comp == "Water") or \
           (user == "Water" and comp == "Gun") or \
           (user == "Gun" and comp == "Snake"):
            return "User"
        else:
            return "Computer"

    # -------- Play Function --------
    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        winner = self.get_winner(user_choice, comp_choice)

        # Update scores
        if winner == "User":
            self.user_score += 1
            result_text = "You Win! 🎉"
        elif winner == "Computer":
            self.comp_score += 1
            result_text = "Computer Wins! 🤖"
        else:
            result_text = "It's a Draw 🤝"

        # Update UI
        self.user_label.config(text=f"You chose: {user_choice}")
        self.comp_label.config(text=f"Computer chose: {comp_choice}")
        self.result_label.config(text=result_text)
        self.score_label.config(
            text=f"Score → You: {self.user_score} | Computer: {self.comp_score}"
        )

    # -------- Reset Game --------
    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.user_label.config(text="")
        self.comp_label.config(text="")
        self.result_label.config(text="Game Reset!")
        self.score_label.config(text="Score → You: 0 | Computer: 0")

    # -------- UI Setup --------
    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Snake 🐍 Water 💧 Gun 🔫",
            font=("Segoe UI", 18, "bold"),
            bg="#121212",
            fg="white"
        )
        title.pack(pady=20)

        # Score
        self.score_label = tk.Label(
            self.root,
            text="Score → You: 0 | Computer: 0",
            font=("Segoe UI", 12),
            bg="#121212",
            fg="#00FFAA"
        )
        self.score_label.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#121212")
        btn_frame.pack(pady=20)

        for i, choice in enumerate(self.choices):
            btn = tk.Button(
                btn_frame,
                text=choice,
                width=12,
                height=2,
                font=("Segoe UI", 10, "bold"),
                bg="#1f1f1f",
                fg="white",
                activebackground="#333",
                command=lambda c=choice: self.play(c)
            )
            btn.grid(row=0, column=i, padx=10)

        # Info Labels
        self.user_label = tk.Label(self.root, text="", font=("Segoe UI", 12),
                                  bg="#121212", fg="white")
        self.user_label.pack(pady=5)

        self.comp_label = tk.Label(self.root, text="", font=("Segoe UI", 12),
                                  bg="#121212", fg="white")
        self.comp_label.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Segoe UI", 14, "bold"),
                                    bg="#121212", fg="#FFD700")
        self.result_label.pack(pady=20)

        # Reset Button
        reset_btn = tk.Button(
            self.root,
            text="Reset Game",
            font=("Segoe UI", 10, "bold"),
            bg="#ff4d4d",
            fg="white",
            command=self.reset_game
        )
        reset_btn.pack(pady=10)


# -------- Run App --------
if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeWaterGunGame(root)
    root.mainloop()