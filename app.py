import tkinter as tk
from tkinter import ttk
from views.main_view import MainView
from views.button_manager_view import ButtonManager

class BoarderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabbed Clipboard App")
        self.root.geometry("400x300")

        # Notebook 생성 (탭)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Main Page 탭 추가
        self.main_page = MainView(self.notebook)
        self.notebook.add(self.main_page, text="Main Page")

        # Button Manager 탭 추가
        self.button_manager = ButtonManager(self.notebook)
        self.notebook.add(self.button_manager, text="Button Manager")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = BoarderApp(root)
    app.run()
