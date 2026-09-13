"""
================================================================================
PYTHON STRINGS - COMPLETE REFERENCE GUIDE
================================================================================
Based on the String Roadmap:
1. Types          : type(), str()
2. Math           : len(), count()
3. Transformations: replace(), +, f{}, split(), *, indexing [0], slicing [1:3]
4. Cleaning       : lstrip(), rstrip(), strip(), lower(), upper()
5. Search         : startswith(), endswith(), find(), 'in'
6. Validation     : isalpha(), isnumeric(), isalnum(), isspace()
================================================================================
"""

# ================================================================================
# 1. TYPES: type(), str()
# ================================================================================
myStr = "Navneet"
print("type(myStr):", type(myStr))  # <class 'str'>

# Converting int to string:
num = 123
myStr2 = str(num)
print("str(123):", myStr2, type(myStr2))  # '123' <class 'str'>

# Note on int() conversion:
numStr = "100"
myInt = int(numStr)  # Works ONLY if string contains numbers!
print("int('100'):", myInt, type(myInt))


# ================================================================================
# 2. MATH: len(), count()
# ================================================================================
sample_text = "banana"
print("len('banana'):", len(sample_text))    # 6
print("count('a'):", sample_text.count("a"))  # 3


# ================================================================================
# 3. TRANSFORMATIONS: replace(), +, f{}, split(), *, indexing [0], slicing [1:3]
# ================================================================================

# A. replace()
print("replace():", "Navneet".replace("Navneet", "Kumar"))

# B. Concatenation (+)
greeting = "H" + "i"
print("Concatenation ('H' + 'i'):", greeting)  # 'Hi'

# C. String Repetition (*)
laughter = "ha" * 3
print("Repetition ('ha' * 3):", laughter)  # 'hahaha'

# D. Formatted String Literals (f-strings)
name_val = "Navneet"
age_val = 27
print(f"f-string: Hello {name_val}, you are {age_val} years old.")

# E. split()
csv_data = "apple,banana,cherry"
print("split(','):", csv_data.split(","))  # ['apple', 'banana', 'cherry']

# F. Extraction (Indexing & Slicing)
cat = "cat"
print("Indexing ('cat'[0]):", cat[0])      # 'c'
print("Slicing ('cat'[1:3]):", cat[1:3])   # 'at'


# ================================================================================
# 4. CLEANING: Clean Whitespaces (lstrip, rstrip, strip) & Clean Cases (lower, upper)
# ================================================================================

# Clean Whitespaces:
raw_user_input = "   navneet@example.com \n "
print("strip():", repr(raw_user_input.strip()))    # 'navneet@example.com'
print("lstrip():", repr("   hello".lstrip()))       # 'hello'
print("rstrip():", repr("hello\n".rstrip()))        # 'hello'

# Clean Cases:
text_case = "Hello Python World"
print("lower():", text_case.lower())  # 'hello python world'
print("upper():", text_case.upper())  # 'HELLO PYTHON WORLD'


# ================================================================================
# 5. SEARCH: startswith(), endswith(), find(), 'in'
# ================================================================================
search_text = "Python Programming Language"

print("'Python' in search_text:", "Python" in search_text)           # True
print("startswith('Python'):", search_text.startswith("Python"))     # True
print("endswith('Language'):", search_text.endswith("Language"))     # True
print("find('Programming'):", search_text.find("Programming"))       # Index: 7
print("find('Java') [missing]:", search_text.find("Java"))           # -1


# ================================================================================
# 6. VALIDATION: isalpha(), isnumeric(), isalnum(), isspace()
# ================================================================================
print("'Navneet'.isalpha():", "Navneet".isalpha())          # True
print("'12345'.isnumeric():", "12345".isnumeric())          # True
print("'User123'.isalnum():", "User123".isalnum())          # True
print("'   '.isspace():", "   ".isspace())                  # True


# ================================================================================
# PRACTICAL EXERCISE SOLUTION (Dynamic String Cleaning)
# Given: "968-Maria, ( D@t@ Engineer );; 27 years  "
# Target: "name : maria | role: data engineer | age: 27"
# ================================================================================
givenString = "968-Maria, ( D@t@ Engineer );; 27 years  "

part1, rest = givenString.split(",", 1)
role_part, age_part = rest.split(";;")

clean_name = part1.split("-")[1].strip().lower()
clean_role = " ".join(role_part.replace("@", "a").replace("(", "").replace(")", "").split()).lower()
clean_age = "".join(c for c in age_part if c.isdigit())

print("\n--- Practical Exercise Output ---")
print(f"name : {clean_name} | role: {clean_role} | age: {clean_age}")
