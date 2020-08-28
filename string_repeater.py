import tkinter as tk 
from tkinter import ttk
import tkinter.scrolledtext as st

def repetition(val, n):
    if(n == 0): return ""
    if(n == 1): return val
    return val + repetition(val, n-1)

class StringRepeater(ttk.Frame):
    def update_text(self, string_var, n_var):
        self.text.delete("1.0","end")
        self.text.insert(tk.END, repetition(string_var.get(), n_var.get()))

    def __init__(self, parent, controller): 
        ttk.Frame.__init__(self, parent)

        controller.topbar_component(self, "Repeat string n times",
                         "Please enter input for the string and number of times to print it.")

        input_form = ttk.Frame(self)
        input_form.grid(row=1, column=0, padx = 10, sticky="n")

        height_label = ttk.Label(input_form, text="string")
        height_label.grid(row = 1, column = 0, sticky="ws")
        string_var = tk.StringVar()
        height_entry = ttk.Entry(input_form, textvariable=string_var)
        height_entry.grid(row = 2, column = 0, sticky="wn")

        base_label = ttk.Label(input_form, text="n")
        base_label.grid(row = 3, column = 0, sticky="ws", pady=(10, 0))
        n_var = tk.IntVar()
        base_entry = ttk.Entry(input_form, textvariable=n_var)
        base_entry.grid(row = 4, column = 0, sticky="wn")

        area_label = ttk.Label(input_form, text="Output")
        area_label.grid(row = 5, column = 0, sticky="ws", pady=(10, 0))
        output_var = tk.StringVar()
        self.text = st.ScrolledText(input_form, width=30, height=4)
        self.text.grid(row = 6, column = 0, sticky="n")

        calc_button = ttk.Button(input_form, text="Print",
                                 command = lambda: self.update_text(string_var, n_var) )
        calc_button.grid(row = 7, column = 0, sticky="n", pady=(10, 0))

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
