import tkinter as tk
from tkinter import ttk

class MainDialog:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Dialog")

        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Create "Create" button
        self.create_button = ttk.Button(self.main_frame, text="Create", command=self.create_popup)
        self.create_button.pack()

    def create_popup(self):
        # Create popup window
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Popup")

        # Create popup frame
        self.popup_frame = ttk.Frame(self.popup)
        self.popup_frame.pack(padx=20, pady=20)

        # Name field
        self.name_label = ttk.Label(self.popup_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.popup_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Age field
        self.age_label = ttk.Label(self.popup_frame, text="Age:")
        self.age_label.grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = ttk.Entry(self.popup_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        # Status field
        self.status_label = ttk.Label(self.popup_frame, text="Status:")
        self.status_label.grid(row=2, column=0, padx=5, pady=5)
        self.status_entry = ttk.Entry(self.popup_frame)
        self.status_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create "Create Event" button
        self.create_event_button = ttk.Button(self.popup_frame, text="Create Event", command=self.create_event)
        self.create_event_button.grid(row=3, columnspan=2, padx=5, pady=5)

    def create_event(self):
        # Get values from entries
        name = self.name_entry.get()
        age = self.age_entry.get()
        status = self.status_entry.get()

        # Print values (You can perform other actions here, such as saving to a database)
        print("Name:", name)
        print("Age:", age)
        print("Status:", status)

        # Close the popup window
        self.popup.destroy()

def main():
    root = tk.Tk()
    app = MainDialog(root)
    root.mainloop()

if __name__ == "__main__":
    main()
