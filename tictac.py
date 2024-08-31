import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Initialize variables 
        self.current_player = 'X'
        self.winner = False
        self.moves = 0

        # Create the game board
        self.board = [' ']*9

        # Create the game buttons
        self.buttons = []
        for i in range(9):
            button = tk.Button(master, text='', font=('Arial', 50), width=3, height=1,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Create the reset button
        self.reset_button = tk.Button(master, text='Reset', font=('Arial', 20),
                                      command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def button_click(self, index):
        # Check if the move is valid
        if self.board[index] == ' ' and not self.winner:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            self.moves += 1
            # Check for a winner
            if self.check_winner():
                self.winner = True
                self.show_winner()
            # Switch to the other player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        elif not self.winner:
            print("Invalid move. Try again.")

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True
        # No winner
        return False

    def show_winner(self):
        # Create the winner message
        message = f"Player {self.current_player} wins!"
        # Show the message in a pop-up window
        popup = tk.Toplevel()
        popup.title("Winner!")
        tk.Label(popup, text=message, font=('Arial', 20)).pack(padx=20, pady=20)

    def reset_game(self):
        # Reset the game board and buttons
        self.board = [' ']*9
        for button in self.buttons:
            button.config(text='')
        # Reset variables
        self.current_player = 'X'
        self.winner = False
        self.moves = 0

# Create the main window
root = tk.Tk()

# Create the Tic Tac Toe game
game = TicTacToe(root)

# Start the game
root.mainloop()
