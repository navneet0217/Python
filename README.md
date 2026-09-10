# 🐍 Python Mastery Roadmap — Chapter-by-Chapter Journey

Welcome to the **Python Learning Repository**! This repository tracks a structured, step-by-step journey from core Python fundamentals to advanced software development concepts.

---

## 🗺️ Chapter Roadmap

| Chapter | Title | Status | Link |
| :--- | :--- | :---: | :--- |
| **01** | **Python Fundamentals** | 🟢 Completed | [01_python_fundamentals.py](file:///d:/Python/Chapter%201%20-%20Python%20Fundamentals/01_python_fundamentals.py) |
| **02** | **Control Flow & Decision Making** | ⏳ Upcoming | `Chapter 2 - Control Flow` |
| **03** | **Loops & Iteration** | ⏳ Upcoming | `Chapter 3 - Loops` |
| **04** | **Functions & Scope** | ⏳ Upcoming | `Chapter 4 - Functions` |
| **05** | **Data Structures in Depth** | ⏳ Upcoming | `Chapter 5 - Data Structures` |
| **06** | **Object-Oriented Programming (OOP)** | ⏳ Upcoming | `Chapter 6 - OOP` |
| **07** | **File I/O & Exception Handling** | ⏳ Upcoming | `Chapter 7 - File IO` |
| **08** | **Modules, Packages & Virtual Envs** | ⏳ Upcoming | `Chapter 8 - Modules` |

---

## 📖 Chapter Breakdown

### 📘 Chapter 1 — Python Fundamentals
📁 **Directory:** [`Chapter 1 - Python Fundamentals`](file:///d:/Python/Chapter%201%20-%20Python%20Fundamentals)  
📄 **Main Script:** [`01_python_fundamentals.py`](file:///d:/Python/Chapter%201%20-%20Python%20Fundamentals/01_python_fundamentals.py)

#### 🎯 Key Concepts Covered:
1. **What Is Python & How It Works**
   - High-level, interpreted, dynamically-typed language.
   - Pipeline: `.py` Source Code ➔ Bytecode (`.pyc`) ➔ Python Virtual Machine (PVM) ➔ Machine Code.
2. **Installing & Running Python**
   - Verification (`python --version`), REPL mode, running scripts (`python main.py`).
3. **Comments & `print()`**
   - Single-line (`#`) & Multi-line (`"""..."""`) comments.
   - `print()` arguments (`sep`, `end`), escape sequences (`\n`, `\t`), and `f-strings`.
4. **Variables & Memory**
   - Naming rules (snake_case, valid initial characters, keyword restrictions).
   - Dynamic typing, variable swapping (`a, b = b, a`), and object identity (`id()`).
5. **User `input()` & Type Casting**
   - Reading input as `str`, converting via `int()`, `float()`, `bool()`, `str()`.
6. **Python Data Types**
   - Primitives: `int`, `float`, `complex`, `str`, `bool`, `NoneType`.
   - Collections preview: `list`, `tuple`, `dict`, `set`.
   - Type inspection: `type()` and `isinstance()`.

---

## ⚡ Quick Recap Cheat Sheet

### 1. `print()` Customizations & F-Strings
```python
# Custom separator and end character
print("2026", "09", "10", sep="-", end="\n\n")

# F-String Formatting
name = "Dev"
score = 98.5
print(f"User: {name} | Score: {score:.2f}%")
```

### 2. Variable Rotation & Dynamic Typing
```python
# Pythonic Swapping (No temp variable needed)
a, b, c = 10, 20, 30
a, b, c = b, c, a  # a=20, b=30, c=10

# Type Checking
x = 42
print(isinstance(x, int))  # True
```

### 3. User Input & Casting
```python
age_str = input("Enter age: ")  # Returns str
age = int(age_str)              # Cast to int for arithmetic operations
```

---

## 🏋️ Practice Questions Summary (Basic ➔ Medium)

The python script includes testable implementations for the following practice problems:

1. **Q1 (Basic Calculator):** Read two numbers, cast to float, and output formatted arithmetic (Sum, Difference, Product, Quotient).
2. **Q2 (String Parsing & Math):** Extract float value from formatted price string `"$49.99"` and calculate total for multiple items.
3. **Q3 (3-Variable Rotation):** Rotate values across 3 variables without using auxiliary storage.
4. **Q4 (Debugging Challenge):** Identify and resolve syntax/type concatenation bugs in raw code snippets.

---

## 🚀 How to Run the Examples

Open your terminal in the workspace root (`d:\Python`) and execute:

```bash
python "Chapter 1 - Python Fundamentals/01_python_fundamentals.py"
```