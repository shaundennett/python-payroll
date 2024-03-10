import tkinter as tk
from tkinter import ttk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Page")
        self.geometry("600x400")

        self.tab_control = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text='Tab 1')
        self.tab_control.add(self.tab2, text='Tab 2')
        self.tab_control.add(self.tab3, text='Tab 3')
        self.tab_control.add(self.tab4, text='Tab 4')

        self.tab_control.pack(expand=1, fill="both")

        self.create_tab1_widgets()

    def create_tab1_widgets(self):
        label = tk.Label(self.tab1, text="Orders Table")
        label.pack(pady=10)

        # Example table of orders
        orders_table = ttk.Treeview(self.tab1, columns=("Order ID", "Customer", "Product", "Quantity"))
        orders_table.heading("#0", text="Order ID")
        orders_table.heading("Order ID", text="Order ID")
        orders_table.heading("Customer", text="Customer")
        orders_table.heading("Product", text="Product")
        orders_table.heading("Quantity", text="Quantity")

        # Insert example data
        orders_table.insert("", "end", text="1", values=("1", "Customer A", "Product X", "5"))
        orders_table.insert("", "end", text="2", values=("2", "Customer B", "Product Y", "10"))

        orders_table.pack(pady=10)

        create_button = tk.Button(self.tab1, text="Create Order", command=self.create_order)
        create_button.pack(side="left", padx=10)

        update_button = tk.Button(self.tab1, text="Update Order", command=self.update_order)
        update_button.pack(side="left", padx=10)

        delete_button = tk.Button(self.tab1, text="Delete Order", command=self.delete_order)
        delete_button.pack(side="left", padx=10)

    def create_order(self):
        popup = tk.Toplevel(self.tab1)
        popup.title("Create Order")
        popup.geometry("300x200")

        label = tk.Label(popup, text="Enter Order Details:")
        label.pack(pady=10)

        # Add entry fields for order details (e.g., customer, product, quantity)
        # You can add entry fields and logic to save the new order data to your database

        submit_button = tk.Button(popup, text="Submit")
        submit_button.pack(pady=10)

    def update_order(self):
        # Logic to update an existing order
        pass

    def delete_order(self):
        # Logic to delete an existing order
        pass


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
