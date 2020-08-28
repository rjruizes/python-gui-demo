import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

from triangle_area import TriangleArea
from triangle_side import TriangleSide
from seconds_converter import SecondsConverter
from string_repeater import StringRepeater

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class tkinterApp(tk.Tk): 
    def __init__(self, *args, **kwargs):  
        tk.Tk.__init__(self, *args, **kwargs) 
          
        container = ttk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 

        self.frames = {}   

        for F in (StartPage, TriangleArea, TriangleSide, SecondsConverter, StringRepeater): 
            frame = F(container, self)
            self.frames[F] = frame  
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(StartPage)

    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise()

    def topbar_component(self, frame, title_str, help_str):
        topbar = ttk.Frame(frame)
        topbar.grid(row=0, column=0, columnspan=2, padx = 10, pady = (10, 20), sticky="new")

        back_button = ttk.Button(topbar, text ="Back",
                            command = lambda : self.show_frame(StartPage)) 
        back_button.grid(row = 0, column = 0, sticky="w")
        title = ttk.Label(topbar, text=title_str)
        title.configure(anchor="center")
        title.grid(row = 0, column = 1, sticky="ew")
        help_button = ttk.Button(topbar, text="Help",
                                 command = lambda : showinfo("Help", help_str))
        help_button.grid(row = 0, column = 2, sticky="e")

        topbar.grid_rowconfigure(0, weight = 1) 
        topbar.grid_columnconfigure(1, weight = 1) 
   
class StartPage(ttk.Frame): 
    def __init__(self, parent, controller):  
        ttk.Frame.__init__(self, parent)

        app_title = ttk.Label(self, text="A Python Programming Assessment", font=("Arial", 20)) 
        app_author = ttk.Label(self, text="Roman Ruiz-Esparza - Aug 28, 2020")
        app_title.configure(anchor="center")
        app_title.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="s")
        app_author.configure(anchor="center")
        app_author.grid(row = 1, column = 0, padx = 10, pady = (10, 0), sticky="n")
        button1 = ttk.Button(self, text ="Area of a Triangle", width = 30,
                             command = lambda : controller.show_frame(TriangleArea)) 
        button1.grid(row = 2, column = 0, padx = 10, pady = (5, 5), ipady=8)
        button2 = ttk.Button(self, text ="Maximum Edge of a Triangle", width = 30,
                             command = lambda : controller.show_frame(TriangleSide))
        button2.grid(row = 3, column = 0, padx = 10, pady = 5, ipady=8)
        button3 = ttk.Button(self, text ="Hours & Minutes to Seconds", width = 30, 
                             command = lambda : controller.show_frame(SecondsConverter))
        button3.grid(row = 4, column = 0, padx = 10, pady = 5, ipady=8)
        button4 = ttk.Button(self, text ="Repeat String n Times", width = 30,
                             command = lambda : controller.show_frame(StringRepeater))
        button4.grid(row = 5, column = 0, padx = 10, pady = (5, 15), ipady=8)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 2)
        self.grid_columnconfigure(0, weight = 1) 

win = tkinterApp()

center(win)
win.attributes("-topmost", True)

win.mainloop() 