# Creating a simple note taking app, this will be later integrated into my password manager project. 
# Switched to Arch Linux as my first GNU/Linux OS distro and this is my first time coding under linux :)
# Password Manager project will be on hold for a while until i make necessary changes to make it compatible.
import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes")
        self.root.config(background="#1e1e1e")
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        self.text_area = tk.Text(self.root, wrap="word", bg="#1e1e1e", fg="white", insertbackground="white")  # Set text and insert color to white
        self.text_area.pack(expand=True, fill="both")

        # Create a menu bar.
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Add the menu bar to the root window
        self.root.config(menu=self.menu_bar)

        self.file_path = None  # Initialize file_path attribute


    def new_file(self):
        self.text_area.delete("1.0", tk.END) 

    def open_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, content)
                self.file_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while opening the file:\n{e}")

    def save_file(self):
        try:
            if not self.file_path:
                self.save_as_file()
            else:
                content = self.text_area.get("1.0", tk.END)
                with open(self.file_path, "w") as file:
                    file.write(content)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file:\n{e}")

    def save_as_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                self.file_path = file_path
                self.save_file()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file:\n{e}")

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()