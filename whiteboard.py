import tkinter as tk

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Paint App")
        
        # Create a canvas widget
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create a toolbar frame
        self.toolbar = tk.Frame(self.master, pady=5)
        self.toolbar.pack(fill=tk.X)
        
        # Create color buttons
        colors = ["black", "red", "green", "blue"]
        self.color_btns = []
        for color in colors:
            btn = tk.Button(self.toolbar, bg=color, width=2, command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=5)
            self.color_btns.append(btn)
        
        # Create brush and eraser buttons
        self.brush_btn = tk.Button(self.toolbar, text="Brush", width=6, command=self.use_brush)
        self.brush_btn.pack(side=tk.LEFT, padx=5)
        
        self.eraser_btn = tk.Button(self.toolbar, text="Eraser", width=6, command=self.use_eraser)
        self.eraser_btn.pack(side=tk.LEFT, padx=5)
        
        # Create clear button
        self.clear_btn = tk.Button(self.toolbar, text="Clear", width=6, command=self.clear_canvas)
        self.clear_btn.pack(side=tk.RIGHT, padx=5)
        
        # Set default values
        self.color = "black"
        self.brush_size = 5
        self.eraser_size = 5
        self.active_button = self.brush_btn
        
        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.release)
    
    def set_color(self, color):
        self.color = color
    
    def use_brush(self):
        self.active_button.config(relief=tk.RAISED)
        self.active_button = self.brush_btn
        self.active_button.config(relief=tk.SUNKEN)
        self.canvas.config(cursor="plus")
        
    def use_eraser(self):
        self.active_button.config(relief=tk.RAISED)
        self.active_button = self.eraser_btn
        self.active_button.config(relief=tk.SUNKEN)
        self.canvas.config(cursor="dot")
        
    def clear_canvas(self):
        self.canvas.delete("all")
    
    def draw(self, event):
        if self.active_button == self.brush_btn:
            self.canvas.create_oval(event.x - self.brush_size, event.y - self.brush_size,
                                    event.x + self.brush_size, event.y + self.brush_size,
                                    fill=self.color, outline=self.color)
        elif self.active_button == self.eraser_btn:
            self.canvas.create_rectangle(event.x - self.eraser_size, event.y - self.eraser_size,
                                          event.x + self.eraser_size, event.y + self.eraser_size,
                                          fill="white", outline="white")
    
    def release(self, event):
        pass

root = tk.Tk()
app = PaintApp(root)
root.mainloop()
