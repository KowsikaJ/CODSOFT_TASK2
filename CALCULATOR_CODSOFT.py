import tkinter as tk
from tkinter import messagebox

# Functions for various operations
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Error: Division by zero"

# Function to perform the calculation
def calculate():
    try:
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        operation=operation_var.get()

        if operation =='+':
            result=add(num1, num2)
            result_label.config(text=f"Addition of {num1} and {num2} = {result}")
        elif operation =='-':
            result =subtract(num1, num2)
            result_label.config(text=f"Subtraction of {num1} and {num2} = {result}")
        elif operation =='*':
            result=multiply(num1, num2)
            result_label.config(text=f"Multiplication of {num1} and {num2} = {result}")
        elif operation =='/':
            result =divide(num1, num2)
            if result =="Error: Division by zero":
                result_label.config(text=result)
            else:
                result_label.config(text=f"Division of {num1} by {num2} = {result}")
        else:
            messagebox.showerror("Invalid Operation","Please select a valid operation.")

    except ValueError:
        messagebox.showerror("Invalid Input","Please enter numeric values.")
    except Exception as e:
        messagebox.showerror("Error",str(e))

root=tk.Tk()
root.title("Simple Calculator")

operation_var=tk.StringVar(value='+')

font_large=('Arial', 14)
font_medium=('Arial', 12)

tk.Label(root,text="Enter the first number:",font=font_large).grid(row=0, column=0, padx=10, pady=10)
entry_num1=tk.Entry(root, font=font_large, width=15)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the second number:", font=font_large).grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root, font=font_large, width=15)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Operation selection buttons
operations_frame = tk.Frame(root)
operations_frame.grid(row=2, columnspan=2, pady=10)

tk.Radiobutton(operations_frame,text="+",variable=operation_var,value='+', 
               font=font_large,indicatoron=0,width=5,padx=20,pady=10).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(operations_frame,text="-", variable=operation_var, value='-', 
               font=font_large,indicatoron=0,width=5,padx=20,pady=10).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(operations_frame,text="*",variable=operation_var,value='*', 
               font=font_large,indicatoron=0, width=5, padx=20, pady=10).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(operations_frame,text="/",variable=operation_var,value='/', 
               font=font_large,indicatoron=0,width=5,padx=20,pady=10).pack(side=tk.LEFT,padx=5)

# Calculate button
tk.Button(root,text="Calculate",command=calculate,font=font_large, width=10).grid(row=3,columnspan=2,pady=20)

# Result label
result_label = tk.Label(root,text="",font=font_large)
result_label.grid(row=4,columnspan=2,pady=10)
root.minsize(400, 300)

root.mainloop()





