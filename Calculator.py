import tkinter as tk
import math             #library import 
import re

 # Function to preprocess mathematical expressions
def preprocess_expression(expression):
#     expression = expression.replace("^", "**")  # Convert exponentiation
#     expression = preprocess_expression(input_var.get()) 
#     expression = expression.replace("π", str(math.pi))  # Replace π with it is value
#     expression = re.sub(r'(\d+)%', r'(\1*0.01)', expression)  # Convert percentage (e.g., 50% → 0.5)

#     expression = re.sub(r'√(\d+)', r'math.sqrt(\1)', expression)  # Convert √x to math.sqrt(x)
     return expression

# Function to handle button clicks
def on_click(button_text):
    if button_text == 'AC':
        input_var.set(" ")  # Clear input
    elif button_text == "-->":
        text = input_var.get()
        input_var.set(text[:-1])  # Remove last character
    elif button_text == '=':
        try:
            expression = preprocess_expression(input_var.get())  # Convert expression
            result = eval(expression, {"math": math, "__builtins__": {}})  # Evaluate safely
            input_var.set(result)
        except Exception:
            input_var.set("Error")  # Show error if calculation fails
    else:
        input_var.set(input_var.get() + button_text)  # Append text to input
    
# Initialize main window
root = tk.Tk()
root.geometry("340x540")
root.title("Calculator")
root.resizable(False, False)

# Input field
input_var = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=input_var,state="readonly",
    font=("Arial", 30),
    justify="right",
    width=20,
    bd=6,
    relief="ridge"
)
entry.pack(pady=10, padx=10)

# Button layout
buttons = [
    ("AC", "(", ")", "-->"),
    ("√", "^", "%", "π"),
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    (".", "0", "=", "+")
]

# Function to assign button colors
def get_color(button_text):
    if button_text in {"AC"}:
        return "red"
    elif button_text in {"Delete", "(", ")"}:
        return "yellowgreen"
    elif button_text in {"+", "-", "*", "/", "^", "%", "π", "√"}:
        return "lightgreen"
    else:
        return "teal"

# Create buttons
frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(fill="both", expand=True)
    for button_text in row:
        btn = tk.Button(
            row_frame,
            text=button_text,
            font=("Arial", 16),
            command=lambda text=button_text: on_click(text),
            width=4,height=2,
            bg=get_color(button_text),
            fg="black"
        )
        btn.pack(side="left",
                  fill="both",
                    expand=True,
                      padx=4,
                        pady=4)

root.mainloop()
