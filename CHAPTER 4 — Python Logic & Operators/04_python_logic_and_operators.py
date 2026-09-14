# """
# ================================================================================
# CHAPTER 4: PYTHON LOGIC & OPERATORS - COMPLETE REFERENCE GUIDE
# ================================================================================
# Based on the Boolean Expressions Concept Map:
# 1. Values               : True, False
# 2. Functions            : bool(), any(), all(), isinstance()
# 3. Comparison Operators : ==, !=, <, >, >=, <=
# 4. Logical Operators    : and, or, not
# 5. Membership Operators : in, not in
# 6. Identity Operators   : is, is not
# ================================================================================
# """

# # ================================================================================
# # 1. BOOLEAN VALUES: True, False
# # ================================================================================
# is_python_fun = True
# is_earth_flat = False

# print("is_python_fun:", is_python_fun, "| Type:", type(is_python_fun))
# print("is_earth_flat:", is_earth_flat, "| Type:", type(is_earth_flat))


# # ================================================================================
# # 2. BOOLEAN FUNCTIONS: bool(), any(), all(), isinstance()
# # ================================================================================

# # bool() -> Evaluates truthiness of any value
# # Falsy values in Python: 0, 0.0, "", [], {}, None, False
# print("\n--- bool() Examples ---")
# print("bool(1):", bool(1))              # True
# print("bool(0):", bool(0))              # False (0 is falsy)
# print("bool('Hello'):", bool("Hello"))  # True
# print("bool(''):", bool(""))            # False (empty string is falsy)

# # any() -> Returns True if AT LEAST ONE element in an iterable is True
# print("\n--- any() Examples ---")
# print("any([False, True, False]):", any([False, True, False]))  # True
# print("any([0, '', None]):", any([0, "", None]))                 # False

# # all() -> Returns True if ALL elements in an iterable are True
# print("\n--- all() Examples ---")
# print("all([True, True, True]):", all([True, True, True]))      # True
# print("all([True, False, True]):", all([True, False, True]))    # False

# # isinstance() -> Checks if an object belongs to a specific class/type
# print("\n--- isinstance() Examples ---")
# print("isinstance(True, bool):", isinstance(True, bool))        # True
# print("isinstance(10, int):", isinstance(10, int))              # True


# # ================================================================================
# # 3. COMPARISON OPERATORS: ==, !=, <, >, >=, <=
# # ================================================================================
# print("\n--- Comparison Operators ---")
# x, y = 10, 20

# print("x == y (Equal to):", x == y)            # False
# print("x != y (Not equal to):", x != y)        # True
# print("x < y  (Less than):", x < y)            # True
# print("x > y  (Greater than):", x > y)         # False
# print("x >= 10 (Greater or equal):", x >= 10)  # True
# print("y <= 20 (Less or equal):", y <= 20)     # True


# # ================================================================================
# # 4. LOGICAL OPERATORS: and, or, not
# # ================================================================================
# print("\n--- Logical Operators ---")
# age = 25
# has_license = True

# # and -> Both conditions must be True
# can_drive = (age >= 18) and has_license
# print("can_drive (and):", can_drive)  # True

# # or -> At least one condition must be True
# is_student = False
# is_senior = True
# gets_discount = is_student or is_senior
# print("gets_discount (or):", gets_discount)  # True

# # not -> Negates / flips the boolean value
# is_logged_in = False
# print("not is_logged_in:", not is_logged_in)  # True


# # ================================================================================
# # 5. MEMBERSHIP OPERATORS: in, not in
# # ================================================================================
# print("\n--- Membership Operators ---")
# fruits = ["apple", "banana", "cherry"]

# print("'banana' in fruits:", "banana" in fruits)         # True
# print("'mango' not in fruits:", "mango" not in fruits)   # True


# # ================================================================================
# # 6. IDENTITY OPERATORS: is, is not
# # ================================================================================
# print("\n--- Identity Operators ---")
# # 'is' checks if two variables point to the EXACT SAME memory location.
# # '==' checks if two variables have equal VALUES.

# list_a = [1, 2, 3]
# list_b = [1, 2, 3]
# list_c = list_a  # Points to the exact same list in memory

# print("list_a == list_b (Equal values):", list_a == list_b)   # True
# print("list_a is list_b (Same memory):", list_a is list_b)     # False (different objects)
# print("list_a is list_c (Same memory):", list_a is list_c)     # True

# print("list_a is not list_b:", list_a is not list_b)           # True


# 1.check if username is not empty and age is greater than or equal to 18
userName = "abc"
age = 17
print(userName and age >= 18)  # Fixed: 'userName' checks not empty (instead of 'not userName')


# 2.check password is atleast 8 char long and does not contain spaces
password = "Abd@17360"
# print(password.isspace())

print(len(password) >= 8 and " " not in password)


# 3.check if user email is not empty , contains @ and ends with .com
userEmail = "navneet@gmail.com"
print(userEmail and '@' in userEmail and userEmail.endswith('.com'))


# 4 check if username is a string,not none and and is longer than 5 characters
userName = "navneet@17360"
print(isinstance(userName, str) and userName is not None and len(userName) > 5)


# 5 check if the user is admin or moderator and either they are not banned  or they have verified their email
userRole = "moderator"
is_banned = True
is_verified_email = True

print((userRole == "admin" or userRole == "moderator")
      and (not is_banned or is_verified_email))


