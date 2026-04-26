import tkinter as tk
import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age TEXT,
    course TEXT,
    email TEXT
)
""")

def submit():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()
    email = entry_email.get()

    cur.execute("INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
                (name, age, course, email))
    conn.commit()

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    status.set("Student Registered Successfully")

root = tk.Tk()
root.title("Student Registration")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Course").pack()
entry_course = tk.Entry(root)
entry_course.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Register", command=submit).pack(pady=10)

status = tk.StringVar()
tk.Label(root, textvariable=status).pack()

root.mainloop()