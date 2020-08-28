
import tkinter as tk 
from tkinter import ttk

def calculate_max_third_side(s1, s2):  
    s1 = s1.get(); s2 = s2.get()
    # Not a valid triangle  
    if (s1 <= 0 or s2 <= 0):
        print(-1, end = "") 
        return
    max_length = s1 + s2 - 1
    min_length = max(s1, s2) - min(s1, s2) + 1
    # Not a valid triangle  
    if (min_length > max_length):
        print(-1, end = "")
        return
    return max_length


class TriangleSide(ttk.Frame):  
    def __init__(self, parent, controller): 
        ttk.Frame.__init__(self, parent)

        controller.topbar_component(self, "Calculating the Maximum Edge of a Triangle",
                         "Please enter input for two sides of a triangle to calculate the maximum size of the third side.")

        input_form = ttk.Frame(self)
        input_form.grid(row=1, column=0, padx = 10, sticky="n")

        height_label = ttk.Label(input_form, text="Side 1")
        height_label.grid(row = 1, column = 0, sticky="ws")
        side1_var = tk.IntVar()
        height_entry = ttk.Entry(input_form, textvariable=side1_var)
        height_entry.grid(row = 2, column = 0, sticky="wn")

        base_label = ttk.Label(input_form, text="Side 2")
        base_label.grid(row = 3, column = 0, sticky="ws", pady=(10, 0))
        side2_var = tk.IntVar()
        base_entry = ttk.Entry(input_form, textvariable=side2_var)
        base_entry.grid(row = 4, column = 0, sticky="wn")

        area_label = ttk.Label(input_form, text="Side 3")
        area_label.grid(row = 5, column = 0, sticky="ws", pady=(10, 0))
        area = tk.StringVar()
        area.set("?")
        area_val_label = ttk.Label(input_form, textvariable=area, font=("Arial", 18))
        area_val_label.grid(row = 6, column = 0, sticky="n")

        calc_button = ttk.Button(input_form, text="Calculate Max",
                                 command = lambda: area.set(calculate_max_third_side(side1_var, side2_var)) )
        calc_button.grid(row = 7, column = 0, sticky="n", pady=(10, 0))

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)