"""
================================================================================
CHAPTER 5: PYTHON CONDITIONAL STATEMENTS & EMAIL VALIDATION
================================================================================
Topics Covered:
1. if, elif, else
2. Nested if statements
3. Guard Clauses (Flat if-elif-else)
4. Ternary Operator (One-line if-else)
5. Match-Case (Python 3.10+)
6. Regex Validation (import re)

Email Rules to Validate:
1. Email must not be empty
2. Email must contain both '.' and '@'
3. Email must contain exactly one '@' symbol
4. Email must end with and contain exactly one '.com', '.org', or '.net'
5. Email must not be longer than 254 characters
6. Email must start and end with a letter or digit (isalnum)
================================================================================
"""

import re

emailAddress = "navneetanand17360@gmail.com"


# ================================================================================
# APPROACH 1: Nested if Statements (Fixed & Corrected)
# ================================================================================
print("--- Approach 1: Nested if ---")

if emailAddress and len(emailAddress) > 0:
    if '.' in emailAddress and '@' in emailAddress:
        if emailAddress.count('@') == 1:
            if (emailAddress.count('.com') + emailAddress.count('.org') + emailAddress.count('.net')) == 1 and emailAddress.endswith(('.com', '.org', '.net')):
                if len(emailAddress) <= 254:
                    if emailAddress[0].isalnum() and emailAddress[-1].isalnum():
                        print("valid")
                    else:
                        print("invalid: Must start and end with a letter or digit")
                else:
                    print("invalid: Exceeds 254 characters")
            else:
                print("invalid: Must contain exactly one valid extension (.com, .org, .net)")
        else:
            print("invalid: Must contain exactly one '@' symbol")
    else:
        print("invalid: Must contain both '.' and '@'")
else:
    print("invalid: Email cannot be empty")


# ================================================================================
# APPROACH 2: Guard Clauses with if-elif-else (Clean & Recommended)
# ================================================================================
print("\n--- Approach 2: Guard Clauses (if-elif-else) ---")

valid_extensions_count = (
    emailAddress.count('.com') + emailAddress.count('.org') + emailAddress.count('.net')
)

if not emailAddress:
    print("invalid: Email cannot be empty")
elif '.' not in emailAddress or '@' not in emailAddress:
    print("invalid: Missing '.' or '@'")
elif emailAddress.count('@') != 1:
    print("invalid: Must contain exactly one '@'")
elif valid_extensions_count != 1 or not emailAddress.endswith(('.com', '.org', '.net')):
    print("invalid: Must contain exactly one extension (.com, .org, .net)")
elif len(emailAddress) > 254:
    print("invalid: Exceeds 254 characters")
elif not (emailAddress[0].isalnum() and emailAddress[-1].isalnum()):
    print("invalid: First and last characters must be alphanumeric")
else:
    print("valid")


# ================================================================================
# APPROACH 3: Regular Expressions (Regex - Professional Standard)
# ================================================================================
print("\n--- Approach 3: Regex (re.match) ---")

# Regex breakdown:
# ^[a-zA-Z0-9]        -> Starts with letter or digit
# [a-zA-Z0-9._%+-]*   -> Allowed characters before '@'
# @                   -> Exactly one '@' symbol
# [a-zA-Z0-9.-]+      -> Domain name
# \.(com|org|net)$    -> Ends with .com, .org, or .net
pattern = r"^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.(com|org|net)$"

if len(emailAddress) <= 254 and re.match(pattern, emailAddress):
    print("valid")
else:
    print("invalid")


# ================================================================================
# BONUS 1: Ternary Operator (One-line if-else)
# Syntax: value_if_true if condition else value_if_false
# ================================================================================
print("\n--- Bonus 1: Ternary Operator ---")

is_valid_email = True if (emailAddress.count('@') == 1 and emailAddress.endswith(('.com', '.org', '.net'))) else False
print("Is valid email?:", is_valid_email)


# ================================================================================
# BONUS 2: Match-Case Statement (Python 3.10+)
# ================================================================================
print("\n--- Bonus 2: Match-Case ---")

status_code = 200

match status_code:
    case 200:
        print("Success: Email processed successfully")
    case 400:
        print("Error: Bad Request - Invalid Email Format")
    case 404:
        print("Error: Email domain not found")
    case _:
        print("Unknown Status Code")