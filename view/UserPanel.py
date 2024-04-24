import tkinter as tk
from tkinter import ttk


class Person:
    def __init__(self, id, name, addressLine1, townCity, postcode, telephone, taxRef, timestamp):
        self.id = id
        self.name = name
        self.addressLine1 = addressLine1
        self.townCity = townCity
        self.postcode = postcode
        self.telephone = telephone
        self.taxRef = taxRef
        self.timestamp = timestamp


class PersonDialog:
    def __init__(self, root):
        self.root = root
        self.root.title("Person Management")

        self.person_list = [
            Person(1, "John Doe", "123 Main St", "Anytown", "ABC123", "1234567890", "T123456", "2024-04-12"),
            Person(2, "Jane Smith", "456 Elm St", "Othertown", "XYZ789", "0987654321", "T987654", "2024-04-12")
        ]

        self.selected_person = None

        self.create_widgets()

    def create_widgets(self):
        # Top Frame
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.BOTH, expand=True)

        # CRUD Buttons
        crud_frame = tk.Frame(top_frame)
        crud_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Button(crud_frame, text="Create", command=self.create_person).pack(fill=tk.X, padx=5, pady=2)
        tk.Button(crud_frame, text="Read", command=self.read_person).pack(fill=tk.X, padx=5, pady=2)
        tk.Button(crud_frame, text="Update", command=self.update_person).pack(fill=tk.X, padx=5, pady=2)
        tk.Button(crud_frame, text="Delete", command=self.delete_person).pack(fill=tk.X, padx=5, pady=2)
        tk.Button(crud_frame, text="Refresh", command=self.refresh_table).pack(fill=tk.X, padx=5, pady=2)

        # Person Details Panel
        details_frame = tk.Frame(top_frame)
        details_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(details_frame, text="ID:").grid(row=0, column=0, sticky=tk.E)
        self.id_entry = tk.Entry(details_frame, state="disabled")
        self.id_entry.grid(row=0, column=1)

        tk.Label(details_frame, text="Name:").grid(row=1, column=0, sticky=tk.E)
        self.name_entry = tk.Entry(details_frame)
        self.name_entry.grid(row=1, column=1)

        tk.Label(details_frame, text="Address:").grid(row=2, column=0, sticky=tk.E)
        self.address_entry = tk.Entry(details_frame)
        self.address_entry.grid(row=2, column=1)

        tk.Label(details_frame, text="Timestamp:").grid(row=3, column=0, sticky=tk.E)
        self.timestamp_entry = tk.Entry(details_frame, state="disabled")
        self.timestamp_entry.grid(row=3, column=1)

        # Table
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.table = ttk.Treeview(table_frame, columns=("ID", "Name", "Address", "Timestamp"), show="headings")
        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Address", text="Address")
        self.table.heading("Timestamp", text="Timestamp")
        self.table.pack(fill=tk.BOTH, expand=True)

        self.refresh_table()

        self.table.bind("<<TreeviewSelect>>", self.on_table_select)

    def create_person(self):
        # Implementation for creating a new person
        pass

    def read_person(self):
        # Implementation for reading a selected person's details
        pass

    def update_person(self):
        # Implementation for updating a selected person's details
        pass

    def delete_person(self):
        # Implementation for deleting a selected person
        pass

    def refresh_table(self):
        # Clear existing items in the table
        self.table.delete(*self.table.get_children())

        # Populate the table with person data
        for person in self.person_list:
            self.table.insert("", "end", values=(person.id, person.name, person.addressLine1, person.timestamp))

    def on_table_select(self, event):
        # Get the selected item from the table
        selected_item = self.table.focus()

        # Get the data associated with the selected item
        if selected_item:
            item_data = self.table.item(selected_item)
            self.selected_person = item_data["values"]

            # Populate the details panel with the selected person's data
            self.id_entry.config(state="normal")
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, self.selected_person[0])
            self.id_entry.config(state="disabled")

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.selected_person[1])

            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, self.selected_person[2])

            self.timestamp_entry.config(state="normal")
            self.timestamp_entry.delete(0, tk.END)
            self.timestamp_entry.insert(0, self.selected_person[3])
            self.timestamp_entry.config(state="disabled")


# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = PersonDialog(root)
    root.mainloop()
