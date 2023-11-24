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


        self.frames= [PlayerEdit(self) ] # Make instances of all the different screens, and store them in a list

        self.demoData() # this creates a single user. This would normally be commented out
        self.switchScreen(0)
        self.mainloop()

    def switchScreen(self,screen):
        for s in self.frames:  # go through each screen and make it forget its grid position, effectively hiding it
            s.grid_forget()
        self.frames[screen].grid(row=2,column=0,sticky="NSEW") # this puts the new screen on the grid, so it is visible
        self.frames[screen].load()  # because the new screen might need to refresh its data, they all need a load method

    def demoData(self):  # this just deletes old data and creates a person, for test purposes. This would not nornally be run
            c = self.db.cursor()
            c.execute("DELETE from Players")
            c.execute("INSERT INTO Players VALUES (NULL, 'Sally', 'Smith', '07KFR')")
            self.db.commit()

main = App()
