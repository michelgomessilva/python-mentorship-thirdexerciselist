# 🚀 Python Mentorship: Third Exercise List

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Mentorship](https://img.shields.io/badge/Mentorship-Squad%20Academy-purple)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)
![Last Commit](https://img.shields.io/github/last-commit/michelgomessilva/python-mentorship-thirdexerciselist)

This repository contains the **third practical programming logic exercise list in Python**, created by mentor **Michel Silva** for students of **Squad Academy**.

The goal of this exercise list is to strengthen the foundations of:

- Complex data structures (Sets, Tuplas, Dicionários)
- Conditional and structural logic
- Exception handling and data integrity
- Input validation and sanitization
- Clean Code and programming best practices

All exercises simulate **real-world scenarios**, applying **robust data validation** and modern Python features.

---

# 📚 Project Structure

```text
python-mentorship-thirdexerciselist
│
├── main.py
│
├── atm_simulator.py
├── data_miner.py
├── inventory_pro_manager.py
├── password_validator.py
├── server_log_processor.py
└── sum_interval.py
```

---

# 📋 Prerequisites

This project uses **uv**, the fastest modern Python package and environment manager.

Install **uv**:

### Windows (PowerShell)

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

# 📥 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/michelgomessilva/python-mentorship-thirdexerciselist.git
cd python-mentorship-thirdexerciselist
```

---

## 2️⃣ Create the Virtual Environment

```bash
uv sync
```

This command:

- creates the `.venv`
- installs dependencies
- prepares the execution environment

---

## 3️⃣ Activate the Virtual Environment

### Windows

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

# ▶️ How to Run

## Main Menu (Hub)

Runs the **central exercise hub** with a colored interface.

```bash
uv run main.py
```

---

## Run an Individual Exercise

```bash
uv run file_name.py
```

Example:

```bash
uv run atm_simulator.py
```

---

# 🧪 Mentorship Exercises

| # | Exercise | File | Description |
|---|---|---|---|
| 1 | Sum Interval | `sum_interval.py` | Calculate the sum of integers from 1 to 100 with validation |
| 2 | Password Validator | `password_validator.py` | Access control simulation with password verification and limits |
| 3 | Data Miner | `data_miner.py` | Matrix filtering for specific numerical conditions (Multiples of 3 and > 10) |
| 4 | ATM Simulator | `atm_simulator.py` | Cash withdrawal logic using the fewest bills possible (Greedy Algorithm) |
| 5 | Server Logs | `server_log_processor.py` | User activity analysis based on server log data with unique page sets |
| 6 | Inventory Pro | `inventory_pro_manager.py` | Advanced stock management using dictionaries, sets, and tuples |

---

# 🎯 Learning Objectives

During these exercises, students will practice:

- Advanced data structures (Sets, Tuples, Dictionaries)
- Deep input validation and data sanitization
- Exception handling and error reporting
- Code modularity and organization
- Interactive terminal UI design

---

# 🛠 Technologies Used

- **Python 3.12+**
- **uv**
- **Git**
- **Antigravity**

---

# 👨🏫 Mentorship

Project created for the **Python Fundamentals Mentorship Program** led by:

**Michel Silva**

Squad Academy 🐍

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to study, modify, and use it for educational purposes.
