import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import simpledialog


class MySQLApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MySQL Data Viewer")
        self.geometry("600x400")

        self.create_widgets()

        # Connect to MySQL
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="payroll"
        )

        # Create cursor
        self.cursor = self.db_connection.cursor()

        # Load data from MySQL table
        self.load_data()

    def create_widgets(self):
        self.table = ttk.Treeview(self, columns=("ID", "Name", "Status", "Password"))
        self.table.heading("#0", text="ID")
        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="FirstName")
        self.table.heading("Status", text="LastName")
        self.table.heading("Password", text="Payroll Id")
        self.table.pack(fill="both", expand=True)

        self.create_button = tk.Button(self, text="Create", command=self.create_row)
        self.create_button.pack(side="left", padx=10)

        self.update_button = tk.Button(self, text="Update", command=self.update_row)
        self.update_button.pack(side="left", padx=10)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_row)
        self.delete_button.pack(side="left", padx=10)

    def load_data(self):
        # Clear existing data
        self.table.delete(*self.table.get_children())

        # Fetch data from MySQL table
        self.cursor.execute("SELECT id,firstname, lastname, payroll_id  FROM User")
        rows = self.cursor.fetchall()

        # Insert data into the table
        for row in rows:
            self.table.insert("", "end", text=row[0], values=row)

    def create_row(self):
        # Create a popup dialog for creating a new row
        name = simpledialog.askstring("Create Row", "Enter Name:")
        status = simpledialog.askstring("Create Row", "Enter Status:")
        password = simpledialog.askstring("Create Row", "Enter Password:")

        # Insert new row into MySQL table
        self.cursor.execute("INSERT INTO User (name, status, password) VALUES (%s, %s, %s)",
                            (name, status, password))
        self.db_connection.commit()

        # Reload data
        self.load_data()

    def update_row(self):
        # Get the ID of the selected row
        selected_item = self.table.selection()[0]
        id = self.table.item(selected_item, "text")

        # Get the new values for the row
        name = simpledialog.askstring("Update Row", "Enter New Name:")
        status = simpledialog.askstring("Update Row", "Enter New Status:")
        password = simpledialog.askstring("Update Row", "Enter New Password:")

        # Update row in MySQL table
        self.cursor.execute("UPDATE your_table SET name=%s, status=%s, password=%s WHERE id=%s",
                            (name, status, password, id))
        self.db_connection.commit()

        # Reload data
        self.load_data()

    def delete_row(self):
        # Get the ID of the selected row
        selected_item = self.table.selection()[0]
        id = self.table.item(selected_item, "text")

        # Delete row from MySQL table
        self.cursor.execute("DELETE FROM your_table WHERE id=%s", (id,))
        self.db_connection.commit()

        # Reload data
        self.load_data()


if __name__ == "__main__":
    app = MySQLApp()
    app.mainloop()
