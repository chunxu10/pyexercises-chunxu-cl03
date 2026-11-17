"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of numbers, where each number is the nights stayed in one hotel booking
# (for example [1, 7, 8, 6, 2, 3, 4, 5]).
# 2. Process: add up all the nights, then divide by the number of bookings in the list.
# 3. Out: the average number of nights per booking, returned as a float (e.g. 4.5).
# 4. My function name, and why return rather than print:
# The function is called average_nights_per_booking. The name says exactly what
# comes out (an average), of what (nights), and per what (per booking), so a
# reader does not need to open the code to know what it does.
# I use return instead of print because return hands the value back to the caller,
# so it can be stored in a variable, compared, or used in another calculation.
# A function that only prints shows the number on screen but gives back None.
# When I replaced return with print and tried average * 2, Python raised
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'.
# Printing is for people to read; returning is for the rest of the program to use.

# Your code below

def average_nights_per_booking(nights):
    if len(nights) == 0:
        return None
    total = sum(nights)
    return total / len(nights)


booking_nights = [1, 7, 8, 6, 2, 3, 4, 5]

# Three calls with different inputs (checked by hand first)
# By hand: (1+7+8+6+2+3+4+5) / 8 = 36 / 8 = 4.5
print("All bookings:", average_nights_per_booking(booking_nights))
# By hand: (1+2+3) / 3 = 6 / 3 = 2.0
print("Short stays:", average_nights_per_booking([1, 2, 3]))
# By hand: (7+8+6) / 3 = 21 / 3 = 7.0
print("Long stays:", average_nights_per_booking([7, 8, 6]))
# Test: the program printed 4.5, 2.0 and 7.0, matching my hand calculations.

# Using the returned value in another calculation
average = average_nights_per_booking(booking_nights)
print("Twice the average stay:", average * 2)

# Empty list check
print("No bookings:", average_nights_per_booking([]))
# Before I added the check, calling the function with [] crashed with
# ZeroDivisionError: division by zero, because len([]) is 0.
# That is not acceptable: one empty list should not stop the whole program.
# Returning 0 would also be wrong, because it would say "the average stay is
# 0 nights", which is false; there are simply no bookings to average.
# So the function now returns None, which means "no answer" rather than a wrong answer.
# Whoever calls the function must check for None before doing maths with the result.