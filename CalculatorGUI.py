import tkinter as tk
from GeminiCaller import *

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_click():
    current = ""
    entry.delete(0, tk.END)
    entry.insert(0, current)

def evaluate_expression():
    user_expression = entry.get()
    # Call the API function here to get the result
    result = call_gemini_api(user_expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

root = tk.Tk()
root.title("Gemini Calculator")

entry = tk.Entry(root, width=30, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buttons numbers
btn_1 = tk.Button(root, text="1", padx=20, pady=10, command=lambda: button_click("1"))
btn_1.grid(row=2, column=0)

btn_2 = tk.Button(root, text="2", padx=20, pady=10, command=lambda: button_click("2"))
btn_2.grid(row=2, column=1)

btn_3 = tk.Button(root, text="3", padx=20, pady=10, command=lambda: button_click("3"))
btn_3.grid(row=2, column=2)

btn_4 = tk.Button(root, text="4", padx=20, pady=10, command=lambda: button_click("4"))
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(root, text="5", padx=20, pady=10, command=lambda: button_click("5"))
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(root, text="6", padx=20, pady=10, command=lambda: button_click("6"))
btn_6.grid(row=3, column=2)

btn_7 = tk.Button(root, text="7", padx=20, pady=10, command=lambda: button_click("7"))
btn_7.grid(row=4, column=0)

btn_8 = tk.Button(root, text="8", padx=20, pady=10, command=lambda: button_click("8"))
btn_8.grid(row=4, column=1)

btn_9 = tk.Button(root, text="9", padx=20, pady=10, command=lambda: button_click("9"))
btn_9.grid(row=4, column=2)

btn_0 = tk.Button(root, text="0", padx=20, pady=10, command=lambda: button_click("0"))
btn_0.grid(row=5, column=1)

# buttons symbols
btn_clear = tk.Button(root, text="C", padx=20, pady=10, command=lambda: clear_click())
btn_clear.grid(row=1, column=2)

btn_openPara = tk.Button(root, text="(", padx=20, pady=10, command=lambda: button_click("("))
btn_openPara.grid(row=1, column=0)

btn_closePara = tk.Button(root, text=")", padx=20, pady=10, command=lambda: button_click(")"))
btn_closePara.grid(row=1, column=1)

btn_point = tk.Button(root, text=".", padx=20, pady=10, command=lambda: button_click("."))
btn_point.grid(row=5, column=2)

# buttons operator
btn_add = tk.Button(root, text="+", padx=20, pady=10, command=lambda: button_click("+"))
btn_add.grid(row=4, column=3)

btn_sub = tk.Button(root, text="-", padx=20, pady=10, command=lambda: button_click("-"))
btn_sub.grid(row=3, column=3)

btn_multi = tk.Button(root, text="*", padx=20, pady=10, command=lambda: button_click("*"))
btn_multi.grid(row=2, column=3)

btn_divide = tk.Button(root, text="/", padx=20, pady=10, command=lambda: button_click("/"))
btn_divide.grid(row=1, column=3)

btn_equals = tk.Button(root, text="=", padx=20, pady=10, command=evaluate_expression)
btn_equals.grid(row=5, column=3)

root.mainloop()
