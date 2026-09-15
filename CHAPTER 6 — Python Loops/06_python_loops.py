"""
============================================================
CHAPTER 6 — PYTHON LOOPS
============================================================

Topics:
1. For Loops
2. Break, Continue, Pass
3. For-Else & Nested Loops
4. While Loops

Beginner Friendly Revision
============================================================
"""


# ============================================================
# 1. FOR LOOP
# ============================================================

"""
A for loop is used when we want to repeat
something multiple times.

Basic syntax:

for variable in sequence:
    code
"""


# Example 1
for i in range(5):
    print(i)

"""
Output:
0
1
2
3
4

Remember:
range(5) starts from 0
and stops BEFORE 5.
"""


# Example 2
for i in range(1, 6):
    print(i)

"""
Output:
1
2
3
4
5
"""


# Example 3 — step
for i in range(1, 10, 2):
    print(i)

"""
Output:
1
3
5
7
9
"""


# Example 4 — reverse
for i in range(5, 0, -1):
    print(i)

"""
Output:
5
4
3
2
1
"""


# ============================================================
# 2. FOR LOOP WITH A STRING
# ============================================================

word = "Python"

for character in word:
    print(character)


"""
Each character is processed one by one.
"""


# ============================================================
# 3. SIMPLE TABLE USING FOR LOOP
# ============================================================

n = 7

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# ============================================================
# 4. BREAK
# ============================================================

"""
break = completely stop the loop.
"""

for i in range(1, 10):

    if i == 5:
        break

    print(i)

"""
Output:
1
2
3
4

As soon as i becomes 5,
the loop stops.
"""


# ============================================================
# 5. BREAK — SIMPLE EXAMPLE
# ============================================================

for i in range(10):

    if i == 3:
        break

    print("Running:", i)


"""
break is useful when we have found
what we were looking for and don't
need to continue.
"""


# ============================================================
# 6. CONTINUE
# ============================================================

"""
continue = skip the current iteration
and move to the next iteration.
"""

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

"""
Output:
1
2
4
5

Only 3 was skipped.
The loop did NOT stop.
"""


# ============================================================
# 7. CONTINUE — EVEN NUMBERS
# ============================================================

for i in range(1, 11):

    if i % 2 != 0:
        continue

    print(i)

"""
Output:
2
4
6
8
10
"""


# ============================================================
# 8. PASS
# ============================================================

"""
pass = do nothing.

It is mainly used as a placeholder
when we want to write the code later.
"""

for i in range(5):

    if i == 2:
        pass

    print(i)


"""
pass does NOT:
    - stop the loop
    - skip the iteration

It simply does nothing.
"""


# ============================================================
# 9. BREAK vs CONTINUE vs PASS
# ============================================================

"""
break
-----
Stops the entire loop.


continue
--------
Skips the current iteration.


pass
----
Does nothing.


Easy way to remember:

break    -> STOP
continue -> SKIP
pass     -> DO NOTHING
"""


# ============================================================
# 10. FOR-ELSE
# ============================================================

"""
A for loop can have an else block.

The else runs when the loop finishes
WITHOUT using break.
"""

for i in range(5):
    print(i)

else:
    print("Loop finished")


# ============================================================
# 11. FOR-ELSE WITH BREAK
# ============================================================

for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("Loop finished")


"""
Here "Loop finished" is NOT printed.

Why?

Because break was used.

Important:

for-else:

NO break -> else runs
break     -> else does not run
"""


# ============================================================
# 12. FOR-ELSE — SEARCH EXAMPLE
# ============================================================

numbers = [10, 20, 30, 40]

target = 30

for number in numbers:

    if number == target:
        print("Found")
        break

else:
    print("Not Found")


"""
If target is not found,
the loop finishes normally,
so else runs.
"""


# ============================================================
# 13. NESTED LOOPS
# ============================================================

"""
A loop inside another loop
is called a nested loop.

Example:

for i:
    for j:
        ...
"""


for i in range(3):

    for j in range(3):

        print(i, j)


"""
Outer loop:
0
1
2

For EACH outer loop,
inner loop runs 3 times.
"""


# ============================================================
# 14. NESTED LOOP — SIMPLE PATTERN
# ============================================================

for i in range(1, 4):

    for j in range(1, 4):

        print("*", end=" ")

    print()


"""
Output:

* * *
* * *
* * *
"""


# ============================================================
# 15. NESTED LOOP — STAR TRIANGLE
# ============================================================

