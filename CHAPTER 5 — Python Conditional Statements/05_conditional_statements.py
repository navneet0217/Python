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

Q5 (Basic): n = 15. FizzBuzz karo — agar 3 aur 5 dono se divide ho to
            "FizzBuzz", sirf 3 se to "Fizz", sirf 5 se to "Buzz", warna
            number khud print karo.

Q6 (Basic-Medium): year = 2024. Check karo leap year hai ya nahi.
                    (Rule: 4 se divisible ho, lekin 100 se divisible ho
                    to 400 se bhi divisible hona chahiye.)

Q7 (Medium): day_num = 3. match-case use karke 1-7 ko weekday name mein
             convert karo (1=Monday...7=Sunday), aur invalid number
             (jaise 9) ke liye "Invalid day" bhi handle karo.

Q8 (Medium): mobile = "9876543210". Regex se validate karo ki yeh ek
             valid 10-digit Indian mobile number hai — 6, 7, 8, ya 9 se
             start hona chahiye aur exactly 10 digits hone chahiye.
             (Hint: r"^[6-9]\\d{9}$")
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

    # Q5
    n = 15
    if n % 3 == 0 and n % 5 == 0:
        fizzbuzz_result = "FizzBuzz"
    elif n % 3 == 0:
        fizzbuzz_result = "Fizz"
    elif n % 5 == 0:
        fizzbuzz_result = "Buzz"
    else:
        fizzbuzz_result = str(n)
    print("Q5 ->", fizzbuzz_result)

    # Q6
    year = 2024
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    print("Q6 -> leap year?", is_leap)

    # Q7
    for day_num in (3, 9):
        match day_num:
            case 1:
                day_name = "Monday"
            case 2:
                day_name = "Tuesday"
            case 3:
                day_name = "Wednesday"
            case 4:
                day_name = "Thursday"
            case 5:
                day_name = "Friday"
            case 6:
                day_name = "Saturday"
            case 7:
                day_name = "Sunday"
            case _:
                day_name = "Invalid day"
        print(f"Q7 -> day {day_num}:", day_name)

    # Q8
    mobile = "9876543210"
    is_valid_mobile = bool(re.match(r"^[6-9]\d{9}$", mobile))
    print("Q8 -> valid mobile?", is_valid_mobile)


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add python conditional statements basics-to-medium practice script
