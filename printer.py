import tkinter as tk
from tkinter import messagebox

def generate_invoice():
    # Get invoice details from user input
    customer_name = entry_customer_name.get()
    item = entry_item.get()
    quantity = int(entry_quantity.get())
    price = float(entry_price.get())

    # Generate invoice string
    invoice = f"Customer Name: {customer_name}\n" \
              f"Item: {item}\n" \
              f"Quantity: {quantity}\n" \
              f"Price: ${price}\n" \
              f"Total: ${quantity * price}"

    # Print invoice
    print(invoice)

    # Show success message
    messagebox.showinfo("Invoice Generated", "Invoice printed successfully!")

# Create Tkinter window
window = tk.Tk()
window.title("Invoice Generator")

# Create labels and entry fields
tk.Label(window, text="Customer Name:").grid(row=0, column=0)
entry_customer_name = tk.Entry(window)
entry_customer_name.grid(row=0, column=1)

tk.Label(window, text="Item:").grid(row=1, column=0)
entry_item = tk.Entry(window)
entry_item.grid(row=1, column=1)

tk.Label(window, text="Quantity:").grid(row=2, column=0)
entry_quantity = tk.Entry(window)
entry_quantity.grid(row=2, column=1)

tk.Label(window, text="Price:").grid(row=3, column=0)
entry_price = tk.Entry(window)
entry_price.grid(row=3, column=1)

# Create button to generate invoice
btn_generate_invoice = tk.Button(window, text="Generate Invoice", command=generate_invoice)
btn_generate_invoice.grid(row=4, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()