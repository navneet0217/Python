"""
Python Fundamentals — Basic se Medium tak
==========================================
Cover kar rahe hain: Python kya hai, print(), variables, input() +
type casting, aur data types check karna.
Har section ke end mein practice questions hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

import sys

# ============================================================
# 1. PYTHON KYA HAI & KAISE CHALTA HAI?
# ============================================================
# Python ek high-level, interpreted language hai — line by line chalti hai.
# Tumhe types (int, str, etc.) manually specify karne ki zaroorat nahi
# (dynamically typed).

print("1. Python version:", sys.version.split()[0])
print("   Flow: Source Code (.py) -> Bytecode -> Python Virtual Machine -> Output")


# ============================================================
# 2. print() KAISE USE KAREIN?
# ============================================================
print("\n2. print() ke tarike:")

# Simple print
print("   Hello, Python!")

# sep -> beech mein kya aayega
print("   ", "Python", "is", "fun", sep=" - ")

# end -> line ke end mein kya aayega (default \n)
print("   Loading", end="... ")
print("Done!")

# f-string -> variable ko seedha string mein daalna
language = "Python"
chapter = 1
print(f"   Learning {language}, Chapter {chapter}")


# ============================================================
# 3. VARIABLES KAISE BANAYEIN?
# ============================================================
# Variable ek labeled box hai jisme data store hota hai.
# Rules: letter/underscore se start, number se nahi; case-sensitive;
# reserved keyword (print, class, etc.) use nahi kar sakte.

student_name = "Alex"
student_age = 20
gpa = 3.8
is_enrolled = True

print(f"\n3. Student: {student_name}, Age: {student_age}, GPA: {gpa}, Enrolled: {is_enrolled}")

# Ek line mein multiple variables
x, y, z = 5, 10, 15
print("   x, y, z:", x, y, z)

# Swap — Python ka magic, temp variable ki zaroorat nahi
a, b = 100, 200
a, b = b, a
print("   Swapped a, b:", a, b)


# ============================================================
# 4. input() aur TYPE CASTING KAISE KAAM KARTA HAI?
# ============================================================
# input() hamesha STRING return karta hai — math karne ke liye
# int()/float() se convert (cast) karna padega.

user_birth_year = "2004"  # yaha input() simulate kar rahe hain
year_number = int(user_birth_year)
calculated_age = 2026 - year_number

print(f"\n4. Birth year (string): '{user_birth_year}'")
print(f"   Birth year (int):    {year_number}")
print(f"   Calculated age:      {calculated_age}")


# ============================================================
# 5. DATA TYPES KAISE CHECK KAREIN?
# ============================================================
my_int = 50
my_float = 19.99
my_string = "Fundamentals"
my_bool = True
my_none = None

print("\n5. type() se check:")
for val in (my_int, my_float, my_string, my_bool, my_none):
    print(f"   {str(val):<15} -> {type(val).__name__}")

# isinstance() -> True/False mein batata hai
print("   isinstance(my_int, int):", isinstance(my_int, int))
print("   isinstance(my_float, str):", isinstance(my_float, str))


# ============================================================
# PRACTICE — Basic to Medium
# ============================================================
"""
Q1 (Basic): num1_str = "15.0", num2_str = "4.0" ko float mein convert karo
            aur unka sum, difference, product, quotient print karo.

Q2 (Basic-Medium): raw_price = "$49.99", quantity = 3. '$' hatao, float mein
                    convert karo, total nikalo aur 2 decimal places tak
                    print karo.

Q3 (Medium): x, y, z = 10, 20, 30 ko is tarah rotate karo ki x ko y ki
             value mile, y ko z ki, aur z ko x ki (ek line mein).

Q4 (Medium): Yeh broken code fix karo:
                 1_score = "95"
                 print("Total: " + 1_score + 5)
             (Hint: variable naming rule + type mismatch dono issues hain)

Q5 (Basic): a = 5, b = 10 ko bina temp variable use kiye swap karo.

Q6 (Basic): user_age_str = "twenty" ko int() se convert karne ki koshish
            karo. Agar ValueError aaye to try/except se handle karo aur
            "Invalid age entered" print karo. (Edge case: bad input)

Q7 (Basic-Medium): name = "Riya", marks = 88.5. f-string use karke
                    "Riya scored 88.5 marks" print karo, aur marks ka
                    type() bhi print karo.

Q8 (Medium): radius_str = "0". Ise float mein convert karke circle ka
             area nikalo (formula: 3.14159 * r * r). Yeh ek edge case
             hai — radius zero hone par area kya aata hai, check karo.
"""


# ============================================================
# SOLUTIONS
# ============================================================

def practice_solutions():
    print("\n--- PRACTICE SOLUTIONS ---")

    # Q1
    n1 = float("15.0")
    n2 = float("4.0")
    print(f"Q1 -> sum: {n1 + n2} | diff: {n1 - n2} | product: {n1 * n2} | quotient: {n1 / n2}")

    # Q2
    raw_price = "$49.99"
    quantity = 3
    price_number = float(raw_price.replace("$", ""))
    total_cost = price_number * quantity
    print(f"Q2 -> total: ${total_cost:.2f}")

    # Q3
    x, y, z = 10, 20, 30
    x, y, z = y, z, x
    print(f"Q3 -> x: {x}, y: {y}, z: {z}")

    # Q4
    score_1 = "95"  # variable ka naam number se start nahi ho sakta
    final_score = int(score_1) + 5  # string ko int mein convert karna zaroori tha
    print(f"Q4 -> Total: {final_score}")

    # Q5
    a, b = 5, 10
    a, b = b, a
    print(f"Q5 -> a: {a}, b: {b}")

    # Q6
    user_age_str = "twenty"
    try:
        user_age = int(user_age_str)
        print("Q6 ->", user_age)
    except ValueError:
        print("Q6 -> Invalid age entered")

    # Q7
    name, marks = "Riya", 88.5
    print(f"Q7 -> {name} scored {marks} marks | type: {type(marks).__name__}")

    # Q8
    radius_str = "0"
    radius = float(radius_str)
    area = 3.14159 * radius * radius
    print(f"Q8 -> area: {area}")


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add python fundamentals basics-to-medium practice script
