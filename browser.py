import tkinter as tk
from tkinter import messagebox

def fake_go():
    url = url_entry.get()
    messagebox.showinfo("Fake Browser", f"Attempting to visit: {url}")

# Set up the window
root = tk.Tk()
root.title("Fake Browser")
root.geometry("400x100")

# URL bar
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

# Go button
go_button = tk.Button(root, text="Go", command=fake_go)
go_button.pack()

root.mainloop()
