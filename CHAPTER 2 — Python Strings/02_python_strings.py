"""
Python Strings — Basic se Medium tak
=====================================
Cover kar rahe hain: string types, math (len/count), transformations,
cleaning, search, aur validation.
Har section ke end mein practice questions hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

# ============================================================
# 1. STRING TYPE KAISE PEHCHANEIN?
# ============================================================
my_str = "Navneet"
print("1. type(my_str):", type(my_str))

num = 123
num_as_str = str(num)
print("   str(123):", num_as_str, "| type:", type(num_as_str).__name__)

# Note: int() sirf tabhi kaam karega jab string mein sirf numbers hon
num_str = "100"
print("   int('100'):", int(num_str))


# ============================================================
# 2. STRING KA MATH (len, count)
# ============================================================
sample_text = "banana"
print("\n2. len('banana'):", len(sample_text))
print("   'banana'.count('a'):", sample_text.count("a"))


# ============================================================
# 3. STRING TRANSFORM KAISE KAREIN?
# ============================================================
print("\n3. Transformations:")
print("   replace():", "Navneet".replace("Navneet", "Kumar"))
print("   concat ('H' + 'i'):", "H" + "i")
print("   repeat ('ha' * 3):", "ha" * 3)

name_val, age_val = "Navneet", 27
print(f"   f-string: Hello {name_val}, {age_val} saal ke ho")

csv_data = "apple,banana,cherry"
print("   split(','):", csv_data.split(","))

cat = "cat"
print("   indexing 'cat'[0]:", cat[0])
print("   slicing 'cat'[1:3]:", cat[1:3])


# ============================================================
# 4. STRING CLEAN KAISE KAREIN?
# ============================================================
raw_input_text = "   navneet@example.com \n "
print("\n4. Cleaning:")
print("   strip():", repr(raw_input_text.strip()))
print("   lstrip():", repr("   hello".lstrip()))
print("   rstrip():", repr("hello\n".rstrip()))

text_case = "Hello Python World"
print("   lower():", text_case.lower())
print("   upper():", text_case.upper())


# ============================================================
# 5. STRING MEIN SEARCH KAISE KAREIN?
# ============================================================
search_text = "Python Programming Language"
print("\n5. Search:")
print("   'Python' in search_text:", "Python" in search_text)
print("   startswith('Python'):", search_text.startswith("Python"))
print("   endswith('Language'):", search_text.endswith("Language"))
print("   find('Programming'):", search_text.find("Programming"))
print("   find('Java') [not found]:", search_text.find("Java"))  # -1 aata hai


# ============================================================
# 6. STRING VALIDATE KAISE KAREIN?
# ============================================================
print("\n6. Validation:")
print("   'Navneet'.isalpha():", "Navneet".isalpha())
print("   '12345'.isnumeric():", "12345".isnumeric())
print("   'User123'.isalnum():", "User123".isalnum())
print("   '   '.isspace():", "   ".isspace())


# ============================================================
# PRACTICE — Basic to Medium
# ============================================================
"""
Q1 (Basic): Ek string "Hello World" ka length nikalo aur usse pura
            uppercase mein print karo.

Q2 (Basic): "python,java,c++,javascript" ko comma se split karo aur
            second language print karo.

Q3 (Medium): "  Navneet@2026  " string ko clean karo — spaces hatao,
             lowercase karo, aur '@' ko 'at' se replace karo.

Q4 (Medium): Diya gaya string: "968-Maria, ( D@t@ Engineer );; 27 years  "
             Isse aise nikalo: "name: maria | role: data engineer | age: 27"
             (Hint: split(",", 1), split(";;"), replace(), isdigit())
"""


# ============================================================
# SOLUTIONS
# ============================================================

def practice_solutions():
    print("\n--- PRACTICE SOLUTIONS ---")

    # Q1
    text_q1 = "Hello World"
    print(f"Q1 -> length: {len(text_q1)} | upper: {text_q1.upper()}")

    # Q2
    langs = "python,java,c++,javascript".split(",")
    print("Q2 -> second language:", langs[1])

    # Q3
    q3_text = "  Navneet@2026  "
    cleaned = q3_text.strip().lower().replace("@", "at")
    print("Q3 -> cleaned:", cleaned)

    # Q4
    given_string = "968-Maria, ( D@t@ Engineer );; 27 years  "
    part1, rest = given_string.split(",", 1)
    role_part, age_part = rest.split(";;")

    clean_name = part1.split("-")[1].strip().lower()
    clean_role = " ".join(role_part.replace("@", "a").replace("(", "").replace(")", "").split()).lower()
    clean_age = "".join(c for c in age_part if c.isdigit())

    print(f"Q4 -> name: {clean_name} | role: {clean_role} | age: {clean_age}")


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add python strings basics-to-medium practice script
