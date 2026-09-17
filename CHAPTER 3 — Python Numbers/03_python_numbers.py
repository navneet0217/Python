"""
Python Numbers — Basic se Medium tak
=====================================
Cover kar rahe hain: number types, math operators, rounding,
advanced math (sqrt/sin/cos/log), random numbers, aur validation.
Har section ke end mein practice questions hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

import math
import random

# ============================================================
# 1. NUMBER TYPES KYA HAIN?
# ============================================================
num_int = 10
num_float = 3.14
num_complex = 2 + 3j  # j = sqrt(-1)

print("1. Types:")
print("   int:", num_int, "->", type(num_int).__name__)
print("   float:", num_float, "->", type(num_float).__name__)
print("   complex:", num_complex, "->", type(num_complex).__name__)

print("   int(3.8):", int(3.8), "(decimal drop ho jata hai)")
print("   float(5):", float(5))


# ============================================================
# 2. MATH OPERATORS KAISE KAAM KARTE HAIN?
# ============================================================
a, b = 3, 2
print("\n2. Operators (a=3, b=2):")
print("   a + b  :", a + b)
print("   a - b  :", a - b)
print("   a * b  :", a * b)
print("   a / b  :", a / b, "(hamesha float return karta hai)")
print("   a // b :", a // b, "(floor division — round down)")
print("   a % b  :", a % b, "(modulus — remainder)")
print("   a ** b :", a ** b, "(power)")


# ============================================================
# 3. ROUNDING KAISE KAREIN?
# ============================================================
print("\n3. Rounding:")
print("   abs(-5):", abs(-5))
print("   round(3.7):", round(3.7))
print("   round(3.14159, 2):", round(3.14159, 2))
print("   math.ceil(3.2):", math.ceil(3.2), "(hamesha upar)")
print("   math.floor(3.8):", math.floor(3.8), "(hamesha neeche)")
print("   math.trunc(3.9):", math.trunc(3.9), "(decimal cut, zero ki taraf)")


# ============================================================
# 4. ADVANCED MATH (math module)
# ============================================================
print("\n4. Advanced math:")
print("   math.sqrt(16):", math.sqrt(16))
print("   math.sin(0):", math.sin(0))
print("   math.cos(0):", math.cos(0))
print("   math.log(10):", math.log(10), "(natural log, base e)")


# ============================================================
# 5. RANDOM NUMBERS KAISE GENERATE KAREIN?
# ============================================================
print("\n5. Random:")
print("   random.random():", random.random(), "(0.0 se 1.0 ke beech)")
print("   random.randint(1, 100):", random.randint(1, 100), "(dono end inclusive)")


# ============================================================
# 6. NUMBER VALIDATE KAISE KAREIN?
# ============================================================
val1, val2 = 4.0, 4.5
print("\n6. Validation:")
print("   (4.0).is_integer():", val1.is_integer())
print("   (4.5).is_integer():", val2.is_integer())
print("   isinstance(5, int):", isinstance(5, int))
print("   isinstance(3.14, float):", isinstance(3.14, float))


# ============================================================
# PRACTICE — Basic to Medium
# ============================================================
"""
Q1 (Basic): 17 ko 5 se divide karo — normal division (/), floor division
            (//), aur modulus (%) teeno print karo.

Q2 (Basic): Ek number 7.567 ko round karke 2 decimal places tak print karo,
            phir math.ceil() aur math.floor() bhi laga kar dekho.

Q3 (Medium): random.randint(1, 100) se ek number generate karo aur check
             karo ki woh even hai ya odd (% operator use karo).

Q4 (Medium): Ek right-angled triangle ke do sides diye hain: base=3, height=4.
             math.sqrt() use karke hypotenuse nikalo
             (formula: sqrt(base**2 + height**2)).

Q5 (Basic): n = 7. Check karo ki yeh prime number hai ya nahi (2 se n-1
            tak divide karke dekho).

Q6 (Basic): celsius = 37. Ise Fahrenheit mein convert karo
            (formula: F = C * 9/5 + 32).

Q7 (Medium): num = 1234. Iske sab digits ka sum nikalo (1+2+3+4 = 10),
             string conversion ya modulus dono tarike try kar sakte ho.

Q8 (Medium): negative_num = -7.8. Isme abs(), round(), math.floor(), aur
             math.ceil() laga kar dekho — negative numbers pe yeh kaise
             behave karte hain, yeh edge case samjho.
"""


# ============================================================
# SOLUTIONS
# ============================================================

def practice_solutions():
    print("\n--- PRACTICE SOLUTIONS ---")

    # Q1
    print(f"Q1 -> 17/5: {17 / 5} | 17//5: {17 // 5} | 17%5: {17 % 5}")

    # Q2
    n = 7.567
    print(f"Q2 -> round: {round(n, 2)} | ceil: {math.ceil(n)} | floor: {math.floor(n)}")

    # Q3
    rand_num = random.randint(1, 100)
    is_even = rand_num % 2 == 0
    print(f"Q3 -> number: {rand_num} | even? {is_even}")

    # Q4
    base, height = 3, 4
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    print(f"Q4 -> hypotenuse: {hypotenuse}")

    # Q5
    n5 = 7
    is_prime = n5 > 1 and all(n5 % i != 0 for i in range(2, n5))
    print(f"Q5 -> is_prime: {is_prime}")

    # Q6
    celsius = 37
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Q6 -> fahrenheit: {fahrenheit}")

    # Q7
    num = 1234
    digit_sum = sum(int(d) for d in str(num))
    print(f"Q7 -> digit sum: {digit_sum}")

    # Q8
    negative_num = -7.8
    print(f"Q8 -> abs: {abs(negative_num)} | round: {round(negative_num)} "
          f"| floor: {math.floor(negative_num)} | ceil: {math.ceil(negative_num)}")


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add python numbers basics-to-medium practice script
