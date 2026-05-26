import tkinter as tk
from game_logic import check_winner, computer_move


class TicTacToeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("700x860")
        self.root.resizable(False, False)
        self.root.config(bg="#0f172a")

        self.current_player = "X"
        self.board = [""] * 9
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.game_mode = "computer"

        self.buttons = []
        self.status = None
        self.score_label = None

        self.start_page()

    def run(self):
        self.root.mainloop()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def hover(self, btn, normal, hover_color):
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=normal))

    def start_page(self):
        self.clear_window()

        tk.Label(
            self.root,
            text="Tic Tac Toe",
            font=("Segoe UI", 34, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        ).pack(pady=60)

        tk.Label(
            self.root,
            text="Choose Game Mode",
            font=("Segoe UI", 18, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=20)

        computer_btn = tk.Button(
            self.root,
            text="🤖 Play with Computer",
            font=("Segoe UI", 16, "bold"),
            bg="#2563eb",
            fg="white",
            width=24,
            height=2,
            relief="raised",
            bd=5,
            command=lambda: self.start_game("computer")
        )
        computer_btn.pack(pady=15)
        self.hover(computer_btn, "#2563eb", "#1d4ed8")

        friend_btn = tk.Button(
            self.root,
            text="👥 Play with Friend",
            font=("Segoe UI", 16, "bold"),
            bg="#16a34a",
            fg="white",
            width=24,
            height=2,
            relief="raised",
            bd=5,
            command=lambda: self.start_game("friend")
        )
        friend_btn.pack(pady=15)
        self.hover(friend_btn, "#16a34a", "#15803d")

        exit_btn = tk.Button(
            self.root,
            text="Exit",
            font=("Segoe UI", 13, "bold"),
            bg="#dc2626",
            fg="white",
            width=14,
            relief="raised",
            bd=4,
            command=self.root.destroy
        )
        exit_btn.pack(pady=35)
        self.hover(exit_btn, "#dc2626", "#b91c1c")

    def start_game(self, mode):
        self.game_mode = mode
        self.board = [""] * 9
        self.current_player = "X"
        self.game_page()

    def game_page(self):
        self.clear_window()

        tk.Label(
            self.root,
            text="Tic Tac Toe Pro",
            font=("Segoe UI", 30, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        ).pack(pady=20)

        mode_text = "Mode: Computer" if self.game_mode == "computer" else "Mode: Friend"

        tk.Label(
            self.root,
            text=mode_text,
            font=("Segoe UI", 13, "bold"),
            bg="#0f172a",
            fg="#c084fc"
        ).pack()

        self.status = tk.Label(
            self.root,
            text="Player X Turn",
            font=("Segoe UI", 17, "bold"),
            bg="#0f172a",
            fg="#a7f3d0"
        )
        self.status.pack(pady=10)

        self.score_label = tk.Label(
            self.root,
            text=f"X: {self.scores['X']}     O: {self.scores['O']}     Draw: {self.scores['Draw']}",
            font=("Segoe UI", 15, "bold"),
            bg="#0f172a",
            fg="white"
        )
        self.score_label.pack(pady=8)

        board_frame = tk.Frame(self.root, bg="#0f172a")
        board_frame.pack(pady=20)

        self.buttons = []

        for i in range(9):
            btn = tk.Button(
                board_frame,
                text="",
                font=("Segoe UI", 30, "bold"),
                width=4,
                height=2,
                bg="#1e293b",
                fg="white",
                activebackground="#334155",
                activeforeground="white",
                relief="raised",
                bd=6,
                command=lambda i=i: self.button_click(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=8, pady=8)
            self.hover(btn, "#1e293b", "#334155")
            self.buttons.append(btn)

        control_frame = tk.Frame(self.root, bg="#0f172a")
        control_frame.pack(pady=15)

        restart_btn = tk.Button(
            control_frame,
            text="Restart",
            font=("Segoe UI", 12, "bold"),
            bg="#2563eb",
            fg="white",
            width=12,
            relief="raised",
            bd=4,
            command=self.reset_board
        )
        restart_btn.grid(row=0, column=0, padx=8)
        self.hover(restart_btn, "#2563eb", "#1d4ed8")

        menu_btn = tk.Button(
            control_frame,
            text="Main Menu",
            font=("Segoe UI", 12, "bold"),
            bg="#9333ea",
            fg="white",
            width=12,
            relief="raised",
            bd=4,
            command=self.start_page
        )
        menu_btn.grid(row=0, column=1, padx=8)
        self.hover(menu_btn, "#9333ea", "#7e22ce")

        reset_btn = tk.Button(
            control_frame,
            text="Reset Score",
            font=("Segoe UI", 12, "bold"),
            bg="#dc2626",
            fg="white",
            width=12,
            relief="raised",
            bd=4,
            command=self.reset_all
        )
        reset_btn.grid(row=0, column=2, padx=8)
        self.hover(reset_btn, "#dc2626", "#b91c1c")

    def update_score(self):
        self.score_label.config(
            text=f"X: {self.scores['X']}     O: {self.scores['O']}     Draw: {self.scores['Draw']}"
        )

    def highlight_winner(self, pos):
        for i in pos:
            self.buttons[i].config(bg="#22c55e", fg="white")

    def reset_board(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.status.config(text="Player X Turn", fg="#a7f3d0")

        for btn in self.buttons:
            btn.config(
                text="",
                bg="#1e293b",
                fg="white",
                state="normal"
            )

    def reset_all(self):
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.update_score()
        self.reset_board()

    def show_result_popup(self, message, color):
        popup = tk.Toplevel(self.root)
        popup.title("Game Result")
        popup.geometry("380x280")
        popup.resizable(False, False)
        popup.config(bg="#020617")
        popup.grab_set()

        popup.update_idletasks()
        x = self.root.winfo_x() + 160
        y = self.root.winfo_y() + 260
        popup.geometry(f"+{x}+{y}")

        shadow = tk.Frame(
            popup,
            bg="#000000"
        )
        shadow.place(x=35, y=35, width=310, height=205)

        card = tk.Frame(
            popup,
            bg="#1e293b",
            bd=8,
            relief="raised"
        )
        card.place(x=25, y=25, width=310, height=205)

        tk.Label(
            card,
            text="🎉 Game Over 🎉",
            font=("Segoe UI", 20, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        ).pack(pady=18)

        tk.Label(
            card,
            text=message,
            font=("Segoe UI", 18, "bold"),
            bg="#1e293b",
            fg=color
        ).pack(pady=8)

        ok_btn = tk.Button(
            card,
            text="OK",
            font=("Segoe UI", 12, "bold"),
            bg="#2563eb",
            fg="white",
            width=12,
            relief="raised",
            bd=5,
            command=popup.destroy
        )
        ok_btn.pack(pady=15)
        self.hover(ok_btn, "#2563eb", "#1d4ed8")

    def end_game(self, winner=None, win_pos=None):
        if winner:
            self.scores[winner] += 1
            self.highlight_winner(win_pos)

            color = "#38bdf8" if winner == "X" else "#f472b6"
            self.show_result_popup(f"Player {winner} Wins!", color)
        else:
            self.scores["Draw"] += 1
            self.show_result_popup("It's a Draw!", "#facc15")

        self.update_score()
        self.root.after(1000, self.reset_board)

    def make_computer_move(self):
        move = computer_move(self.board)
        if move is not None:
            self.button_click(move)

    def button_click(self, i):
        if self.board[i] != "":
            return

        self.board[i] = self.current_player

        color = "#38bdf8" if self.current_player == "X" else "#f472b6"

        self.buttons[i].config(
            text=self.current_player,
            fg=color,
            state="disabled",
            disabledforeground=color
        )

        win_pos = check_winner(self.board)

        if win_pos:
            self.root.after(300, lambda: self.end_game(self.current_player, win_pos))
            return

        if "" not in self.board:
            self.root.after(300, lambda: self.end_game())
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status.config(text=f"Player {self.current_player} Turn")

        if self.game_mode == "computer" and self.current_player == "O":
            self.root.after(500, self.make_computer_move)