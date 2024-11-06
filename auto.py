import tkinter as tk
from tkinter import messagebox

def book_ride():
    pickup = entry_pickup.get()
    dropoff = entry_dropoff.get()
    vehicle = vehicle_type.get()

    if pickup and dropoff and vehicle:
        messagebox.showinfo("Booking Confirmed", f"Ride booked from {pickup} to {dropoff} by {vehicle}.")
    else:
        messagebox.showwarning("Incomplete Information", "Please fill in all the details.")

def cancel_booking():
    entry_pickup.delete(0, tk.END)
    entry_dropoff.delete(0, tk.END)
    vehicle_type.set(None)


window = tk.Tk()
window.title("Cab/Auto Booking App")
window.geometry("400x300")


tk.Label(window, text="Pickup Location:").pack(pady=5)
entry_pickup = tk.Entry(window, width=30)
entry_pickup.pack(pady=5)


tk.Label(window, text="Drop-off Location:").pack(pady=5)
entry_dropoff = tk.Entry(window, width=30)
entry_dropoff.pack(pady=5)


tk.Label(window, text="Select Vehicle Type:").pack(pady=5)
vehicle_type = tk.StringVar(value=None)

tk.Radiobutton(window, text="Cab", variable=vehicle_type, value="Cab").pack(anchor="w", padx=20)
tk.Radiobutton(window, text="Auto", variable=vehicle_type, value="Auto").pack(anchor="w", padx=20)
tk.Radiobutton(window, text="Bike", variable=vehicle_type, value="Bike").pack(anchor="w", padx=20)


frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=20)

btn_book = tk.Button(frame_buttons, text="Book Ride", command=book_ride)
btn_book.grid(row=0, column=0, padx=10)

btn_cancel = tk.Button(frame_buttons, text="Cancel", command=cancel_booking)
btn_cancel.grid(row=0, column=1, padx=10)


window.mainloop()
