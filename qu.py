import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Online Quiz")
window.geometry("400x300")


selected_answer = tk.StringVar()


quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
]


current_question = 0

def load_question():
    global current_question
    question_data = quiz_data[current_question]
    
    
    label_question.config(text=question_data["question"])
    
   
    for widget in frame_options.winfo_children():
        widget.destroy()
    
  
    for option in question_data["options"]:
        tk.Radiobutton(frame_options, text=option, variable=selected_answer, value=option).pack(anchor="w")

def check_answer():
    global current_question
    selected = selected_answer.get()
    correct_answer = quiz_data[current_question]["answer"]
    
    if selected == correct_answer:
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect", f"The correct answer is {correct_answer}")
    
   
    current_question += 1
    if current_question < len(quiz_data):
        load_question()
    else:
        messagebox.showinfo("Quiz Finished", "You've completed the quiz!")
        window.quit()


label_question = tk.Label(window, text="Question will appear here", font=("Arial", 14), wraplength=300)
label_question.pack(pady=20)


frame_options = tk.Frame(window)
frame_options.pack(pady=10)


submit_button = tk.Button(window, text="Submit", command=check_answer)
submit_button.pack(pady=20)


load_question()

window.mainloop()
