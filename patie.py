import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("400x500")


def submit_registration():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    department = department_listbox.get(department_listbox.curselection())
    symptoms = []
    if fever_var.get():
        symptoms.append("Fever")
    if cough_var.get():
        symptoms.append("Cough")
    if headache_var.get():
        symptoms.append("Headache")
    if fatigue_var.get():
        symptoms.append("Fatigue")
    
    comments = comments_text.get("1.0", tk.END).strip()
    
    if name and age and gender and department:
        try:
            age = int(age)
            messagebox.showinfo("Registration Submitted", f"Patient {name} registered successfully!")
        except ValueError:
            messagebox.showerror("Invalid Age", "Please enter a valid age.")
    else:
        messagebox.showwarning("Missing Information", "Please fill all required fields.")


tk.Label(root, text="Patient Registration Form", font=("Arial", 16)).pack(pady=10)


tk.Label(root, text="Name:").pack(anchor="w", padx=20)
name_entry = tk.Entry(root, width=30)
name_entry.pack(padx=20, pady=5)


tk.Label(root, text="Age:").pack(anchor="w", padx=20)
age_entry = tk.Entry(root, width=30)
age_entry.pack(padx=20, pady=5)


tk.Label(root, text="Gender:").pack(anchor="w", padx=20)
gender_var = tk.StringVar(value="Male")
gender_frame = tk.Frame(root)
gender_frame.pack(anchor="w", padx=20)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(side="left")


tk.Label(root, text="Department:").pack(anchor="w", padx=20)
department_listbox = tk.Listbox(root, height=4, selectmode="single")
for department in ["General Medicine", "Pediatrics", "Orthopedics", "Cardiology"]:
    department_listbox.insert(tk.END, department)
department_listbox.pack(padx=20, pady=5)
department_listbox.select_set(0)


tk.Label(root, text="Symptoms:").pack(anchor="w", padx=20)
fever_var = tk.BooleanVar()
cough_var = tk.BooleanVar()
headache_var = tk.BooleanVar()
fatigue_var = tk.BooleanVar()
tk.Checkbutton(root, text="Fever", variable=fever_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Cough", variable=cough_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Headache", variable=headache_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Fatigue", variable=fatigue_var).pack(anchor="w", padx=40)


tk.Label(root, text="Additional Comments:").pack(anchor="w", padx=20)
comments_text = tk.Text(root, height=5, width=30)
comments_text.pack(padx=20, pady=5)


submit_button = tk.Button(root, text="Submit Registration", command=submit_registration)
submit_button.pack(pady=20)


root.mainloop()
