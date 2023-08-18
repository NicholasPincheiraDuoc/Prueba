import tkinter as tk
from tkinter import ttk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.pen_color = "black"
        
        self.pen_button = ttk.Button(self.root, text="Pen Color", command=self.change_pen_color)
        self.pen_button.pack()
        
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        
        self.drawing = False
        self.last_x = 0
        self.last_y = 0
        
    def start_drawing(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y
        
    def draw(self, event):
        if self.drawing:
            x = event.x
            y = event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pen_color)
            self.last_x = x
            self.last_y = y
            
    def stop_drawing(self, event):
        self.drawing = False
        
    def change_pen_color(self):
        color = tk.colorchooser.askcolor()[1]
        if color:
            self.pen_color = color

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()