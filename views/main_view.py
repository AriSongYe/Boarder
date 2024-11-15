import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Main Page", font=("Arial", 16))
        label.pack(pady=20)