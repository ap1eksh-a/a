import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Customer Feedback Form")
root.geometry("400x500")


def submit_feedback():
    feedback = {
        "name": name_entry.get(),
        "email": email_entry.get(),
        "rating": rating_var.get(),
        "comments": comments_text.get("1.0", tk.END),
        "suggestions": suggestion_var.get(),
        "service_quality": service_quality_var.get(),
        "food_quality": food_quality_var.get(),
    }
    
    messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
    root.quit()


tk.Label(root, text="Customer Feedback Form", font=("Arial", 16)).pack(pady=10)


tk.Label(root, text="Name:").pack(anchor="w", padx=20)
name_entry = tk.Entry(root, width=30)
name_entry.pack(padx=20, pady=5)


tk.Label(root, text="Email:").pack(anchor="w", padx=20)
email_entry = tk.Entry(root, width=30)
email_entry.pack(padx=20, pady=5)


tk.Label(root, text="Rate your experience (1-5):").pack(anchor="w", padx=20)
rating_var = tk.StringVar(value="3")
rating_options = ["1", "2", "3", "4", "5"]
rating_menu = tk.OptionMenu(root, rating_var, *rating_options)
rating_menu.pack(padx=20, pady=5)


suggestion_var = tk.BooleanVar()
tk.Checkbutton(root, text="I have suggestions to improve", variable=suggestion_var).pack(anchor="w", padx=20)


tk.Label(root, text="Quality Feedback:", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(10, 0))
service_quality_var = tk.BooleanVar()
tk.Checkbutton(root, text="Good Service Quality", variable=service_quality_var).pack(anchor="w", padx=40)
food_quality_var = tk.BooleanVar()
tk.Checkbutton(root, text="Good Food Quality", variable=food_quality_var).pack(anchor="w", padx=40)


tk.Label(root, text="Additional Comments:").pack(anchor="w", padx=20)
comments_text = tk.Text(root, height=5, width=30)
comments_text.pack(padx=20, pady=5)


submit_button = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_button.pack(pady=20)


root.mainloop()
