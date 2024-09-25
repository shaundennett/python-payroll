import tkinter as tk
from tkinter import simpledialog, messagebox
import datetime

class EntryDialog(simpledialog.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Data Entry")

    def body(self, frame):
        # Define the form fields
        self.contact_name_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.time_var = tk.StringVar()
        self.hours_var = tk.IntVar()
        self.state_var = tk.StringVar()
        self.timestamp_var = tk.StringVar(value=str(datetime.datetime.now()))

        # Create the form widgets
        tk.Label(frame, text="Contact Name").grid(row=0, column=0, sticky=tk.W)
        self.contact_name_entry = tk.Entry(frame, textvariable=self.contact_name_var)
        self.contact_name_entry.grid(row=0, column=1)

        tk.Label(frame, text="Date (YYYY-MM-DD)").grid(row=1, column=0, sticky=tk.W)
        self.date_entry = tk.Entry(frame, textvariable=self.date_var)
        self.date_entry.grid(row=1, column=1)

        tk.Label(frame, text="Time (HH:MM)").grid(row=2, column=0, sticky=tk.W)
        self.time_entry = tk.Entry(frame, textvariable=self.time_var)
        self.time_entry.grid(row=2, column=1)

        tk.Label(frame, text="Hours").grid(row=3, column=0, sticky=tk.W)
        self.hours_entry = tk.Entry(frame, textvariable=self.hours_var)
        self.hours_entry.grid(row=3, column=1)

        tk.Label(frame, text="State").grid(row=4, column=0, sticky=tk.W)
        self.state_entry = tk.Entry(frame, textvariable=self.state_var)
        self.state_entry.grid(row=4, column=1)

        tk.Label(frame, text="Timestamp").grid(row=5, column=0, sticky=tk.W)
        self.timestamp_label = tk.Label(frame, textvariable=self.timestamp_var)
        self.timestamp_label.grid(row=5, column=1)

        return self.contact_name_entry  # Focus on first entry

    def validate(self):
        try:
            datetime.datetime.strptime(self.date_var.get(), "%Y-%m-%d")  # Validate date format
            datetime.datetime.strptime(self.time_var.get(), "%H:%M")     # Validate time format
            return True
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid date or time format.")
            return False

    def apply(self):
        # Collect the data to be returned
        self.result = {
            "contactName": self.contact_name_var.get(),
            "date": self.date_var.get(),
            "time": self.time_var.get(),
            "hours": self.hours_var.get(),
            "state": self.state_var.get(),
            "timestamp": self.timestamp_var.get()
        }

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Button to open the data entry dialog
        self.open_dialog_button = tk.Button(self, text="Open Entry Dialog", command=self.open_entry_dialog)
        self.open_dialog_button.pack(pady=20)

        # Label to display submitted data
        self.result_label = tk.Label(self, text="No data submitted")
        self.result_label.pack(pady=20)

    def open_entry_dialog(self):
        # Open the modal dialog
        dialog = EntryDialog(self)
        if dialog.result:
            # If data is submitted, show it in the result label
            result_str = (f"Name: {dialog.result['contactName']}, Date: {dialog.result['date']}, "
                          f"Time: {dialog.result['time']}, Hours: {dialog.result['hours']}, "
                          f"State: {dialog.result['state']}, Timestamp: {dialog.result['timestamp']}")
            self.result_label.config(text=result_str)
        else:
            # If canceled, show a message
            self.result_label.config(text="No data submitted")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = MainFrame(master=root)
    app.mainloop()
