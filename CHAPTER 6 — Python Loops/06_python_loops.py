"""
Python Loops — Basic se Medium tak
====================================
Cover kar rahe hain: for loop, break/continue/pass, for-else,
nested loops, aur while loop.
Har section ke end mein practice questions hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

# ============================================================
# 1. FOR LOOP KAISE CHALTA HAI?
# ============================================================
print("1. Basic for loop (0 se 4 tak):")
for i in range(5):
    print("  ", i)

print("   range(1, 6) -> 1 se 5 tak:")
for i in range(1, 6):
    print("  ", i)

print("   range(1, 10, 2) -> step 2 ke saath:")
for i in range(1, 10, 2):
    print("  ", i)

print("   range(5, 0, -1) -> reverse:")
for i in range(5, 0, -1):
    print("  ", i)

# String pe bhi loop chala sakte ho
print("   String pe loop:")
for ch in "cat":
    print("  ", ch)


# ============================================================
# 2. BREAK, CONTINUE, PASS KYA KARTE HAIN?
# ============================================================
print("\n2. break -> loop ko turant rok deta hai")
for n in range(10):
    if n == 4:
        break
    print("  ", n)

print("   continue -> is iteration ko skip karke aage badh jata hai")
for n in range(6):
    if n % 2 == 0:
        continue  # even numbers skip
    print("  ", n)

print("   pass -> kuch nahi karta, sirf placeholder hai")
for n in range(3):
    if n == 1:
        pass  # baad mein logic likhenge
    print("  ", n)


# ============================================================
# 3. FOR-ELSE KYA HOTA HAI?
# ============================================================
# else block tabhi chalta hai jab loop 'break' na hua ho.
print("\n3. for-else (bina break):")
for n in range(3):
    print("  ", n)
else:
    print("   Loop pura chala, koi break nahi hua!")

print("   for-else (search example — number dhoondo):")
numbers = [4, 8, 15, 16, 23, 42]
target = 15
for n in numbers:
    if n == target:
        print(f"   {target} mil gaya!")
        break
else:
    print(f"   {target} nahi mila.")


# ============================================================
# 4. NESTED LOOPS KAISE KAAM KARTE HAIN?
# ============================================================
print("\n4. Nested loop — star triangle:")
for row in range(1, 4):
    for _ in range(row):
        print("*", end="")
    print()  # naya line

print("   Nested loop — number pattern:")
for row in range(1, 4):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()


# ============================================================
# 5. WHILE LOOP KAISE CHALTA HAI?
# ============================================================
print("\n5. while loop (0 se 4 tak):")
count = 0
while count < 5:
    print("  ", count)
    count += 1  # yeh line miss mat karna, warna infinite loop ho jayega!

print("   while loop with break:")
count = 0
while True:
    if count == 3:
        break
    print("  ", count)
    count += 1


# ============================================================
# 6. FOR vs WHILE — KAB KONSA USE KAREIN?
# ============================================================
print("\n6. for -> jab pata ho kitni baar repeat karna hai (fixed sequence)")
print("   while -> jab tak ek condition True hai, tab tak chalate raho")


# ============================================================
# PRACTICE — Basic to Medium
# ============================================================
"""
Q1 (Basic): 1 se 10 tak sirf even numbers print karo (for loop + continue,
            ya range step 2).

Q2 (Basic): while loop use karke 5 se 1 tak countdown print karo, aur end
            mein "Liftoff!" print karo.

Q3 (Medium): Ek list of numbers diya hai. for-else use karke check karo
             ki usme koi negative number hai ya nahi.

Q4 (Medium): Nested loop use karke ek multiplication table print karo
             (1 se 3 tak, 1 se 3 tak) format: "1 x 1 = 1".

Q5 (Basic): n = 5. for loop use karke n ka factorial nikalo (5! = 120).

Q6 (Basic-Medium): while loop use karke 1 se 10 tak numbers ka sum
                    nikalo (bina sum() built-in ke).

Q7 (Medium): rows = 4. Nested loop use karke ek right-angled triangle
             banao stars se:
                 *
                 **
                 ***
                 ****

Q8 (Medium): numbers = [4, 2, 7, 2, 9, 4]. Nested loop use karke pehla
             duplicate value dhoondo (jo pehle bhi list mein aa chuka
             ho) aur usse print karo.
"""


# ============================================================
# SOLUTIONS
# ============================================================

def practice_solutions():
    print("\n--- PRACTICE SOLUTIONS ---")

    # Q1
    print("Q1 ->", end=" ")
    for n in range(1, 11):
        if n % 2 != 0:
            continue
        print(n, end=" ")
    print()

    # Q2
    print("Q2 ->")
    count = 5
    while count >= 1:
        print("  ", count)
        count -= 1
    print("   Liftoff!")

    # Q3
    nums_q3 = [4, 8, 15, 16, 23, 42]
    print("Q3 ->", end=" ")
    for n in nums_q3:
        if n < 0:
            print("Negative number mila!")
            break
    else:
        print("Koi negative number nahi hai.")

    # Q4
    print("Q4 ->")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"   {i} x {j} = {i * j}")

    # Q5
    n5 = 5
    factorial = 1
    for i in range(1, n5 + 1):
        factorial *= i
    print(f"Q5 -> {n5}! = {factorial}")

    # Q6
    total = 0
    i = 1
    while i <= 10:
        total += i
        i += 1
    print("Q6 -> sum 1 to 10:", total)

    # Q7
    print("Q7 ->")
    rows = 4
    for i in range(1, rows + 1):
        print("  " + "*" * i)

    # Q8
    numbers_q8 = [4, 2, 7, 2, 9, 4]
    seen = []
    first_duplicate = None
    for n in numbers_q8:
        if n in seen:
            first_duplicate = n
            break
        seen.append(n)
    print("Q8 -> first duplicate:", first_duplicate)


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add python loops basics-to-medium practice script
