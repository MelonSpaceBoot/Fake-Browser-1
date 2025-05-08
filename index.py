import tkinter as tk
from tkinter import messagebox

# Simulated browser state
tabs = {}          # Each tab stores its own history
current_tab = "Tab 1"

def normalize_url(raw_url):
    url = raw_url.lower().strip()
    url = url.replace("https://", "").replace("http://", "").strip("/")
    return url

def switch_tab(tab_name):
    global current_tab
    current_tab = tab_name
    if not tabs[tab_name]:  # First visit = go home
        load_url_in_tab("www.google.com")
    else:
        load_page(tabs[tab_name][-1])

def fake_go():
    raw_url = url_entry.get()
    url = normalize_url(raw_url)
    load_url_in_tab(url)

def load_url_in_tab(url):
    if current_tab not in tabs:
        tabs[current_tab] = []
    if not tabs[current_tab] or tabs[current_tab][-1] != url:
        tabs[current_tab].append(url)
    url_entry.delete(0, tk.END)
    url_entry.insert(0, url)
    load_page(url)

def go_back():
    if len(tabs[current_tab]) > 1:
        tabs[current_tab].pop()
        previous_url = tabs[current_tab][-1]
        url_entry.delete(0, tk.END)
        url_entry.insert(0, previous_url)
        load_page(previous_url)
    else:
        messagebox.showinfo("Back", "No previous page.")

def go_home():
    load_url_in_tab("www.google.com")

def load_page(url):
    for widget in content_frame.winfo_children():
        widget.destroy()

    if url == "www.google.com":
        show_google()
    elif url == "www.facebook.com":
        show_facebook()
    elif url == "www.youtube.com":
        show_youtube()
    else:
        tk.Label(content_frame, text=f"404 Page Not Found for '{url}'", font=("Arial", 14)).pack()

# Fake page functions
def show_google():
    tk.Label(content_frame, text="Welcome to Fake Google", font=("Arial", 16)).pack()
    tk.Entry(content_frame, width=30).pack(pady=5)
    tk.Button(content_frame, text="Search", command=lambda: messagebox.showinfo("Fake Search", "No real results!")).pack()

def show_facebook():
    tk.Label(content_frame, text="Fake Facebook Feed", font=("Arial", 16)).pack()
    tk.Label(content_frame, text="Post: 'Hello world!'", font=("Arial", 12)).pack(pady=5)
    tk.Button(content_frame, text="Like", command=lambda: messagebox.showinfo("Fake Like", "You liked the post!")).pack()

def show_youtube():
    tk.Label(content_frame, text="Fake YouTube", font=("Arial", 16)).pack()
    tk.Label(content_frame, text="Video: How to make a fake browser", font=("Arial", 12)).pack(pady=5)
    tk.Button(content_frame, text="Play", command=lambda: messagebox.showinfo("Fake Video", "Pretend the video is playing...")).pack()

# Main window setup
root = tk.Tk()
root.title("Fake Browser with Tabs")
root.geometry("700x450")

url_frame = tk.Frame(root)
url_frame.pack(pady=5)

url_entry = tk.Entry(url_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=5)
url_entry.focus_set()

go_button = tk.Button(url_frame, text="Go", command=fake_go)
go_button.pack(side=tk.LEFT)

back_button = tk.Button(url_frame, text="Back", command=go_back)
back_button.pack(side=tk.LEFT, padx=3)

home_button = tk.Button(url_frame, text="Home", command=go_home)
home_button.pack(side=tk.LEFT)

tab_frame = tk.Frame(root)
tab_frame.pack(pady=5)

# Create two tabs
for i in range(1, 3):
    tab_name = f"Tab {i}"
    tabs[tab_name] = []
    tk.Button(tab_frame, text=tab_name, command=lambda t=tab_name: switch_tab(t)).pack(side=tk.LEFT, padx=5)

content_frame = tk.Frame(root)
content_frame.pack(pady=20)

# Load default page
switch_tab("Tab 1")

root.mainloop()
