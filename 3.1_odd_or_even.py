"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: An integer N entered by the user.
# 2. Process: Check whether each number from 1 to N is odd or even.
# 3. Out: Each number from 1 to N labelled as odd or even, or a message if N is outside the allowed range.
# 4. What happens on 0, on a negative number, on a very large number:
# If N is 0 or negative, display "Please enter a positive integer."
# If N is greater than 100, display "Please enter a number no greater than 100."


# Your code below
# Ask the user for an integer
N = int(input("Enter an integer from 1 to 100: "))
# Display a message if the number is zero or negative.
if N <= 0:
    print("please enter a positive integer")

# Display a message if the number is above the chosen limit
elif N > 100:
    print("please enter a number no greater than 100")

# for valid input, check every number from 1 to N, including N.
else:
    for number in range(1, N + 1):
        #  A remainder of zero means the number is even
        if number % 2 == 0:
            print (number, "is even")
        else:
            print(number,"is odd")