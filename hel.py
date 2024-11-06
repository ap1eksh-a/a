import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Help")
root.geometry("500x500")


def contact_support():
    messagebox.showinfo("Contact Support", "For further assistance, please email support@example.com or call 1-800-123-HELP.")


def show_troubleshooting_tips():
    messagebox.showinfo("Troubleshooting Tips", 
                        "1. Restart the app if it is not responding.\n"
                        "2. Ensure you have an active internet connection.\n"
                        "3. Clear the cache if you experience slow performance.\n"
                        "4. Update the app to the latest version.")


tk.Label(root, text="Help Center", font=("Arial", 18, "bold")).pack(pady=10)


tk.Label(root, text="How to Use the App", font=("Arial", 14)).pack(anchor="w", padx=20, pady=(10, 0))
tk.Label(root, text="1. Navigate through the main menu to access features.\n"
                    "2. Use the 'Settings' tab to customize your experience.\n"
                    "3. Check 'Notifications' for updates and messages.\n"
                    "4. Visit 'Profile' to manage your account.",
         wraplength=460, justify="left").pack(anchor="w", padx=20, pady=5)


tk.Label(root, text="Troubleshooting Common Issues", font=("Arial", 14)).pack(anchor="w", padx=20, pady=(10, 0))
troubleshoot_button = tk.Button(root, text="View Troubleshooting Tips", command=show_troubleshooting_tips)
troubleshoot_button.pack(anchor="w", padx=20, pady=5)


tk.Label(root, text="Need Further Assistance?", font=("Arial", 14)).pack(anchor="w", padx=20, pady=(10, 0))
contact_button = tk.Button(root, text="Contact Support", command=contact_support)
contact_button.pack(anchor="w", padx=20, pady=5)


tk.Label(root, text="FAQs", font=("Arial", 14)).pack(anchor="w", padx=20, pady=(10, 0))
tk.Label(root, text="Q: How do I reset my password?\n"
                    "A: Go to 'Profile' > 'Settings' > 'Reset Password'.\n\n"
                    "Q: Can I use the app offline?\n"
                    "A: Some features may be available offline, but an internet connection is required for full functionality.\n\n"
                    "Q: How do I report a bug?\n"
                    "A: Use the 'Feedback' section in the main menu.",
         wraplength=460, justify="left").pack(anchor="w", padx=20, pady=5)


root.mainloop()
