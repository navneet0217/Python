"""
List/Array Concepts — Basic se Medium tak
==========================================
Cover kar rahe hain: Create, Access/Read, Unpack, Explore/Analyze (Min/Max),
aur Change (Update, Append, Remove).
Har section ke end mein practice questions bhi hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

# ============================================================
# 1. HOW TO CREATE?
# ============================================================
# List banane ka sabse simple tarika — square brackets.

my_list = ["a", "b", "c"]
print("1. Created list:", my_list)

# Alternate ways to create
empty_list = []
using_list_func = list(("x", "y", "z"))       # from a tuple
numbers = list(range(1, 6))                    # [1, 2, 3, 4, 5]
repeated = [0] * 5                              # [0, 0, 0, 0, 0]

print("   empty_list      :", empty_list)
print("   using_list_func :", using_list_func)
print("   numbers         :", numbers)
print("   repeated        :", repeated)


# ============================================================
# 2. HOW TO ACCESS & READ?
# ============================================================
# Index se access karo — 0 se start hota hai (index-0 based).

print("\n2. Access & Read:")
print("   my_list[0] (first) :", my_list[0])   # a
print("   my_list[1] (mid)   :", my_list[1])   # b
print("   my_list[2] (last)  :", my_list[2])   # c
print("   my_list[-1] (last, negative index):", my_list[-1])

# Slicing — ek range access karna
print("   my_list[0:2] (slice):", my_list[0:2])


# ============================================================
# 3. HOW TO UNPACK?
# ============================================================
# List ke elements ko seedha variables mein daal sakte ho.

first, middle, last = my_list
print("\n3. Unpacked ->", "First:", first, "| Middle:", middle, "| Last:", last)

# Agar list badi ho to * (star) use karo baaki values collect karne ke liye
nums = [10, 20, 30, 40, 50]
head, *rest = nums
print("   head:", head, "| rest:", rest)


# ============================================================
# 4. HOW TO EXPLORE & ANALYZE? (Max / Min)
# ============================================================
scores = [3, 1, 2, 7]

print("\n4. Explore & Analyze:")
print("   scores       :", scores)
print("   max(scores)  :", max(scores))
print("   min(scores)  :", min(scores))
print("   len(scores)  :", len(scores))
print("   sum(scores)  :", sum(scores))
print("   sorted asc   :", sorted(scores))
print("   sorted desc  :", sorted(scores, reverse=True))

# "Bad" case jaisa image mein tha — empty list pe max/min lagane se error aata hai
try:
    max([])
except ValueError as e:
    print("   max([]) error ->", e)


# ============================================================
# 5. HOW TO CHANGE? (Update / Append / Remove)
# ============================================================
letters = ["a", "b", "c", "d"]
print("\n5. Change (before):", letters)

# UPDATE — kisi index ki value badalna
letters[0] = "e"
print("   after update (index 0 -> 'e'):", letters)

# APPEND — end mein naya element daalna
letters.append("d_new")
print("   after append('d_new'):", letters)

# REMOVE — kisi element ya index ko hatana
letters.remove("b")          # value se remove
print("   after remove('b'):", letters)

del letters[0]                # index se remove
print("   after del index 0:", letters)

popped = letters.pop()        # last element hatao aur return bhi karo
print("   after pop() ->", "removed:", popped, "| list:", letters)

# Bonus: insert — kisi bhi position pe daal sakte ho
letters.insert(1, "z")
print("   after insert(1, 'z'):", letters)


# ============================================================
# PRACTICE — Basic to Medium
# ============================================================
"""
Q1 (Basic): Ek list banao 5 fruits ki. Print karo second aur last fruit.

Q2 (Basic): Ek list [5, 10, 15, 20, 25] ko unpack karo first, middle values,
            aur last mein — first variable, ek "rest" list, aur last variable
            mein (hint: first, *rest, last = ...).

Q3 (Medium): Ek list of numbers do. Bina max()/min() built-in use kiye,
             khud loop likh kar largest aur smallest number nikalo.

Q4 (Medium): Ek list ["apple", "banana", "cherry"] mein "banana" ko
             "blueberry" se update karo, phir "date" ko end mein append
             karo, phir "apple" ko remove karo. Final list print karo.

Q5 (Medium): Ek list of numbers do. Ek naya list banao jisme sirf woh
             numbers ho jo average se bade hain (list comprehension use
             karne ki koshish karo).

Q6 (Basic): letters = ['p', 'y', 't', 'h', 'o', 'n']. Ise reverse() built-in
            use kiye bina reverse karo (slicing [::-1] ya loop use karo).

Q7 (Medium): list1 = [1, 2, 3], list2 = [3, 4, 5]. Dono ko merge karo aur
             duplicate values hata do (hint: set() use karo, phir wapas
             list mein convert karo).

Q8 (Medium): nested = [[1, 2], [3, 4], [5, 6]]. Ise flatten karke ek
             single list bana do: [1, 2, 3, 4, 5, 6] (nested loop ya
             list comprehension use karo).
"""


# ============================================================
# SOLUTIONS (practice khatam karne ke baad hi dekho!)
# ============================================================

def practice_solutions():
    print("\n--- PRACTICE SOLUTIONS ---")

    # Q1
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Q1 -> second:", fruits[1], "| last:", fruits[-1])

    # Q2
    q2_list = [5, 10, 15, 20, 25]
    first_val, *rest_vals, last_val = q2_list
    print("Q2 -> first:", first_val, "| rest:", rest_vals, "| last:", last_val)

    # Q3
    nums_q3 = [12, 45, 3, 89, 21]
    largest = nums_q3[0]
    smallest = nums_q3[0]
    for n in nums_q3:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    print("Q3 -> largest:", largest, "| smallest:", smallest)

    # Q4
    q4_list = ["apple", "banana", "cherry"]
    q4_list[1] = "blueberry"
    q4_list.append("date")
    q4_list.remove("apple")
    print("Q4 -> final list:", q4_list)

    # Q5
    nums_q5 = [4, 8, 15, 16, 23, 42]
    avg = sum(nums_q5) / len(nums_q5)
    above_avg = [n for n in nums_q5 if n > avg]
    print("Q5 -> average:", avg, "| above average:", above_avg)

    # Q6
    letters = ["p", "y", "t", "h", "o", "n"]
    print("Q6 -> reversed:", letters[::-1])

    # Q7
    list1, list2 = [1, 2, 3], [3, 4, 5]
    merged_unique = list(set(list1 + list2))
    print("Q7 -> merged unique:", sorted(merged_unique))

    # Q8
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = [item for sub_list in nested for item in sub_list]
    print("Q8 -> flattened:", flattened)


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add list basics-to-medium practice script (create, access, unpack, analyze, change)
