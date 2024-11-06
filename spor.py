import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Sports Academy Registration Form")
root.geometry("500x600")


def submit_registration():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    sport = sport_listbox.get(sport_listbox.curselection())
    skill_level = skill_level_var.get()
    experience = experience_text.get("1.0", tk.END).strip()
    
    if name and age and gender and sport and skill_level:
        try:
            age = int(age)
            messagebox.showinfo("Registration Successful", f"Thank you {name} for registering!")
        except ValueError:
            messagebox.showerror("Invalid Age", "Please enter a valid age.")
    else:
        messagebox.showwarning("Missing Information", "Please fill all required fields.")


tk.Label(root, text="Sports Academy Registration Form", font=("Arial", 18, "bold")).pack(pady=10)


tk.Label(root, text="Name:").pack(anchor="w", padx=20)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=20, pady=5)


tk.Label(root, text="Age:").pack(anchor="w", padx=20)
age_entry = tk.Entry(root, width=40)
age_entry.pack(padx=20, pady=5)


tk.Label(root, text="Gender:").pack(anchor="w", padx=20)
gender_var = tk.StringVar(value="Male")
gender_frame = tk.Frame(root)
gender_frame.pack(anchor="w", padx=20)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(side="left")


tk.Label(root, text="Select Sport:").pack(anchor="w", padx=20)
sport_listbox = tk.Listbox(root, height=5, selectmode="single")
for sport in ["Basketball", "Football", "Tennis", "Swimming", "Cricket"]:
    sport_listbox.insert(tk.END, sport)
sport_listbox.pack(padx=20, pady=5)
sport_listbox.select_set(0)


tk.Label(root, text="Skill Level:").pack(anchor="w", padx=20)
skill_level_var = tk.StringVar(value="Beginner")
skill_level_frame = tk.Frame(root)
skill_level_frame.pack(anchor="w", padx=20)
tk.Radiobutton(skill_level_frame, text="Beginner", variable=skill_level_var, value="Beginner").pack(side="left")
tk.Radiobutton(skill_level_frame, text="Intermediate", variable=skill_level_var, value="Intermediate").pack(side="left")
tk.Radiobutton(skill_level_frame, text="Advanced", variable=skill_level_var, value="Advanced").pack(side="left")


tk.Label(root, text="Previous Experience (if any):").pack(anchor="w", padx=20)
experience_text = tk.Text(root, height=5, width=40)
experience_text.pack(padx=20, pady=5)


submit_button = tk.Button(root, text="Submit Registration", command=submit_registration)
submit_button.pack(pady=20)


root.mainloop()
