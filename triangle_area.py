import tkinter as tk 
from tkinter import ttk
from PIL import ImageTk, Image

class TriangleArea(ttk.Frame): 
    def calculate_area(self, h, b):
        return int(h.get() * b.get() / 2)

    def __init__(self, parent, controller): 
          
        ttk.Frame.__init__(self, parent) 
        controller.topbar_component(self, "Calculating the Area of a Triangle",
                         "Please enter input for the height and the base to calculate the area of a triangle.")

        img = Image.open("triangle.png").resize((284,252))
        pic = ImageTk.PhotoImage(img)

        img_label = ttk.Label(self, image = pic )
        img_label.image = pic
        img_label.grid(row = 1, column = 0, padx = 10, pady = 10) 
        img_label.configure(anchor="center")
        
        input_form = ttk.Frame(self)
        input_form.grid(row=1, column=1, padx = 10, pady = 10, sticky="n")

        area_label = ttk.Label(input_form, text="Area")
        area_label.grid(row = 1, column = 1, sticky="ws")
        area = tk.StringVar()
        area.set("?")
        area_val_label = ttk.Label(input_form, textvariable=area, font=("Arial", 18))
        area_val_label.grid(row = 2, column = 1, sticky="n")

        height_label = ttk.Label(input_form, text="Height (h)")
        height_label.grid(row = 3, column = 1, sticky="ws", pady=(10, 0))
        height_var = tk.IntVar()
        height_entry = ttk.Entry(input_form, textvariable=height_var)
        height_entry.grid(row = 4, column = 1, sticky="wn")

        base_label = ttk.Label(input_form, text="Base (b)")
        base_label.grid(row = 5, column = 1, sticky="ws", pady=(10, 0))
        base_var = tk.IntVar()
        base_entry = ttk.Entry(input_form, textvariable=base_var)
        base_entry.grid(row = 6, column = 1, sticky="wn")

        calc_button = ttk.Button(input_form, text="Calculate Area",
                                 command = lambda: area.set(self.calculate_area(height_var, base_var)) )
        calc_button.grid(row = 7, column = 1, sticky="n", pady=(10, 0))  
