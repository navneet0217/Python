"""
List/Array Concepts — Basic se Medium tak
==========================================
Cover kar rahe hain: Create, Access/Read, Unpack, Explore/Analyze (Min/Max),
Change (Update, Append, Remove), Sort, Copy (reference vs shallow vs deep),
aur Combine (+, extend, zip).
Har section ke end mein practice questions bhi hain — pehle khud try karo,
phir SOLUTIONS section dekho.
"""

# ============================================================
# 1. HOW TO CREATE?
# ============================================================
# List banane ka sabse simple tarika — square brackets.

import copy
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
print("\n3. Unpacked ->", "First:", first,
      "| Middle:", middle, "| Last:", last)

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
# 6. HOW TO SORT?
# ============================================================
# sorted() -> NAYI list return karta hai, original untouched rehta hai.
# .sort()  -> ORIGINAL list ko khud modify karta hai, kuch return nahi karta.

lst = [4, 3, 1, 2]
sorted_list = sorted(lst)                 # naya list, ascending
sorted_desc = sorted(lst, reverse=True)   # naya list, descending

print("\n6. Sort:")
print("   original lst      :", lst, "(sorted() ke baad bhi same hai)")
print("   sorted(lst)       :", sorted_list)
print("   sorted(reverse=T) :", sorted_desc)

# .sort() -> in-place, original list hi badal jati hai
lst_inplace = [4, 3, 1, 2]
lst_inplace.sort()
print("   lst.sort() (in-place):", lst_inplace)

# reversed() -> ek iterator deta hai, list() laga kar list banao
rev_list = list(reversed(sorted_list))
print("   list(reversed(sorted_list)):", rev_list)


# ============================================================
# 7. HOW TO COPY? (Reference vs Shallow vs Deep)
# ============================================================

print("\n7. Copy:")

# '=' sirf REFERENCE copy karta hai — dono naam SAME list ko point karte hain.
original = [1, 2, 3]
same_reference = original
same_reference.append(4)
print("   after same_reference.append(4):")
print("   original       :", original, "(yeh bhi badal gaya!)")
print("   same_reference :", same_reference)
print("   original is same_reference:", original is same_reference)

# .copy() (ya copy.copy()) -> SHALLOW copy, naya outer list banta hai
original2 = [1, 2, 3]
shallow = original2.copy()
shallow.append(99)
print("\n   after shallow.append(99):")
print("   original2 :", original2, "(safe rehta hai, badla nahi)")
print("   shallow   :", shallow)
print("   original2 is shallow:", original2 is shallow)

# Shallow copy ka trap — NESTED lists ke andar wahi reference share hoti hai
nested_original = [[1, 2], [3, 4]]
nested_shallow = nested_original.copy()
nested_shallow[0].append(999)  # inner list dono mein shared hai
print("\n   Shallow copy trap (nested list):")
print("   nested_original:", nested_original, "(inner list bhi badal gaya!)")
print("   nested_shallow :", nested_shallow)

# copy.deepcopy() -> pura naya copy, andar ke nested objects bhi alag
nested_original2 = [[1, 2], [3, 4]]
nested_deep = copy.deepcopy(nested_original2)
nested_deep[0].append(999)
print("\n   copy.deepcopy() (nested list):")
print("   nested_original2:", nested_original2, "(safe — bilkul nahi badla)")
print("   nested_deep     :", nested_deep)


# ============================================================
# 8. HOW TO COMBINE?
# ============================================================
print("\n8. Combine:")

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# '+' operator -> naya list return karta hai (original untouched)
combined_plus = list_a + list_b
print("   list_a + list_b     :", combined_plus)

# extend() -> IN-PLACE, list_a khud badal jata hai
list_a_copy = [1, 2, 3]
list_a_copy.extend(list_b)
print("   list_a.extend(list_b):", list_a_copy)

# zip() -> dono lists ko pair-pair mein jodta hai, tuples ka iterator deta hai
names = ["Navneet", "Riya", "Aman"]
scores = [88, 92, 79]
zipped = list(zip(names, scores))  # list() lagana zaroori hai dekhne ke liye
print("   list(zip(names, scores)):", zipped)

# zip alag-alag length ki lists pe shortest ke hisaab se ruk jata hai
short_list = [1, 2]
long_list = ["a", "b", "c", "d"]
print("   zip with unequal lengths:", list(zip(short_list, long_list)))


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

Q9 (Basic): prices = [299, 99, 450, 150]. Bina original list ko chhede
            (sorted() use karke) ascending order mein sorted list banao,
            phir usi se reversed() use karke descending list bhi banao.

Q10 (Basic-Medium): list_x = [1, 2, 3]. list_y = list_x likh kar
                     list_y.append(4) karo. Check karo ki list_x pe
                     bhi effect pada ya nahi, aur `is` operator se
                     confirm karo ki dono same object hain kya.
                     (Fix bhi likho: list_y = list_x.copy() use karke.)

Q11 (Medium): matrix = [[1, 2], [3, 4]]. Ek shallow copy (.copy()) aur
              ek deep copy (copy.deepcopy()) banao. Dono copies ke
              pehle inner list mein ek value change karo aur dekho
              original matrix pe kya effect padta hai — farak samjho.

Q12 (Medium): student_names = ["Aman", "Riya", "Kabir"],
              student_marks = [78, 91, 65]. zip() use karke dono ko
              jodo aur ek dictionary jaisa output print karo:
              "Aman: 78", "Riya: 91", "Kabir: 65" (ek loop mein).
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

    # Q9
    prices = [299, 99, 450, 150]
    ascending = sorted(prices)
    descending = list(reversed(ascending))
    print("Q9 -> original:", prices, "| ascending:",
          ascending, "| descending:", descending)

    # Q10
    list_x = [1, 2, 3]
    list_y = list_x
    list_y.append(4)
    print("Q10 -> list_x:", list_x, "| list_y:",
          list_y, "| same object?", list_x is list_y)
    # Fix: alag list chahiye to .copy() use karo
    list_x_fixed = [1, 2, 3]
    list_y_fixed = list_x_fixed.copy()
    list_y_fixed.append(4)
    print("       fixed -> list_x_fixed:",
          list_x_fixed, "| list_y_fixed:", list_y_fixed)

    # Q11
    matrix = [[1, 2], [3, 4]]
    matrix_shallow = matrix.copy()
    matrix_deep = copy.deepcopy(matrix)
    matrix_shallow[0].append(100)
    matrix_deep[0].append(200)
    print("Q11 -> original matrix:", matrix,
          "(shallow copy ke change se affect hua)")
    print("       matrix_shallow :", matrix_shallow)
    print("       matrix_deep    :", matrix_deep,
          "(original par koi asar nahi)")

    # Q12
    student_names = ["Aman", "Riya", "Kabir"]
    student_marks = [78, 91, 65]
    print("Q12 ->")
    for name, marks in zip(student_names, student_marks):
        print(f"   {name}: {marks}")


if __name__ == "__main__":
    practice_solutions()


# ============================================================
# Suggested commit message
# ============================================================
# feat: add list basics-to-medium practice script (create, access, unpack, analyze, change, sort, copy, combine)
