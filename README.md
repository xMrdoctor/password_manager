
# 🔐 Local Password Manager - Python + Tkinter + SQLite3

A simple, lightweight and secure **offline password manager** built with Python, using Tkinter for GUI and SQLite3 for local storage.

---

## 🎯 Project Goal
The purpose of this project is to provide a **basic and secure GUI-based password manager** for storing and retrieving passwords **locally**, without the need for an internet connection or external services.

---

## 💡 Features

- Add passwords with `Website`, `Username`, and `Password` fields
- Secure password storage using `SHA-256` hashing
- View saved passwords in a clean and simple Tkinter window
- Clean separation of logic and helper functions
- Easy to use and extend for more advanced features

---

## 🗂 Project Structure

```
Tkinter_Password_Manager/
├── main.py                # Main GUI logic and database interaction
├── db/passwords.db        # Local SQLite3 database (auto-created)
├── utils/helpers.py       # Password hashing utility
├── assets/                # Optional folder for icons or future assets
└── README.md              # This documentation file
```

---

## 📦 Requirements

- Python 3.x
- Tkinter (comes with Python)
- SQLite3 (built into Python)
- No external dependencies

---

## 🚀 How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Tkinter_Password_Manager.git
    cd Tkinter_Password_Manager
    ```

2. Run the application:
    ```bash
    python main.py
    ```

> 💡 Note: A `passwords.db` file will automatically be created inside a `/db` folder the first time the app runs.

---

## 🔐 Security Note

- Passwords are **hashed** using SHA-256 before being stored.
- This is a simple local manager and **not** meant for enterprise-level security.
- For higher security, consider using salt + encryption (e.g., Fernet) and master passwords.

---

## 🧠 Use Case

Perfect for developers, students, or learners who want to:
- Learn GUI programming with Tkinter
- Practice SQLite3 local data storage
- Understand password hashing basics
- Build a real-world Python project

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify.

---

> Built with 💻 by [YourName]
