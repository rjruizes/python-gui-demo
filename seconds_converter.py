import tkinter as tk 
from tkinter import ttk

def calc_seconds(hours, minutes):
    hour_in_sec = 60*60*hours.get()
    min_in_sec = 60*minutes.get()
    return hour_in_sec + min_in_sec

class SecondsConverter(ttk.Frame):  
    def __init__(self, parent, controller): 
        ttk.Frame.__init__(self, parent)

        controller.topbar_component(self, "Convert hours and minutes into seconds",
                         "Please enter input for the hours and minutes to calculate the number of seconds.")

        input_form = ttk.Frame(self)
        input_form.grid(row=1, column=0, padx = 10, sticky="n")

        height_label = ttk.Label(input_form, text="Hours")
        height_label.grid(row = 1, column = 0, sticky="ws")
        hours_var = tk.IntVar()
        height_entry = ttk.Entry(input_form, textvariable=hours_var)
        height_entry.grid(row = 2, column = 0, sticky="wn")

        base_label = ttk.Label(input_form, text="Minutes")
        base_label.grid(row = 3, column = 0, sticky="ws", pady=(10, 0))
        minutes_var = tk.IntVar()
        base_entry = ttk.Entry(input_form, textvariable=minutes_var)
        base_entry.grid(row = 4, column = 0, sticky="wn")

        area_label = ttk.Label(input_form, text="Seconds")
        area_label.grid(row = 5, column = 0, sticky="ws", pady=(10, 0))
        area = tk.StringVar()
        area.set("?")
        area_val_label = ttk.Label(input_form, textvariable=area, font=("Arial", 18))
        area_val_label.grid(row = 6, column = 0, sticky="n")

        calc_button = ttk.Button(input_form, text="Calculate Seconds",
                                 command = lambda: area.set(calc_seconds(hours_var, minutes_var)) )
        calc_button.grid(row = 7, column = 0, sticky="n", pady=(10, 0))

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)