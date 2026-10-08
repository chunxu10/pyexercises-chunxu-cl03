"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answers to a hotel booking confirmation question
# 2. Process: Ask repeatedly, remove surrounding whitespace,
# convert the answer to lowercase, and count the attempts
# 3. Out: A summary showing the number of attempts
# and whether the booking was confirmed
# 4. My stop condition, my attempt limit, my summary:
# Stop when the user enters "yes" or after 3 attempts
# If the limit is reached without "yes", leave the booking unconfirmed
# Accept "Yes", "YES", and " yes " as the same answer
# Any other answer counts as an unsuccessful attempt

# Your code below
# Set the attempt limit and the initial confirmation status.
max_attempts = 3
attempts = 0
confirmed = False

# Keep asking while attempts remain and the booking is not confirmed.
while attempts < max_attempts and not confirmed:
    answer = input("Do you confirm your hotel booking? Enter yes: ")
    attempts += 1

    # Ignore surrounding whitespace and differences in letter case.
    answer = answer.strip().lower()

    # Stop asking once the user confirms.
    if answer == "yes":
        confirmed = True

# After the loop, display the attempt count and final status.
print("Attempts used:", attempts)

if confirmed:
    print("Booking confirmed.")
else:
    print("Attempt limit reached. Booking not confirmed.")


#Do you confirm your hotel booking? Enter yes: no
#Do you confirm your hotel booking? Enter yes: no
#Do you confirm your hotel booking? Enter yes: no
#Attempts used: 3

#Do you confirm your hotel booking? Enter yes:   Yes
#Attempts used: 1
#Booking confirmed.