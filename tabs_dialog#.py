import tkinter as tk
from tkinter import ttk

class InternalPanelDialog:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Internal Panel with Tabs")

        # Create internal panel
        self.internal_panel = ttk.Frame(self.parent)
        self.internal_panel.pack(fill=tk.BOTH, expand=True)

        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.internal_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Tab 1")
        self.notebook.add(self.tab2, text="Tab 2")
        self.notebook.add(self.tab3, text="Tab 3")

        # Add content to tabs (you can add widgets as needed)
        label1 = ttk.Label(self.tab1, text="Content for Tab 1")
        label1.pack(padx=20, pady=20)

        label2 = ttk.Label(self.tab2, text="Content for Tab 2")
        label2.pack(padx=20, pady=20)

        label3 = ttk.Label(self.tab3, text="Content for Tab 3")
        label3.pack(padx=20, pady=20)

def main():
    root = tk.Tk()
    app = InternalPanelDialog(root)
    root.mainloop()

if __name__ == "__main__":
    main()
