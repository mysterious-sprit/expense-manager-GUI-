import tkinter as tk
from tkinter import messagebox
from utils import load_expenses, save_expense
from datetime import datetime

# Initialize main window
root = tk.Tk()
root.title("💸 Expense Tracker")
root.geometry("500x500")

# --- GUI Layout ---

# Expense Input Frame
frame_input = tk.Frame(root, pady=10)
frame_input.pack()

# Amount
tk.Label(frame_input, text="Amount (Rs):").grid(row=0, column=0)
entry_amount = tk.Entry(frame_input)
entry_amount.grid(row=0, column=1)

# Category
tk.Label(frame_input, text="Category:").grid(row=1, column=0)
entry_category = tk.Entry(frame_input)
entry_category.grid(row=1, column=1)

# Description
tk.Label(frame_input, text="Description:").grid(row=2, column=0)
entry_description = tk.Entry(frame_input)
entry_description.grid(row=2, column=1)

# --- Expense List ---
frame_list = tk.Frame(root, pady=10)
frame_list.pack()

listbox_expenses = tk.Listbox(frame_list, width=60, height=10)
listbox_expenses.pack()

# --- Total Display ---
label_total = tk.Label(root, text="Total: Rs 0", font=("Arial", 12, "bold"))
label_total.pack(pady=5)

# --- Add Expense Function ---
def add_expense():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get().strip()
        description = entry_description.get().strip()
        date = datetime.now().strftime("%Y-%m-%d")

        if not category or not description:
            raise ValueError("All fields must be filled.")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        save_expense(expense)
        update_display()
        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_description.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# --- Update Display Function ---
def update_display():
    listbox_expenses.delete(0, tk.END)
    expenses = load_expenses()
    total = 0
    for exp in expenses:
        line = f"{exp['date']} - Rs {exp['amount']} - {exp['category']} - {exp['description']}"
        listbox_expenses.insert(tk.END, line)
        total += exp['amount']
    label_total.config(text=f"Total: Rs {total}")

# --- Add Button ---
btn_add = tk.Button(root, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white")
btn_add.pack(pady=10)

# Load existing data on start
update_display()

# Start GUI loop
root.mainloop()
