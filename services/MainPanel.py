import tkinter as tk
from tkinter import ttk
from UserService import UserSservice

class PersonPanel(tk.Frame):

    def __init__(self, modelRef):


        self.db_reference = modelRef
        self.root = tk.Tk()
        self.tab_control = ttk.Notebook(self.root)

        self.create_panels(self.tab_control)

        self.root.mainloop()


    def create_panels(self):

        # first panel - manage person

        self.tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab, text="User Management")
        self.tab_control.pack(expand=1, fill="both")
        panel = PersonPanel(self.tab)
        panel.pack(fill="both", expand=1)

