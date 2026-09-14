"""
================================================================================
CHAPTER 3: PYTHON NUMBERS - COMPLETE REFERENCE GUIDE
================================================================================
Based on the Numeric Concept Map:
1. Types          : type(), int(), float(), complex()
2. Math Operators : +, -, *, /, //, %, **
3. Rounding       : abs(), round(), math.ceil(), math.floor(), math.trunc()
4. Advanced Math  : math.sqrt(), math.sin(), math.cos(), math.log()
5. Random         : random.random(), random.randint()
6. Validation     : .is_integer(), isinstance()
================================================================================
"""

import math
import random


# ================================================================================
# 1. NUMERIC TYPES: int, float, complex
# ================================================================================
# Integers are whole numbers (positive or negative)
num_int = 10
print("Integer:", num_int, "| Type:", type(num_int))  # <class 'int'>

# Floats are decimal numbers
num_float = 3.14
print("Float:", num_float, "| Type:", type(num_float))  # <class 'float'>

# Complex numbers have real and imaginary parts (j represents sqrt(-1))
num_complex = 2 + 3j
print("Complex:", num_complex, "| Type:", type(num_complex))  # <class 'complex'>

# Type Conversions
print("int(3.8):", int(3.8))      # 3 (converts to int by dropping decimals)
print("float(5):", float(5))      # 5.0 (converts int to float)


# ================================================================================
# 2. MATH OPERATORS
# ================================================================================
a, b = 3, 2

print("Addition (+):", a + b)           # 3 + 2 = 5
print("Subtraction (-):", a - b)        # 3 - 2 = 1
print("Multiplication (*):", a * b)     # 3 * 2 = 6
print("Division (/):", a / b)           # 3 / 2 = 1.5 (always returns a float)
print("Floor Division (//):", a // b)   # 3 // 2 = 1 (rounds down to whole number)
print("Modulus / Remainder (%):", a % b) # 3 % 2 = 1 (remainder after division)
print("Exponentiation (**):", a ** b)   # 3 ** 2 = 9 (3 raised to power of 2)


# ================================================================================
# 3. ROUNDING FUNCTIONS
# ================================================================================
# abs() -> Returns absolute (positive) value
print("abs(-5):", abs(-5))              # 5

# round() -> Rounds to nearest integer or specified decimal places
print("round(3.7):", round(3.7))        # 4
print("round(3.14159, 2):", round(3.14159, 2))  # 3.14

# math.ceil() -> Always rounds UP to next integer
print("math.ceil(3.2):", math.ceil(3.2))  # 4

# math.floor() -> Always rounds DOWN to previous integer
print("math.floor(3.8):", math.floor(3.8))  # 3

# math.trunc() -> Truncates (cuts off) decimals towards zero
print("math.trunc(3.9):", math.trunc(3.9))  # 3


# ================================================================================
# 4. ADVANCED MATH FUNCTIONS (math module)
# ================================================================================
print("math.sqrt(16):", math.sqrt(16))    # 4.0 (square root)
print("math.sin(0):", math.sin(0))        # 0.0 (sine of angle in radians)
print("math.cos(0):", math.cos(0))        # 1.0 (cosine of angle in radians)
print("math.log(10):", math.log(10))      # 2.30258... (natural log base e)


# ================================================================================
# 5. RANDOM NUMBER GENERATION (random module)
# ================================================================================
# random.random() -> Returns random float between 0.0 and 1.0
print("random.random():", random.random())

# random.randint(a, b) -> Returns random integer between a and b (inclusive)
print("random.randint(1, 100):", random.randint(1, 100))


# ================================================================================
# 6. NUMERIC VALIDATION
# ================================================================================
# .is_integer() -> Checks if float has no fractional part (e.g. 4.0 is int-like)
val1 = 4.0
val2 = 4.5
print("(4.0).is_integer():", val1.is_integer())  # True
print("(4.5).is_integer():", val2.is_integer())  # False

# isinstance() -> Checks if a variable belongs to a specific data type
print("isinstance(5, int):", isinstance(5, int))        # True
print("isinstance(3.14, float):", isinstance(3.14, float))  # True


# ================================================================================
# PRACTICAL EXERCISE: Random Even Number Check
# Question: Generate a random integer from 1 to 100 and check if it is even
# ================================================================================
rand_num = random.randint(1, 100)
is_even = (rand_num % 2 == 0)

print("\n--- Practical Exercise Output ---")
print("Generated Number:", rand_num)
print("Is Even?:", is_even)
