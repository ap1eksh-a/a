import tkinter as tk
from tkinter import messagebox

def signup():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    agree = agree_var.get()

   
    if not name or not email or not password or not confirm_password:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
    elif not agree:
        messagebox.showwarning("Agreement Required", "You must agree to the terms and conditions.")
    else:
        messagebox.showinfo("Sign-Up Successful", f"Welcome, {name}!")


window = tk.Tk()
window.title("Sign-Up Window")
window.geometry("400x400")


tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_email = tk.Entry(window)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Password:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_password = tk.Entry(window, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=10)

tk.Label(window, text="Confirm Password:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
entry_confirm_password = tk.Entry(window, show="*")
entry_confirm_password.grid(row=3, column=1, padx=10, pady=10)


agree_var = tk.BooleanVar()
check_agree = tk.Checkbutton(window, text="I agree to the terms and conditions", variable=agree_var)
check_agree.grid(row=4, columnspan=2, padx=10, pady=10)


signup_button = tk.Button(window, text="Sign Up", command=signup)
signup_button.grid(row=5, columnspan=2, padx=10, pady=20)


window.mainloop()