for i in range(1, 6):

    for j in range(i):

        print("*", end="")

    print()


"""
Output:

*
**
***
****
*****
"""


# ============================================================
# 16. NESTED LOOP — NUMBER PATTERN
# ============================================================

for i in range(1, 6):

    for j in range(i):

        print(i, end="")

    print()


"""
Output:

1
22
333
4444
55555
"""


# ============================================================
# 17. BREAK IN NESTED LOOP
# ============================================================

"""
If break is inside the inner loop,
it stops ONLY the inner loop.
"""

for i in range(3):

    for j in range(5):

        if j == 2:
            break

        print(i, j)


"""
The outer loop continues.

Remember:

break affects the loop in which
it is written.
"""


# ============================================================
# 18. WHILE LOOP
# ============================================================

"""
A while loop runs as long as
the condition is True.

Syntax:

while condition:
    code
"""


# Example
i = 1

while i <= 5:

    print(i)

    i += 1


"""
Output:
1
2
3
4
5
"""


# ============================================================
# 19. WHY i += 1 IS IMPORTANT
# ============================================================

i = 1

while i <= 5:

    print(i)

    i += 1


"""
Every time the loop runs,
i increases.

Eventually:

i <= 5

becomes False.

Then the loop stops.
"""


# ============================================================
# 20. INFINITE LOOP — IMPORTANT
# ============================================================

"""
Be careful:

i = 1

while i <= 5:
    print(i)

Here i never changes.

So i will ALWAYS be 1.

The condition will always be True.

This creates an infinite loop.

Correct:

i = 1

while i <= 5:
    print(i)
    i += 1
"""


# ============================================================
# 21. WHILE LOOP — REVERSE
# ============================================================

i = 5

while i >= 1:

    print(i)

    i -= 1


"""
Output:

5
4
3
2
1
"""


# ============================================================
# 22. WHILE LOOP WITH BREAK
# ============================================================

i = 1

while i <= 10:

    if i == 5:
        break

    print(i)

    i += 1


"""
Output:

1
2
3
4
"""


# ============================================================
# 23. WHILE LOOP WITH CONTINUE
# ============================================================

i = 0

while i < 5:

    i += 1

    if i == 3:
        continue

    print(i)


"""
Output:

1
2
4
5
"""


# ============================================================
# 24. FOR LOOP vs WHILE LOOP
# ============================================================

"""
FOR LOOP
--------

Use when you are going through
a known sequence or range.

Example:

for i in range(5):
    print(i)


WHILE LOOP
----------

Use when the loop should continue
while a condition is True.

Example:

while i < 5:
    print(i)
    i += 1


Simple rule:

FOR   -> repeat over a range/sequence
WHILE -> repeat while a condition is True
"""


# ============================================================
# 25. BEGINNER PRACTICE QUESTIONS
# ============================================================

"""
Try these yourself BEFORE checking the answers.

Q1.
Print numbers from 1 to 10.

Q2.
Print numbers from 10 to 1.

Q3.
Print even numbers from 1 to 20.

Q4.
Print odd numbers from 1 to 20.

Q5.
Print the table of 7.

Q6.
Print each character of "Python".

Q7.
Use break to stop a loop when
the number reaches 5.

Q8.
Use continue to skip number 5.

Q9.
Print this pattern:

*
**
***
****
*****

Q10.
Print this pattern:

*****
****
***
**
*

Q11.
Use for-else to search for 30
in a sequence.

Q12.
Use a while loop to print
1 to 5.

Q13.
Use a while loop to print
5 to 1.

Q14.
Use nested loops to print:

***
***
***

Q15.
Explain in your own words:

break
continue
pass
"""


# ============================================================
# 26. QUICK REVISION
# ============================================================

"""
FOR LOOP
--------

for i in range(5):
    print(i)


BREAK
-----

Stops the loop completely.


CONTINUE
--------

Skips current iteration.


PASS
----

Does nothing.


FOR-ELSE
--------

else runs if the for loop
finishes without break.


NESTED LOOP
-----------

Loop inside another loop.


WHILE LOOP
----------

Runs while the condition is True.


INFINITE LOOP
-------------

Happens when the while condition
never becomes False.


============================================================
MOST IMPORTANT REMEMBER
============================================================

break    = STOP
continue = SKIP
pass     = DO NOTHING

for      = iterate/repeat over a sequence or range
while    = repeat while condition is True

for-else:
    break nahi hua -> else runs

nested loop:
    loop ke andar loop
============================================================
"""
