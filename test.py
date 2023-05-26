import tkinter as tk

def open_calculator():
    
    calc = tk.Tk()
    calc.title("Calculator")
    

    buttons = [
    '7',  '8',  '9',  '*',  'C',
    '4',  '5',  '6',  '/',  'Neg',
    '1',  '2',  '3',  '-',  '$',
    '0',  '.',  '=',  '+',  '@' ]

    # set up GUI
    row = 1
    col = 0
    for i in buttons:
        button_style = 'raised'
        action = lambda x = i: click_event(x)
        tk.Button(calc, text = i, width = 7, height = 7, relief = button_style, command = action) \
            .grid(row = row, column = col, sticky = 'nesw', )
        col += 1
        if col > 4:
            col = 0
            row += 1

    display = tk.Entry(calc, width = 40, bg = "white",font=("Arial 24"))
    display.grid(row = 0, column = 0, columnspan = 5)

    def click_event(key):

        # = -> calculate results
        if key == '=':
            # safeguard against integer division
            if '/' in display.get() and '.' not in display.get():
                display.insert(tk.END, ".0")
                
            # attempt to evaluate results
            try:
                result = eval(display.get())
                display.insert(tk.END, " = " + str(result))
            except:
                display.insert(tk.END, "   Error, use only valid chars")
                
        # C -> clear display		
        elif key == 'C':
            display.delete(0, tk.END)
            
            
        # $ -> clear display		
        elif key == '$':
            display.delete(0, tk.END)
            display.insert(tk.END, "$$$$C.$R.$E.$A.$M.$$$$")
            

        # @ -> clear display		
        elif key == '@':
            display.delete(0, tk.END)
            display.insert(tk.END, "wwwwwwwwwwwwwwwwebsite")		

            
        # neg -> negate term
        elif key == 'neg':
            if '=' in display.get():
                display.delete(0, tk.END)
            try:
                if display.get()[0] == '-':
                    display.delete(0)
                else:
                    display.insert(0, '-')
            except IndexError:
                pass

        # clear display and start new input		
        else:
            if '=' in display.get():
                display.delete(0, tk.END)
            display.insert(tk.END, key)

    # RUNTIME
    calc.mainloop()


# Define a function to open the whiteboard application


def open_whiteboard():
    import tkinter as tk

    class Whiteboard:
        def __init__(self, master):
            self.master = master
            master.title("Whiteboard")

            # Initialize variables
            self.x_pos = None
            self.y_pos = None
            self.color = 'black'

            # Create the canvas
            self.canvas = tk.Canvas(master, bg='white', width=400, height=400)
            self.canvas.pack(expand=True, fill='both')

            # Create the color buttons
            self.color_frame = tk.Frame(master)
            self.color_frame.pack(pady=10)
            colors = ['black', 'red', 'green', 'blue', 'purple']
            for color in colors:
                button = tk.Button(self.color_frame, bg=color, width=3, height=1,
                                command=lambda color=color: self.set_color(color))
                button.pack(side='left', padx=5)

            # Create the clear button
            self.clear_button = tk.Button(master, text='Clear', font=('Arial', 20),
                                        command=self.clear_canvas)
            self.clear_button.pack(pady=10)

            # Bind mouse events to the canvas
            self.canvas.bind('<Button-1>', self.start_draw)
            self.canvas.bind('<B1-Motion>', self.draw)
            self.canvas.bind('<ButtonRelease-1>', self.stop_draw)

        def start_draw(self, event):
            # Record the starting position of the mouse
            self.x_pos = event.x
            self.y_pos = event.y

        def draw(self, event):
            # Draw a line from the last recorded position to the current position
            if self.x_pos and self.y_pos:
                self.canvas.create_line(self.x_pos, self.y_pos, event.x, event.y,
                                        width=5, fill=self.color, capstyle='round',
                                        smooth=True)
            # Update the last recorded position
            self.x_pos = event.x
            self.y_pos = event.y

        def stop_draw(self, event):
            # Reset the starting position of the mouse
            self.x_pos = None
            self.y_pos = None

        def set_color(self, color):
            # Set the color of the pen
            self.color = color

        def clear_canvas(self):
            # Clear the canvas
            self.canvas.delete('all')

    # Create the main window
    root = tk.Tk()

    # Create the whiteboard
    board = Whiteboard(root)

    # Start the application
    root.mainloop()


