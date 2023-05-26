import tkinter as tk

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
