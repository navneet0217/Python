"""
================================================================================
 CHAPTER 1: PYTHON FUNDAMENTALS -- BEGINNER GUIDE & RECAP
================================================================================
 Welcome! This script is your interactive tutorial & quick recap notes.
 You can read through the simple comments or run this file to see everything!

 Topics Covered in this File:
  1. What Is Python & How It Works
  2. Installing & Running Python
  3. Comments & print() Function
  4. Variables & Naming Rules
  5. User input() & Converting Data Types (Type Casting)
  6. Python Data Types & Checking Types
  7. Practice Questions & Step-by-Step Solutions
================================================================================
"""

import sys

# ------------------------------------------------------------------------------
# TOPIC 1: WHAT IS PYTHON & HOW IT WORKS
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("[TOPIC 1] WHAT IS PYTHON & HOW IT WORKS")
print("=" * 60)

# What is Python?
# ---------------
# * Created by Guido van Rossum in 1991.
# * High-level: Easy for humans to read and write (looks like plain English).
# * Interpreted: Runs line-by-line using the Python Virtual Machine (PVM).
# * Dynamically Typed: You don't need to specify data types like int or String manually.

# How Python Code Runs (Under the Hood):
# 1. Your Code (.py file) -> Python Compiler
# 2. Bytecode (.pyc file) -> Python Virtual Machine (PVM)
# 3. Machine Code (0s & 1s) -> Your Computer CPU executes it!

print(f"Current Python Version: {sys.version.split()[0]}")
print("Code Execution Flow: Source Code (.py) -> Bytecode -> PVM -> Output!")


# ------------------------------------------------------------------------------
# TOPIC 2: INSTALLING & RUNNING PYTHON
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("[TOPIC 2] INSTALLING & RUNNING PYTHON")
print("=" * 60)

# How to check your Python version in command line:
#   python --version   (or python3 --version)
#
# How to run any python file from terminal:
#   python filename.py
#
# How to open Interactive Python Shell (REPL):
#   Just type 'python' in terminal and hit Enter!

print("Quick Tip: You can test small code bits directly in terminal by typing 'python'!")


# ------------------------------------------------------------------------------
# TOPIC 3: COMMENTS & THE print() FUNCTION
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("[TOPIC 3] COMMENTS & print() FUNCTION")
print("=" * 60)

# Single-Line Comment: Starts with a hash (#). Python ignores it.

"""
Multi-Line Comment (or Docstring):
Uses triple quotes (\"\"\" or ''').
Great for writing long notes or multi-line explanations!
"""

# 1. Basic Printing
print("Hello, Welcome to Python!")

# 2. Custom Separator (sep="...") - Controls what goes between items
print("Python", "is", "fun", sep=" - ")

# 3. Custom End Character (end="...") - Default end is a new line (\n)
print("Loading data", end="... ")
print("Complete! [OK]")

# 4. Special Characters (Escape Sequences)
# \n = New Line
# \t = Tab Space
print("Line 1\nLine 2\t(Tabbed space)")

# 5. Formatted Strings (f-strings) - The modern way to put variables into text!
language = "Python"
chapter = 1
print(f"Learning {language} -- Chapter {chapter} is in progress!\n")


# ------------------------------------------------------------------------------
# TOPIC 4: VARIABLES & MEMORY BASICS
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("[TOPIC 4] VARIABLES & MEMORY BASICS")
print("=" * 60)

# What is a Variable?
# A variable is like a labeled box that stores data in your computer's memory.

# Variable Naming Rules:
# [YES] Must start with a letter (a-z, A-Z) or an underscore (_)
# [YES] Can contain numbers, but CANNOT start with a number (e.g., age1 is valid, 1age is INVALID)
# [YES] Case-sensitive (age, Age, and AGE are 3 different variables!)
# [NO]  Cannot use Python reserved keywords (like print, input, class, def, return)

# Example 1: Creating variables
student_name = "Alex"     # String (Text)
student_age = 20          # Integer (Whole number)
gpa = 3.8                 # Float (Decimal number)
is_enrolled = True        # Boolean (True or False)

print(f"Student: {student_name}, Age: {student_age}, GPA: {gpa}, Enrolled: {is_enrolled}")

# Example 2: Multiple variables in one line
x, y, z = 5, 10, 15
print(f"x = {x}, y = {y}, z = {z}")

# Example 3: Easy Variable Swapping (Python magic!)
a = 100
b = 200
print(f"Before Swap: a = {a}, b = {b}")

# Swap values in 1 simple line!
a, b = b, a
print(f"After Swap:  a = {a}, b = {b}")


# ------------------------------------------------------------------------------
# TOPIC 5: USER input() & TYPE CASTING
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("[TOPIC 5] USER input() & TYPE CASTING")
print("=" * 60)

# IMPORTANT: The input() function ALWAYS returns data as a STRING ("str")!
# If you want to do math with user input, you must convert (cast) it to int or float.