# Define a function to open the stopwatch application


def open_todo():
    
    def add_item():
        todo_item = todo_entry.get()
        if todo_item:
            todo_listbox.insert(tk.END, todo_item)
            todo_entry.delete(0, tk.END)

    def remove_item():
        selected_item = todo_listbox.curselection()
        if selected_item:
            todo_listbox.delete(selected_item)

    root = tk.Tk()
    root.geometry("700x600")
    root.title("Todo List")

    todo_label = tk.Label(root, text="Enter a task:")
    todo_label.config(font=("Arial",20))
    todo_label.pack()

    todo_entry = tk.Entry(root,width=40,font=("Arial 24"))
    todo_entry.pack()

    add_button = tk.Button(root, text="Add Task", command=add_item)
    add_button.config(font=("Arial",20))
    add_button.pack()

    todo_listbox = tk.Listbox(root,width=40,font=("Arial 24"))
    todo_listbox.pack()

    remove_button = tk.Button(root, text="Remove Task", command=remove_item,font=("Arial 18"))
    remove_button.pack()

    root.mainloop()


# Define a function to open the BMI calculator application


def open_bmi_calculator():


    def calculate_bmi():
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = round(weight / (height ** 2), 2)  
        result_label.config(text=f"Your BMI is {bmi}")

    root = tk.Tk()
    root.title("BMI Calculator")
    root.geometry("500x300")
    height_label = tk.Label(root, text="Enter your height (in meters):",font=("Arial 30"))
    height_label.pack()

    height_entry = tk.Entry(root,width=30,font=("Arial 34"))
    height_entry.pack()

    weight_label = tk.Label(root, text="Enter your weight (in kg):",font=("Arial 30"))
    weight_label.pack()

    weight_entry = tk.Entry(root,width=30,font=("Arial 34"))
    weight_entry.pack()

    calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi,font=("Arial 15"))
    calculate_button.pack()

    result_label = tk.Label(root,font=("Arial 20"))
    result_label.pack()

    root.mainloop() 


# Define a function to open the tic tac toe game application


def open_tic_tac_toe():


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

# Define a function to open the notepad application


def open_notepad():
    
    root = tk.Tk()
    root.title("Notepad")
    
    # Define dimensions for the notepad
    width = 500
    height = 500

    # Set the background color for the notepad
    root.configure(bg="yellow")

    # Create a frame to contain the text widget
    frame = tk.Frame(root, borderwidth=2, relief="groove", bg="yellow")
    frame.pack(fill="both", expand=True)

    # Create the text widget for the notepad
    text = tk.Text(frame, borderwidth=0, highlightthickness=0, bg="yellow")
    text.pack(side="left", fill="both", expand=True)

    # Create a scrollbar for the text widget
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=text.yview)
    scrollbar.pack(side="right", fill="y")

    # Link the scrollbar to the text widget
    text.config(yscrollcommand=scrollbar.set)

    # Set the dimensions for the notepad window
    root.geometry(f"{width}x{height}")

    # Start the main loop for the GUI
    root.mainloop()


# Create the main window
root = tk.Tk()

# Set the window title and size
root.title("TOOLS TOGETHER")
root.geometry("760x400")

# Create six buttons, each with a different label and command
calculator_button = tk.Button(root, text="Calculator", command=open_calculator, width=30, height=10)
whiteboard_button = tk.Button(root, text="Whiteboard", command=open_whiteboard, width=30, height=10)
todo_button = tk.Button(root, text="Todo-list", command=open_todo, width=30, height=10)
bmi_calculator_button = tk.Button(root, text="BMI Calculator", command=open_bmi_calculator, width=30, height=10)
tic_tac_toe_button = tk.Button(root, text="Tic Tac Toe", command=open_tic_tac_toe, width=30, height=10)
notepad_button = tk.Button(root, text="Notepad", command=open_notepad, width=30, height=10)

# Add the buttons to the window using the grid layout manager
calculator_button.grid(row=0, column=0, padx=10, pady=10)
whiteboard_button.grid(row=0, column=1, padx=10, pady=10)
todo_button.grid(row=0, column=2, padx=10, pady=10)
bmi_calculator_button.grid(row=1, column=0, padx=10, pady=10)
tic_tac_toe_button.grid(row=1, column=1, padx=10, pady=10)
notepad_button.grid(row=1, column=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()