import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Welcome Screen")
root.geometry("500x300")


def continue_to_app():
    messagebox.showinfo("Welcome", "Welcome to the app! Loading the main application...")
    root.destroy()  


app_name_label = tk.Label(root, text="MyApp", font=("Arial", 24, "bold"), fg="blue")
app_name_label.pack(pady=20)


welcome_message = tk.Label(root, text="Welcome to MyApp, your one-stop solution for all your needs!",
                           font=("Arial", 14), wraplength=400, justify="center")
welcome_message.pack(pady=10)


instructions = tk.Label(root, text="Click 'Continue' to explore the features of MyApp.",
                        font=("Arial", 12), wraplength=400, justify="center")
instructions.pack(pady=20)


continue_button = tk.Button(root, text="Continue", font=("Arial", 12), command=continue_to_app)
continue_button.pack(pady=10)


root.mainloop()
