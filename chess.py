import sqlite3
import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
from playerFrame import PlayerEdit




class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.titleFont =  tkFont.Font(family="Arial", size=20, slant="italic")
        self.labelFont =  tkFont.Font(family="Arial", size=16)
        self.entryFont =  tkFont.Font(family="Consolas", size=16)
        self.geometry("800x800+100+100")
        self.title("Chess Manager")
        self.menuButton = tk.Button(self,text="Menu")
        self.menuButton.grid(row=0, column=0, sticky="NW")

        self.db = sqlite3.connect("chess.db")


        self.frames= [PlayerEdit(self) ]

        self.demoData()
        self.switchScreen(0)
        self.mainloop()

    def switchScreen(self,screen):
        self.frames[screen].grid(row=2,column=0,sticky="NSEW")
        self.frames[screen].load()

    def demoData(self):
            c = self.db.cursor()
            c.execute("DELETE from Players")
            c.execute("INSERT INTO Players VALUES (NULL, 'Sally', 'Smith', '07KFR')")
            self.db.commit()

main = App()
