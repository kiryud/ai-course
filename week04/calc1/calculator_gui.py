import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("파이썬 계산기")
        self.root.geometry("300x400")
        
        self.result_var = tk.StringVar(value="0")
        
        # 입력창 생성
        entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), 
                         borderwidth=5, relief="flat", justify='right')
        entry.pack(fill="both", padx=10, pady=20)

        # 버튼 프레임
        button_frame = tk.Frame(root)
        button_frame.pack()

        # 버튼 레이아웃 구성
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(button_frame, text=button, width=5, height=2, font=("Arial", 14),
                      command=action).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char == 'C':
            self.result_var.set("0")
        elif char == '=':
            try:
                # eval 함수를 사용하여 문자열 수식을 계산합니다.
                result = eval(current_text)
                self.result_var.set(str(result))
            except ZeroDivisionError:
                messagebox.showerror("에러", "0으로 나눌 수 없습니다.")
                self.result_var.set("0")
            except Exception:
                messagebox.showerror("에러", "잘못된 수식입니다.")
                self.result_var.set("0")
        else:
            if current_text == "0":
                self.result_var.set(char)
            else:
                self.result_var.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
