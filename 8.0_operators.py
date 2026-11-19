"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In:
#    Two room types written by hotel staff: "Suite" and "suite".
#    They are the same word, but with different capitalisation.
#
# 2. Process:
#    Compare the two values with the six comparison operators
#    (==, !=, <, >, <=, >=), then combine some of those results
#    with the logical operators and, or, not.
#    Before running, I wrote my prediction for each line in the list "predictions".
#
# 3. Out:
#    A table with one line per expression: the expression, my prediction,
#    the real result, and whether my prediction was right.
#    At the end: how many predictions I got right.
#
# 4. My two values, and the result that surprised me:
#    "Suite" and "suite". I expected Python to see them as the same word,
#    but "Suite" == "suite" is False: Python compares letters exactly.
#    The biggest surprise: "Suite" < "suite" is True.
#    Python compares strings letter by letter using their code numbers:
#    ord("S") is 83 and ord("s") is 115. 83 is smaller, so "Suite" comes first.
#    All capital letters come before all small letters.
#    To compare without caring about capitals, I must use .lower() first.

# Your code below
# The two values I compare
value_a = "Suite"
value_b = "suite"

# Every comparison between the two values
equal = value_a == value_b
not_equal = value_a != value_b
less = value_a < value_b
greater = value_a > value_b
less_or_equal = value_a <= value_b
greater_or_equal = value_a >= value_b

# Logical combinations of the comparison results
both_equal_and_less = equal and less
equal_or_less = equal or less
not_equal_result = not equal
same_word_ignoring_case = value_a.lower() == value_b.lower()

# Each line: the expression as text, and its real result
results = [
    ('"Suite" == "suite"', equal),
    ('"Suite" != "suite"', not_equal),
    ('"Suite" <  "suite"', less),
    ('"Suite" >  "suite"', greater),
    ('"Suite" <= "suite"', less_or_equal),
    ('"Suite" >= "suite"', greater_or_equal),
    ("(==) and (<)", both_equal_and_less),
    ("(==) or (<)", equal_or_less),
    ("not (==)", not_equal_result),
    ("lower() == lower()", same_word_ignoring_case),
]

# My predictions, written BEFORE running, in the same order as the table
predictions = [False, True, False, False, False, False, False, False, True, True]

# Display the table: expression, prediction, real result, right or wrong
print(f"Value A: {value_a!r}   Value B: {value_b!r}")
print(f"ord('S') = {ord('S')}, ord('s') = {ord('s')}")
print()
print(f"{'Expression':<22}{'Predicted':<11}{'Result':<9}Right?")
print("-" * 48)

right_count = 0
for (expression, result), predicted in zip(results, predictions):
    if predicted == result:
        right_count = right_count + 1
        check = "yes"
    else:
        check = "NO"
    print(f"{expression:<22}{str(predicted):<11}{str(result):<9}{check}")

print("-" * 48)
print(f"Predictions right: {right_count}/{len(results)}")

# Output when I ran it:
# Value A: 'Suite'   Value B: 'suite'
# ord('S') = 83, ord('s') = 115
#
# Expression            Predicted  Result   Right?
# ------------------------------------------------
# "Suite" == "suite"    False      False    yes
# "Suite" != "suite"    True       True     yes
# "Suite" <  "suite"    False      True     NO
# "Suite" >  "suite"    False      False    yes
# "Suite" <= "suite"    False      True     NO
# "Suite" >= "suite"    False      False    yes
# (==) and (<)          False      False    yes
# (==) or (<)           False      True     NO
# not (==)              True       True     yes
# lower() == lower()    True       True     yes
# ------------------------------------------------
# Predictions right: 7/10
# My three wrong predictions all come from the same mistake:
# I did not expect a capital letter to be "smaller" than a small letter.