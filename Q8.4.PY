import tkinter as tk
import sqlite3

conn = sqlite3.connect("tasks.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")

def load_tasks():
    listbox.delete(0, tk.END)
    cur.execute("SELECT * FROM tasks")
    for row in cur.fetchall():
        listbox.insert(tk.END, row)

def add_task():
    cur.execute("INSERT INTO tasks (task) VALUES (?)", ("New Task",))
    conn.commit()
    load_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        cur.execute("DELETE FROM tasks WHERE id=?", (item[0],))
        conn.commit()
        load_tasks()

def edit_task():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        cur.execute("UPDATE tasks SET task=? WHERE id=?", ("Updated Task", item[0]))
        conn.commit()
        load_tasks()

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x300")
root.resizable(False, False)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=2)
tk.Button(root, text="Edit Task", command=edit_task).pack(pady=2)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=2)

load_tasks()

root.mainloop()