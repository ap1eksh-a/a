import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

  
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def cancel():
    window.destroy()


window = tk.Tk()
window.title("Login Window")
window.geometry("300x200")


tk.Label(window, text="Username:").pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)


tk.Label(window, text="Password:").pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)


frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

btn_login = tk.Button(frame_buttons, text="Login", command=login)
btn_login.grid(row=0, column=0, padx=5)

btn_cancel = tk.Button(frame_buttons, text="Cancel", command=cancel)
btn_cancel.grid(row=0, column=1, padx=5)


window.mainloop()
