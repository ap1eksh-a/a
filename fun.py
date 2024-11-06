import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Fund Transfer")
root.geometry("400x400")


def transfer_funds():
    sender_account = sender_entry.get()
    recipient_account = recipient_entry.get()
    amount = amount_entry.get()
    
    if sender_account and recipient_account and amount:
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount should be greater than 0.")
            messagebox.showinfo("Success", f"Transfer of ₹{amount} from account {sender_account} to {recipient_account} completed successfully.")
        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))
    else:
        messagebox.showwarning("Missing Information", "Please fill all fields.")


tk.Label(root, text="Fund Transfer", font=("Arial", 18)).pack(pady=20)


tk.Label(root, text="Sender's Account Number:").pack(anchor="w", padx=20)
sender_entry = tk.Entry(root, width=30)
sender_entry.pack(padx=20, pady=5)


tk.Label(root, text="Recipient's Account Number:").pack(anchor="w", padx=20)
recipient_entry = tk.Entry(root, width=30)
recipient_entry.pack(padx=20, pady=5)


tk.Label(root, text="Amount (₹):").pack(anchor="w", padx=20)
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(padx=20, pady=5)


transfer_button = tk.Button(root, text="Confirm Transfer", command=transfer_funds)
transfer_button.pack(pady=20)


root.mainloop()
