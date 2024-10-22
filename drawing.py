import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(Fill=tk.BOTH, expand=True)

        self.color_lable = tk.Label(root, text="Color:")
        self.color_lable.pack(side=tk.LEFT, padx=10)

        self.color_var = tk.StringVar()
        self.color_var.set("black")

        self.color_entry = tk.Entry(root, textvariable=self.color_var)
        self.color_entry.pack(side=tk.LEFT, padx=10)

        self.thickness_lable = tk.Label(root, text="Thickness")
        self.thickness_lable.pack(side=tk.LEFT, padx=10)
        
        self.thickness_var = tk.IntVar()
        self.thickness_var.set(2)

        self.thickness_entry = tk.Entry(root, textvariable=self.thickness_var)
        self.thickness_entry.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(root, text="Clear canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.drawing = False
        self.last_x = None
        self.last_y = None

        def start_drawing(self, event):
            self.drawing = True
            self.last_x = event.x
            self.last_y = event.y

            def draw(self, event):
                if self.drawing:
                    x, y = event.x, event.y
                    if self.last_x and self.last_y:
                        color = self.color_var.get()
                        thickness = self.thickness_var.get()
                        self.canvas.create_line(
                            self.last_x, self.last_y, x, y, fill=color, width=thickness
                        )

                        self.last_x = x
                        self.last_y = y

                        def stop_drawing(self, event):
                            self.drawing = False
                            self.last_x = None
                            self.last_y = None

                            def clear_canvas(self):
                                self.canvas.delete("all")


if __name__ == "__drawing__":
    root = tk.TK()
    app = DrawingApp(root)
    root.mainloop()