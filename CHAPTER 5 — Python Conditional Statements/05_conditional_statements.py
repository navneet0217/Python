"""
Python Conditional Statements — Basic se Medium tak
=====================================================
Cover kar rahe hain: if-elif-else, nested if, guard clauses,
ternary operator, match-case, aur regex validation.
Har section ke end mein practice questions hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

import re

# ============================================================
# 1. if-elif-else KAISE KAAM KARTA HAI?
# ============================================================
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"1. Score {score} -> Grade {grade}")


# ============================================================
# 2. NESTED if KAISE LIKHEIN?
# ============================================================
age, has_ticket = 20, True
print("\n2. Nested if:")

if age >= 18:
    if has_ticket:
        print("   Access Granted: Welcome!")
    else:
        print("   Access Denied: Ticket chahiye.")
else:
    print("   Access Denied: Underage.")


# ============================================================
# 3. GUARD CLAUSES (FLAT if-elif-else) KYA HOTE HAIN?
# ============================================================
# Nested if ki jagah, sab conditions ko ek hi level pe check karna —
# padhne mein aasan hota hai.
user_role, account_active = "editor", True
print("\n3. Guard clauses:")

if not account_active:
    print("   Denied: Account suspended.")
elif user_role == "admin":
    print("   Granted: Full Admin Access.")
elif user_role == "editor":
    print("   Granted: Editor Access.")
else:
    print("   Granted: Standard Viewer Access.")


# ============================================================
# 4. TERNARY OPERATOR (One-line if-else)
# ============================================================
# Syntax: value_if_true if condition else value_if_false
age_check = 20
status = "Adult" if age_check >= 18 else "Minor"
print(f"\n4. Ternary -> Age {age_check}: {status}")


# ============================================================
# 5. MATCH-CASE KAISE USE KAREIN? (Python 3.10+)
# ============================================================
http_status = 200
print("\n5. Match-case:")

match http_status:
    case 200:
        response = "200 OK"
    case 400:
        response = "400 Bad Request"
    case 404:
        response = "404 Not Found"
    case _:
        response = "Unknown status"

print("   HTTP response:", response)


# ============================================================
# 6. REGEX SE VALIDATION KAISE KAREIN?
# ============================================================
zip_code = "90210"
is_valid_zip = bool(re.match(r"^\d{5}$", zip_code))
print(f"\n6. Zip '{zip_code}' valid? {is_valid_zip}")


# ============================================================
# PRACTICE — Basic to Medium
# ============================================================
"""
Q1 (Basic): marks = 45. Grade decide karo: >=90 "A", >=75 "B", >=50 "C",
            baaki "Fail".

Q2 (Basic-Medium): temperature = 40. Ternary operator use karke print
                    karo "Hot" agar >= 35, nahi to "Normal".

Q3 (Medium): Email Validation — email = "navneetanand@gmail.com".
             Rules: khali nahi ho, exactly ek '@' ho, aur '.com'/'.org'/
             '.net' pe end ho. "valid" ya reason batao invalid ka.

Q4 (Medium): Password Validation — password = "Abcd@1234".
             Rules: min 8 chars, kam se kam 1 uppercase, kam se kam
             1 lowercase, aur koi space na ho.
"""


# ============================================================
# SOLUTIONS
# ============================================================

def practice_solutions():
    print("\n--- PRACTICE SOLUTIONS ---")

    # Q1
    marks = 45
    if marks >= 90:
        result_grade = "A"
    elif marks >= 75:
        result_grade = "B"
    elif marks >= 50:
        result_grade = "C"
    else:
        result_grade = "Fail"
    print("Q1 ->", result_grade)

    # Q2
    temperature = 40
    weather = "Hot" if temperature >= 35 else "Normal"
    print("Q2 ->", weather)

    # Q3
    email = "navneetanand@gmail.com"
    if not email:
        email_result = "invalid: Email khali nahi ho sakta"
    elif email.count("@") != 1:
        email_result = "invalid: Exactly ek '@' hona chahiye"
    elif not email.endswith((".com", ".org", ".net")):
        email_result = "invalid: '.com' / '.org' / '.net' pe end hona chahiye"
    else:
        email_result = "valid"
    print("Q3 ->", email_result)

    # Q4
    password = "Abcd@1234"
    if len(password) < 8:
        pwd_result = "invalid: kam se kam 8 characters"
    elif password.lower() == password:
        pwd_result = "invalid: kam se kam 1 uppercase chahiye"
    elif password.upper() == password:
        pwd_result = "invalid: kam se kam 1 lowercase chahiye"
    elif " " in password:
        pwd_result = "invalid: space nahi hona chahiye"
    else:
        pwd_result = "valid"
    print("Q4 ->", pwd_result)


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add python conditional statements basics-to-medium practice script
