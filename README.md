# 💸 Personal Expense Tracker (GUI)

A simple and user-friendly desktop app to track your daily expenses using Python and Tkinter.

---

## ✨ Features

- Add expenses with amount, category, and description
- View all recorded expenses
- Automatically calculates total expenses
- Data stored in a local JSON file
- Clean and responsive Tkinter GUI

---

## 🖥️ Screenshot

> Add a screenshot here (optional)

---

## 🚀 Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/expense-tracker-gui.git
cd expense-tracker-gui
```

### 2. Run the app:
```bash
python main.py
```

No extra libraries required. Uses Python’s built-in modules only (`tkinter`, `json`, `datetime`, `os`).

---

## 🗃️ Folder Structure
```
expense-tracker-gui/
├── main.py             # Main GUI app
├── utils.py            # Helper functions (save/load)
├── data.json           # Stored expenses (auto-created)
├── .gitignore
└── README.md
```

---

## 📦 Data Format (data.json)
```json
[
  {
    "amount": 250,
    "category": "Groceries",
    "description": "Fruits and snacks",
    "date": "2025-06-19"
  }
]
```

---

## 📌 To Do / Ideas
- Filter expenses by category or date
- Export data to CSV
- Monthly budget summary

---

## 📄 License
MIT License.

---

Made with ❤️ in Python.
