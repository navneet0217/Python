"""
================================================================================
CHAPTER 5: PYTHON CONDITIONAL STATEMENTS - COMPLETE REFERENCE GUIDE
================================================================================
Sequential Concept Breakdown:
1. Basic Control Flow   : if, elif, else
2. Nested if Statements : Hierarchical decision trees
3. Guard Clauses        : Flat early-exit validation (if-elif-else)
4. Ternary Operator     : One-line if-else expressions
5. Match-Case           : Structural pattern matching (Python 3.10+)
6. Regex Validation     : Pattern matching using import re
7. Practical Project 1  : Email Validation Challenge
8. Practical Project 2  : Password Quality & Correctness Validation Challenge
================================================================================
"""

import re

# ================================================================================
# 1. BASIC CONTROL FLOW: if, elif, else
# ================================================================================
print("=== 1. Basic Control Flow (if, elif, else) ===")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")


# ================================================================================
# 2. NESTED IF STATEMENTS (Hierarchical Checks)
# ================================================================================
print("\n=== 2. Nested if Statements ===")

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Access Granted: Welcome to the event!")
    else:
        print("Access Denied: Ticket required.")
else:
    print("Access Denied: Underage.")


# ================================================================================
# 3. GUARD CLAUSES / FLAT IF-ELIF-ELSE (Early Exits)
# ================================================================================
print("\n=== 3. Guard Clauses (Flat if-elif-else) ===")

user_role = "editor"
account_active = True

if not account_active:
    print("Denied: Account suspended.")
elif user_role == "admin":
    print("Granted: Full Admin Access.")
elif user_role == "editor":
    print("Granted: Editor Content Access.")
else:
    print("Granted: Standard Viewer Access.")


# ================================================================================
# 4. TERNARY OPERATOR (One-line if-else)
# Syntax: value_if_true if condition else value_if_false
# ================================================================================
print("\n=== 4. Ternary Operator ===")

age_check = 20
status = "Adult" if age_check >= 18 else "Minor"
print(f"Age {age_check}: {status}")


# ================================================================================
# 5. MATCH-CASE STATEMENT (Python 3.10+ Pattern Matching)
# ================================================================================
print("\n=== 5. Match-Case Statement ===")

http_status = 200

match http_status:
    case 200:
        response = "200 OK: Success"
    case 400:
        response = "400 Bad Request"
    case 404:
        response = "404 Not Found"
    case 500:
        response = "500 Internal Server Error"
    case _:
        response = "Unknown Status Code"

print("HTTP Response:", response)


# ================================================================================
# 6. REGEX VALIDATION (import re)
# ================================================================================
print("\n=== 6. Regex Validation (re.match) ===")

zip_code = "90210"
is_valid_zip = bool(re.match(r"^\d{5}$", zip_code))
print(f"Zip '{zip_code}' Valid?:", is_valid_zip)


# ================================================================================
# 7. PRACTICAL CHALLENGE 1: EMAIL VALIDATION
# Rules:
# 1. Must not be empty
# 2. Must contain both '.' and '@'
# 3. Must contain exactly one '@'
# 4. Must contain exactly one '.com', '.org', or '.net' and end with it
# 5. Must not be longer than 254 chars
# 6. Must start and end with alphanumeric character
# ================================================================================
print("\n=== 7. Practical Challenge 1: Email Validation ===")

email = "navneetanand17360@gmail.com"

ext_count = email.count('.com') + email.count('.org') + email.count('.net')

if not email:
    email_result = "invalid: Email cannot be empty"
elif '.' not in email or '@' not in email:
    email_result = "invalid: Missing '.' or '@'"
elif email.count('@') != 1:
    email_result = "invalid: Must contain exactly one '@'"
elif ext_count != 1 or not email.endswith(('.com', '.org', '.net')):
    email_result = "invalid: Must contain exactly one valid extension"
elif len(email) > 254:
    email_result = "invalid: Exceeds 254 characters"
elif not (email[0].isalnum() and email[-1].isalnum()):
    email_result = "invalid: First and last chars must be alphanumeric"
else:
    email_result = "valid"

print(f"Email '{email}' -> {email_result}")


# ================================================================================
# 8. PRACTICAL CHALLENGE 2: PASSWORD QUALITY & CORRECTNESS VALIDATION
# Rules:
# 1. Must not be empty
# 2. Must be at least 8 characters
# 3. Must include at least 1 uppercase letter
# 4. Must include at least 1 lowercase letter
# 5. Must not be same as the email
# 6. Must not contain any spaces
# 7. Must start and end with a letter or digit
# ================================================================================
print("\n=== 8. Practical Challenge 2: Password Validation ===")

sample_password = "Abd@17360"
sample_email = "navneetanand17360@gmail.com"

if not sample_password:
    pwd_result = "invalid: Password cannot be empty"
elif len(sample_password) < 8:
    pwd_result = "invalid: Password must be at least 8 characters"
elif sample_password.lower() == sample_password:
    pwd_result = "invalid: Must contain at least 1 uppercase letter"
elif sample_password.upper() == sample_password:
    pwd_result = "invalid: Must contain at least 1 lowercase letter"
elif sample_password == sample_email:
    pwd_result = "invalid: Password cannot be the same as email"
elif " " in sample_password:
    pwd_result = "invalid: Password must not contain spaces"
elif not (sample_password[0].isalnum() and sample_password[-1].isalnum()):
    pwd_result = "invalid: Must start and end with a letter or digit"
else:
    pwd_result = "valid"

print(f"Password '{sample_password}' -> {pwd_result}")

