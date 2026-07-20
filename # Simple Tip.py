import tkinter as tk

def calculate_tip():
    try:
        bill = float(bill_entry.get())
        tip = float(tip_entry.get())

        total = bill + tip

        result_label.config(
            text=f"Bill Amount: ₹{bill:.2f}\n"
                 f"Tip Amount: ₹{tip:.2f}\n"
                 f"Total Amount: ₹{total:.2f}"
        )
    except:
        result_label.config(text="Please enter valid numbers!")

# Window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("400x450")
root.configure(bg="sky blue")

# Heading
title = tk.Label(
    root,
    text="TIP CALCULATOR",
    font=("Arial", 20, "bold"),
    bg="sky blue"
)
title.pack(pady=20)

# Bill Amount
tk.Label(root,
         text="Bill Amount (₹)",
         font=("Arial", 12),
         bg="sky blue").pack()

bill_entry = tk.Entry(root, font=("Arial", 14))
bill_entry.pack(pady=5)

# Tip Amount
tk.Label(root,
         text="Tip Amount (₹)",
         font=("Arial", 12),
         bg="sky blue").pack()

tip_entry = tk.Entry(root, font=("Arial", 14))
tip_entry.pack(pady=5)

# Button
tk.Button(
    root,
    text="Calculate",
    font=("Arial", 14, "bold"),
    bg="orange",
    command=calculate_tip
).pack(pady=20)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="sky blue"
)
result_label.pack(pady=20)

root.mainloop()