import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == "+":
            result.set(num1 + num2)
        elif op == "-":
            result.set(num1 - num2)
        elif op == "*":
            result.set(num1 * num2)
        elif op == "/":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error")
        else:
            result.set("Invalid")
    except:
        result.set("Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")
root.resizable(False, False)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

operator = tk.Entry(root)
operator.pack(pady=5)

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=10)

result = tk.StringVar()
label = tk.Label(root, textvariable=result)
label.pack(pady=10)

root.mainloop()