import tkinter as tk
import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

def signup():
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                (entry_user.get(), entry_pass.get()))
    conn.commit()
    status.set("Signup Successful")

def login():
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                (entry_user.get(), entry_pass.get()))
    user = cur.fetchone()
    if user:
        status.set("Login Successful")
    else:
        status.set("Invalid Credentials")

root = tk.Tk()
root.title("Login System")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Signup", command=signup).pack(pady=5)
tk.Button(root, text="Login", command=login).pack(pady=5)

status = tk.StringVar()
tk.Label(root, textvariable=status).pack(pady=10)

root.mainloop()