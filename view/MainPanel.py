import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Sample Tkinter App")
        self.master.geometry("600x400")
        self.pack(fill=tk.BOTH, expand=True)

        # Create menu bar
        self.create_menu()

        # Create icon list at the top
        self.create_icon_list()

        # Create table below the icon list
        self.create_table()

        # Add ADD and CLOSE buttons at the bottom
        self.create_buttons()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.dummy_action)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_icon_list(self):
        icon_frame = tk.Frame(self)
        icon_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Icons: Add your actual icons instead of empty labels
        icon1 = tk.Label(icon_frame, text="Icon1", bg="lightblue", width=15)
        icon1.pack(side=tk.LEFT, padx=5)
        icon2 = tk.Label(icon_frame, text="Icon2", bg="lightgreen", width=15)
        icon2.pack(side=tk.LEFT, padx=5)
        icon3 = tk.Label(icon_frame, text="Icon3", bg="lightpink", width=15)
        icon3.pack(side=tk.LEFT, padx=5)

    def create_table(self):
        table_frame = tk.Frame(self)
        table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

        # Create the treeview (table)
        columns = ("ID", "Date", "Description")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        # Define headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Description", text="Description")

        # Define column widths
        self.tree.column("ID", width=100, anchor=tk.CENTER)
        self.tree.column("Date", width=150, anchor=tk.CENTER)
        self.tree.column("Description", width=300)

        # Add sample data
        data = [
            (1, "2024-01-01", "Item 1 description"),
            (2, "2024-02-01", "Item 2 description"),
            (3, "2024-03-01", "Item 3 description")
        ]
        for item in data:
            self.tree.insert('', tk.END, values=item)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def create_buttons(self):
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.BOTTOM, pady=10)

        # ADD button
        add_button = tk.Button(button_frame, text="ADD", command=self.add_item)
        add_button.pack(side=tk.LEFT, padx=10)

        # CLOSE button
        close_button = tk.Button(button_frame, text="CLOSE", command=self.master.quit)
        close_button.pack(side=tk.LEFT, padx=10)

    def dummy_action(self):
        # Placeholder for menu actions
        messagebox.showinfo("Action", "Dummy action triggered!")

    def show_about(self):
        messagebox.showinfo("About", "Sample Tkinter App v1.0")

    def add_item(self):
        # Placeholder for the ADD button functionality
        messagebox.showinfo("Add", "Add item functionality to be implemented.")


# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MainFrame(master=root)
    app.mainloop()
