import sqlite3
import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox

class PlayerEdit(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self)
        self.parent = parent
        playerL1 = tk.Label(self,text="Edit Players", font=self.parent.titleFont)
        playerL1.grid(row=0, column=0)
        self.rowconfigure(1,minsize=30)
        playerL2 = tk.Label(self,text="ID:", font=self.parent.labelFont)
        playerL2.grid(row=2, column=0, sticky="E")
        playerL3 = tk.Label(self,text="First Name:", font=self.parent.labelFont)
        playerL3.grid(row=3, column=0, sticky="E")
        playerL4 = tk.Label(self,text="Surname:", font=self.parent.labelFont)
        playerL4.grid(row=4, column=0, sticky="E")
        playerL5 = tk.Label(self,text="Form:", font=self.parent.labelFont)
        playerL5.grid(row=5, column=0, sticky="E")

        self.playerID = tk.Entry(self,width=20, font=self.parent.entryFont)
        self.playerID.grid(row=2, column=1, sticky="W")
        self.playerFname = tk.Entry(self,width=20, font=self.parent.entryFont)
        self.playerFname.grid(row=3, column=1, sticky="W")
        self.playerSname = tk.Entry(self,width=20, font=self.parent.entryFont)
        self.playerSname.grid(row=4, column=1, sticky="W")
        self.playerForm = tk.Entry(self,width=20, font=self.parent.entryFont)
        self.playerForm.grid(row=5, column=1, sticky="W")
        self.columnconfigure(3, minsize=30)
        playerL6 = tk.Label(self,text="Select from list:", font=self.parent.labelFont)
        playerL6.grid(row=1,column=4, sticky="W")
        self.playerList = tk.Listbox(self,width=30, height=20)
        self.playerList.grid(row=2, column=4, sticky="NSEW", rowspan=5)

        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=9, column=0, columnspan = 9)
        saveButton = tk.Button(self.buttonFrame,text="Save", command=self.save)
        saveButton.grid(row=0, column=0, sticky="NW")
        newButton = tk.Button(self.buttonFrame,text="New", command=self.new)
        newButton.grid(row=0, column=1, sticky="NW")

        self.rowconfigure(7,weight=1)
        self.playerList.bind("<<ListboxSelect>>", self.selectPlayer)
        self.currentPlayer = 0


    def load(self):
        c = self.parent.db.cursor()
        results = c.execute("SELECT * FROM Players")
        self.currentPupils = results.fetchall()
        for p in self.currentPupils:
            self.playerList.insert(tk.END,str(p[0]).ljust(5," ") + (p[1]+" "+p[2]).ljust(20," ") + p[3])

    def selectPlayer(self,e):
        selectedplayer = self.currentPupils[self.playerList.curselection()[0]]
        self.playerForm.delete(0, tk.END)
        self.playerForm.insert(0,selectedplayer[3])
        self.playerSname.delete(0, tk.END)
        self.playerSname.insert(0,selectedplayer[2])
        self.playerFname.delete(0, tk.END)
        self.playerFname.insert(0,selectedplayer[1])
        self.playerID.delete(0, tk.END)
        self.playerID.insert(0,selectedplayer[0])

    def save(self):
        pass


    def new(self):
        pass