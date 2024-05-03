import tkinter as tk
from tkinter import ttk
from view.UserPanel import PersonPanel


class ApplicationTabs():
    def __init__(self, controller):

        self.controller = controller
        root = tk.Tk()
        tab_control = ttk.Notebook(root)
        # add the user view as a tab
        self.create_user_view(tab_control)

        root.mainloop()

    def create_user_view(self, tab_control):
        # Top Section
        person_tab = ttk.Frame(tab_control)
        tab_control.add(person_tab, text="Person")
        tab_control.pack(expand=True, fill="both")
        person_panel = PersonPanel(person_tab, self.controller)
        person_panel.pack(expand=True, fill="both")


# Example usage
