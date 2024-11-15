import tkinter as tk
from tkinter import simpledialog
import pyperclip


class ButtonManager(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # 버튼 목록을 저장할 프레임
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=20)

        # 버튼 추가 버튼
        self.add_button = tk.Button(self, text="Add Button", command=self.add_new_button)
        self.add_button.pack(pady=10)

        # 동적으로 생성된 버튼의 카운트
        self.button_count = 0
        self.buttons = []  # 버튼 객체를 저장할 리스트

    def add_new_button(self):
        """새로운 버튼 추가"""
        self.button_count += 1
        button_text = f"Button {self.button_count}"  # 고유한 버튼 텍스트
        new_button = tk.Button(
            self.button_frame,
            text=button_text,
            command=lambda text=button_text: self.copy_to_clipboard(text)
        )

        # 우클릭 메뉴 추가
        new_button.bind("<Button-3>", lambda event, btn=new_button: self.show_context_menu(event, btn))

        new_button.pack(pady=5)
        self.buttons.append(new_button)

    def copy_to_clipboard(self, text):
        """버튼 텍스트를 클립보드에 복사"""
        pyperclip.copy(text)
        print(f"Copied to clipboard: {text}")  # 콘솔 출력 확인용

    def show_context_menu(self, event, button):
        """우클릭 메뉴를 표시"""
        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="Edit Button Text", command=lambda: self.edit_button_text(button))
        context_menu.add_command(label="Copy to Clipboard", command=lambda: self.copy_to_clipboard(button.cget("text")))
        context_menu.post(event.x_root, event.y_root)

    def edit_button_text(self, button):
        """버튼 텍스트 수정"""
        new_text = simpledialog.askstring("Edit Text", "Enter new text for the button:", initialvalue=button.cget("text"))
        if new_text:
            button.config(text=new_text)  # 버튼 텍스트 수정