# Example of converting (casting) data types:
# int("10")    -> Converts string "10" to number 10
# float("5.5") -> Converts string "5.5" to decimal number 5.5
# str(100)     -> Converts number 100 to text "100"

user_birth_year = "2004"  # Simulating input from user
year_number = int(user_birth_year)  # Converting string to integer

calculated_age = 2026 - year_number

print(f"Birth Year (as string): '{user_birth_year}' (Type: {type(user_birth_year).__name__})")
print(f"Birth Year (as int):    {year_number} (Type: {type(year_number).__name__})")
print(f"Calculated Age:         {calculated_age} years old")


# ------------------------------------------------------------------------------
# TOPIC 6: PYTHON DATA TYPES OVERVIEW
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("[TOPIC 6] PYTHON DATA TYPES OVERVIEW")
print("=" * 60)

# Built-in Data Types in Python:
# 1. int      -> Whole numbers (e.g., 42, -7)
# 2. float    -> Decimal numbers (e.g., 3.14, -0.01)
# 3. complex  -> Complex numbers with imaginary part (e.g., 2 + 3j)
# 4. str      -> Text enclosed in quotes (e.g., "Hello World")
# 5. bool     -> True or False
# 6. NoneType -> Represents 'nothing' or absence of value (None)

my_int = 50
my_float = 19.99
my_string = "Python Fundamentals"
my_bool = True
my_none = None

print("Checking data types using type():")
print(f"  Value: {my_int:<20} -> Type: {type(my_int).__name__}")
print(f"  Value: {my_float:<20} -> Type: {type(my_float).__name__}")
print(f"  Value: '{my_string}' -> Type: {type(my_string).__name__}")
print(f"  Value: {my_bool:<20} -> Type: {type(my_bool).__name__}")
print(f"  Value: {str(my_none):<20} -> Type: {type(my_none).__name__}")

# Checking types using isinstance() -- Returns True or False
print(f"\nIs my_int an integer? {isinstance(my_int, int)}")
print(f"Is my_float a string? {isinstance(my_float, str)}")


# ------------------------------------------------------------------------------
# TOPIC 7: PRACTICE QUESTIONS & STEP-BY-STEP SOLUTIONS
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("[TOPIC 7] PRACTICE QUESTIONS & SOLUTIONS")
print("=" * 60)

# ---------------------------------------------------------
# QUESTION 1 (Basic): Simple Calculator
# Task: Take two numbers (e.g., 15.0 and 4.0), convert them to float, 
# and print their Sum, Difference, Product, and Quotient.
# ---------------------------------------------------------
print("\n--- [Question 1] Simple Calculator ---")
num1_str = "15.0"
num2_str = "4.0"

n1 = float(num1_str)
n2 = float(num2_str)

print(f"First Number:  {n1}")
print(f"Second Number: {n2}")
print(f"Sum (+):        {n1 + n2}")
print(f"Difference (-): {n1 - n2}")
print(f"Product (*):    {n1 * n2}")
print(f"Quotient (/):   {n1 / n2}")


# ---------------------------------------------------------
# QUESTION 2 (Basic-Medium): String Price Parser
# Task: You have price = "$49.99". Extract the number 49.99,
# multiply by quantity = 3, and display formatted total.
# ---------------------------------------------------------
print("\n--- [Question 2] Price Parser ---")
raw_price = "$49.99"
quantity = 3

# Step 1: Remove dollar sign '$'
clean_price_str = raw_price.replace("$", "")

# Step 2: Convert to float number
price_number = float(clean_price_str)

# Step 3: Calculate total
total_cost = price_number * quantity

print(f"Original Price Tag: {raw_price}")
print(f"Quantity Purchased: {quantity}")
print(f"Total Amount Due:   ${total_cost:.2f}")


# ---------------------------------------------------------
# QUESTION 3 (Medium): Rotate 3 Variables
# Task: Given x=10, y=20, z=30, swap them so that:
# x gets y's value, y gets z's value, and z gets x's value.
# ---------------------------------------------------------
print("\n--- [Question 3] 3-Variable Rotation ---")
x, y, z = 10, 20, 30
print(f"Original Values: x = {x}, y = {y}, z = {z}")

# Pythonic Rotation Swap:
x, y, z = y, z, x
print(f"Rotated Values:  x = {x}, y = {y}, z = {z}")


# ---------------------------------------------------------
# QUESTION 4 (Medium): Fix the Broken Code
# Broken Code snippet:
#   1_score = "95"
#   print("Total score is: " + 1_score + 5)
# ---------------------------------------------------------
print("\n--- [Question 4] Bug Fix Challenge ---")
print("What was broken in original snippet?")
print("  [ERROR] 1_score starts with a number 1 (Invalid variable name)")
print("  [ERROR] '1_score' (str) cannot be added (+) directly to integer 5 (TypeError)")

# Fixed Code:
score_1 = "95"
final_score = int(score_1) + 5
print(f"[FIXED] Output: Total score is: {final_score}")

print("\n" + "=" * 60)
print("SUCCESS: You completed Chapter 1 Fundamentals!")
print("=" * 60 + "\n")
