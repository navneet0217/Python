"""
Python Logic & Operators — Basic se Medium tak
================================================
Cover kar rahe hain: boolean values, boolean functions (bool/any/all),
comparison operators, logical operators, membership operators,
aur identity operators.
Har section ke end mein practice questions hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

# ============================================================
# 1. BOOLEAN VALUES KYA HOTE HAIN?
# ============================================================
is_python_fun = True
is_earth_flat = False

print("1. Boolean values:")
print("   is_python_fun:", is_python_fun, "->", type(is_python_fun).__name__)
print("   is_earth_flat:", is_earth_flat)


# ============================================================
# 2. BOOLEAN FUNCTIONS (bool, any, all, isinstance)
# ============================================================
print("\n2. Boolean functions:")
# Falsy values Python mein: 0, 0.0, "", [], {}, None, False
print("   bool(1):", bool(1))
print("   bool(0):", bool(0), "(0 falsy hota hai)")
print("   bool('Hello'):", bool("Hello"))
print("   bool(''):", bool(""), "(empty string bhi falsy hai)")

# any() -> kam se kam ek True ho to True
print("   any([False, True, False]):", any([False, True, False]))
# all() -> sab True hone chahiye
print("   all([True, False, True]):", all([True, False, True]))

print("   isinstance(True, bool):", isinstance(True, bool))


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================
x, y = 10, 20
print("\n3. Comparison (x=10, y=20):")
print("   x == y:", x == y)
print("   x != y:", x != y)
print("   x < y :", x < y)
print("   x > y :", x > y)
print("   x >= 10:", x >= 10)
print("   y <= 20:", y <= 20)


# ============================================================
# 4. LOGICAL OPERATORS (and, or, not)
# ============================================================
age, has_license = 25, True
print("\n4. Logical operators:")

can_drive = (age >= 18) and has_license
print("   and -> can_drive:", can_drive)

is_student, is_senior = False, True
gets_discount = is_student or is_senior
print("   or  -> gets_discount:", gets_discount)

is_logged_in = False
print("   not -> not is_logged_in:", not is_logged_in)


# ============================================================
# 5. MEMBERSHIP OPERATORS (in, not in)
# ============================================================
fruits = ["apple", "banana", "cherry"]
print("\n5. Membership:")
print("   'banana' in fruits:", "banana" in fruits)
print("   'mango' not in fruits:", "mango" not in fruits)


# ============================================================
# 6. IDENTITY OPERATORS (is, is not)
# ============================================================
# '==' value compare karta hai, 'is' memory location compare karta hai.
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a  # same object

print("\n6. Identity:")
print("   list_a == list_b (same values):", list_a == list_b)
print("   list_a is list_b (same memory):", list_a is list_b)
print("   list_a is list_c (same memory):", list_a is list_c)


# ============================================================
# PRACTICE — Basic to Medium
# ============================================================
"""
Q1 (Basic): username = "abc", age = 17. Check karo ki username khali
            nahi hai AUR age >= 18 hai ya nahi.

Q2 (Basic-Medium): password = "Abd@17360". Check karo ki password kam se
                    kam 8 characters ka hai AUR usme koi space nahi hai.

Q3 (Medium): email = "navneet@gmail.com". Check karo ki email khali nahi
             hai, usme '@' hai, aur woh '.com' pe end hota hai.

Q4 (Medium): userRole = "moderator", is_banned = True,
             is_verified_email = True. Check karo ki user admin ya
             moderator hai AUR (banned nahi hai YA email verified hai).
"""


# ============================================================
# SOLUTIONS
# ============================================================

def practice_solutions():
    print("\n--- PRACTICE SOLUTIONS ---")

    # Q1
    username, user_age = "abc", 17
    print("Q1 ->", bool(username) and user_age >= 18)

    # Q2
    password = "Abd@17360"
    print("Q2 ->", len(password) >= 8 and " " not in password)

    # Q3
    user_email = "navneet@gmail.com"
    print("Q3 ->", bool(user_email) and "@" in user_email and user_email.endswith(".com"))

    # Q4
    user_role, is_banned, is_verified_email = "moderator", True, True
    result = (user_role in ("admin", "moderator")) and (not is_banned or is_verified_email)
    print("Q4 ->", result)


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add python logic and operators basics-to-medium practice script
