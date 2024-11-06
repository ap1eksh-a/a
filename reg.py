import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = listbox_courses.get(tk.ACTIVE)
    agree = agree_var.get()

    if not name or not age or gender == "Select" or course == "" or not agree:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields and agree to the terms.")
    else:
        messagebox.showinfo("Registration Successful", f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}")

window = tk.Tk()
window.title("Student Registration Form")
window.geometry("400x400")


tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1, padx=10, pady=10)


gender_var = tk.StringVar(value="Select")
tk.Label(window, text="Gender:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky=tk.W)
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, sticky=tk.W)


tk.Label(window, text="Select Course:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
listbox_courses = tk.Listbox(window, height=4)
courses = ["Computer Science", "Mathematics", "Physics", "Chemistry"]
for course in courses:
    listbox_courses.insert(tk.END, course)
listbox_courses.grid(row=3, column=1, padx=10, pady=10)


agree_var = tk.BooleanVar()
check_agree = tk.Checkbutton(window, text="I agree to the terms and conditions", variable=agree_var)
check_agree.grid(row=4, columnspan=3, padx=10, pady=10)


submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=5, columnspan=3, padx=10, pady=20)

window.mainloop()
