import tkinter as tk
from tkinter import ttk
import services.UserService as user_services


class PersonPanel(tk.Frame):
    def __init__(self, master,controller , *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.controller = controller
        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        # Top Section
        self.top_section = tk.Frame(self)
        self.top_section.grid(row=0, column=0, sticky="nsew", pady=10)

        labels = ["ID", "Name", "Address Line 1", "Town/City", "Postcode", "Telephone", "Tax Ref", "Timestamp"]
        self.entry_vars = {}
        for i, label in enumerate(labels):
            label = tk.Label(self.top_section, text=label)
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            entry_var = tk.StringVar()
            entry = tk.Entry(self.top_section, textvariable=entry_var)
            entry.grid(row=i, column=1, sticky="ew", padx=10, pady=5)
            self.entry_vars[label.cget("text")] = entry_var

        # CRUD Buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=1, column=0, sticky="nsew")

        crud_buttons = [("Create", self.create_person), ("Read", self.read_person), ("Update", self.update_person),
                        ("Delete", self.delete_person), ("Refresh", self.populate_table)]
        for i, (text, command) in enumerate(crud_buttons):
            button = tk.Button(self.button_frame, text=text, command=command)
            button.grid(row=0, column=i, sticky="ew")

        # Table
        #[1, 'John Doe', '123 Main St', 'Anytown', '12345', '555-1234', '123-456-789', '2022-02-16']

        self.table = ttk.Treeview(self, columns=["ID", "Name", "Address Line 1","Postcode","Telephone","Tax Ref", "Timestamp"])
        self.table.grid(row=2, column=0, sticky="nsew")
        self.table.heading("#0", text="ID")
        for column in self.table["columns"]:
            self.table.heading(column, text=column)
        self.table.bind("<ButtonRelease-1>", self.on_table_click)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_person(self):
        pass

    def read_person(self):
        pass

    def update_person(self):
        pass

    def delete_person(self):
        pass

    def populate_table(self):
        # Dummy data for demonstration
        data = self.controller.user_service.get_all_person()

        self.table.delete(*self.table.get_children())
        for row in data:

            self.table.insert("", "end", values=row.get_data())

    def on_table_click(self, event):
        selected_item = self.table.selection()
        if selected_item:
            values = self.table.item(selected_item, "values")
            for label, value in zip(["ID", "Name", "Address Line 1", "Timestamp"], values):
                self.entry_vars[label].set(value)


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    tab_control = ttk.Notebook(root)

    person_tab = ttk.Frame(tab_control)
    tab_control.add(person_tab, text="Person")
    tab_control.pack(expand=True, fill="both")

    person_panel = PersonPanel(person_tab)
    person_panel.pack(expand=True, fill="both")

    root.mainloop()
