import tkinter as tk

def show():
    label.config(text=entry.get())

root = tk.Tk()
root.title("Input Window")
root.geometry("400x300")
root.resizable(False, False)

entry = tk.Entry(root)
entry.pack(pady=20)

btn = tk.Button(root, text="Submit", command=show)
btn.pack()

label = tk.Label(root, text="")
label.pack(pady=20)

root.mainloop()