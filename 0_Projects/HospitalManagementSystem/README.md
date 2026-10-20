# 🏥 Hospital Management System

A **console-based Hospital Management System** built with Python and Object-Oriented Programming (OOP). This project helps manage hospital records for doctors, employees, and patients through CRUD operations, with JSON-based data persistence.

## ✨ Features

- 🩺 **Doctor Management** — Add, view, update, and delete doctor records.
- 👨‍💼 **Employee Management** — Manage employee information and records.
- 🧑‍⚕️ **Patient Management** — Manage patient details, assigned doctors, and room numbers.
- 🔄 **CRUD Operations** — Create, read, update, and delete records.
- 💾 **JSON Data Persistence** — Save hospital records to a JSON file and load them when the application starts.
- ✅ **Input Validation** — Validate user input to help prevent invalid data.
- 🧩 **Object-Oriented Design** — Organize the project using classes, objects, and reusable methods.

## 🛠️ Technologies Used

- **Python 3**
- **Object-Oriented Programming (OOP)**
- **JSON** for data storage
- **Git & GitHub** for version control

## 📂 Project Structure

```text
HospitalManagementSystem/
│
├── main.py              # Application entry point and menus
├── hospital.py          # Hospital class and CRUD operations
├── doctor.py            # Doctor class
├── employee.py          # Employee class
├── patient.py           # Patient class
├── utils.py             # Reusable input and validation helpers
├── hospital_data.json   # Saved hospital records
└── README.md            # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
https://github.com/faizanali725/learning.git
```

### 2. Navigate to the Project Folder

```bash
cd HospitalManagementSystem
```

### 3. Run the Application

```bash
python main.py
```

**Requirements:** Python 3 installed on your system. No external packages are required if the project uses only Python's standard library.

## 💾 Data Storage

Hospital records are stored in `hospital_data.json`.

- Existing records are loaded when the application starts.
- Changes made through supported CRUD operations are saved to the JSON file.
- Keep the JSON file safe to preserve your records.

> **Note:** Avoid manually changing the JSON structure unless you understand the expected format.

## 🎯 Learning Objectives

This project demonstrates practical use of:

- Classes and objects
- Constructors and instance attributes
- Encapsulation and methods
- Dictionaries for record management
- CRUD operations
- Exception handling and input validation
- Reading and writing JSON data
- Organizing Python code across multiple modules

## 🔮 Future Improvements

- Add automated unit tests.
- Improve search and filtering options.
- Add a graphical user interface (GUI).
- Introduce a database such as SQLite.
- Add user authentication and role-based access.

## 👨‍💻 Author

**Faizan Ali**

An aspiring AI professional learning Python, OOP, and software development through hands-on projects.

---

⭐ If you find this project useful, consider giving the repository a star!
