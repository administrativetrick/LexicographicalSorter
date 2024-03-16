import tkinter as tk

class LexicographicalSorterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lexicographical Sorter")

        self.instructions_label = tk.Label(master, text="Type items and press Enter to add them to the list. Use Ctrl+C/Cmd+C to copy and Ctrl+V/Cmd+V to paste:")
        self.instructions_label.pack(fill=tk.X)

        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.item_listbox = tk.Listbox(self.frame, height=10, width=50, yscrollcommand=self.scrollbar.set)
        self.item_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.item_listbox.yview)

        self.item_entry = tk.Entry(master)
        self.item_entry.bind("<Return>", self.add_item_directly)
        self.item_entry.pack(fill=tk.X)

        self.sort_button = tk.Button(master, text="Sort Items", command=self.sort_items)
        self.sort_button.pack(fill=tk.X)

        self.clear_button = tk.Button(master, text="Clear Items", command=self.clear_items)
        self.clear_button.pack(fill=tk.X)

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack(fill=tk.X)

        # Bindings for copying and pasting with support for macOS
        self.item_listbox.bind("<Control-c>", self.copy_to_clipboard)
        self.item_listbox.bind("<Control-v>", self.paste_from_clipboard)
        self.item_listbox.bind("<Command-c>", self.copy_to_clipboard)  # For macOS
        self.item_listbox.bind("<Command-v>", self.paste_from_clipboard)  # For macOS

    def add_item_directly(self, event=None):
        item = self.item_entry.get().strip()
        if item:
            self.item_listbox.insert(tk.END, item)
            self.item_entry.delete(0, tk.END)

    def sort_items(self):
        items = list(self.item_listbox.get(0, tk.END))
        items.sort()
        self.item_listbox.delete(0, tk.END)
        for item in items:
            self.item_listbox.insert(tk.END, item)

    def clear_items(self):
        self.item_listbox.delete(0, tk.END)

    def copy_to_clipboard(self, event=None):
        if not self.item_listbox.curselection():
            return
        self.master.clipboard_clear()
        selected_text = self.item_listbox.get(self.item_listbox.curselection())
        self.master.clipboard_append(selected_text)

    def paste_from_clipboard(self, event=None):
        try:
            clipboard_text = self.master.clipboard_get()
        except tk.TclError:
            return
        for line in clipboard_text.split('\n'):
            if line.strip():
                self.item_listbox.insert(tk.END, line.strip())

if __name__ == '__main__':
    root = tk.Tk()
    gui = LexicographicalSorterGUI(root)
    root.geometry("600x500")
    root.mainloop()
