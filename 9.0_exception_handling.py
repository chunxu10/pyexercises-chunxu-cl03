"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    The number of nights of a hotel booking, typed by the user.
#    The total price of the booking is fixed in the program: 360.00 euros.
#
# 2. Process:
#    Convert the text to a whole number, then divide the total price by it
#    to get the price per night. If the value is not acceptable, explain why
#    and ask again. The user has at most 3 attempts.
#
# 3. Out:
#    The price per night, with 2 decimals, for example "120.00 euros".
#    Or, after 3 unacceptable values, a message saying that the program
#    stops without a result. The program never crashes.
#
# 4. The two failures, and whether they deserve the same message:
#    Failure 1, ValueError: the text is not a whole number ("abc", "2.5").
#      This is a typing mistake. Message: type digits only, for example 3.
#    Failure 2, ZeroDivisionError: the text IS a number, but it is 0.
#      This is not a typing mistake: the number is correct, but the
#      calculation makes no sense, because a booking cannot have 0 nights.
#      Message: a booking needs at least 1 night.
#    They must NOT have the same message: they have different causes,
#    so the user needs different advice to fix them.
#    (Same idea as the exam: a campaign with 0 conversions has no CPA.)
#
#    My other decisions:
#    - An empty line gets its own message ("you did not type anything"),
#      checked with an if before the conversion.
#    - A negative number is converted without error, but it is not a real
#      number of nights, so it is refused with an if.
#    - At most 3 attempts. After that the program stops politely,
#      so it can never ask for ever.
#
# Why catch each failure separately, not every error at once:
#    With "except Exception:" every problem gets the same vague message,
#    so the user does not know what to fix. Worse, it also hides real bugs
#    in MY code (for example a misspelled variable name, NameError):
#    the program would say "invalid number" while the real problem is a bug.
#    Catching ValueError and ZeroDivisionError separately gives the right
#    advice for each case, and any other unexpected error still appears.


# Your code below
# The total price of the booking, and how many tries the user gets
TOTAL_PRICE = 360.0
MAX_ATTEMPTS = 3


def price_per_night(total_price, nights):
    """Return the price of one night. Raises ZeroDivisionError if nights is 0."""
    return total_price / nights


attempts = 0
result_found = False

# Keep asking until the value is acceptable or the attempts are used up
while attempts < MAX_ATTEMPTS and not result_found:
    attempts = attempts + 1
    try:
        text = input(f"Number of nights (attempt {attempts}/{MAX_ATTEMPTS}): ").strip()
    except EOFError:
        # Ctrl+D (or the end of the input): nothing more can be read, so stop politely
        print()
        break

    # Empty line: nothing to convert, so explain it before trying
    if text == "":
        print("You did not type anything. Please type a number of nights, for example 3.")
        continue

    try:
        # int() raises ValueError if the text is not a whole number
        nights = int(text)
        # The division raises ZeroDivisionError if nights is 0
        price = price_per_night(TOTAL_PRICE, nights)
    except ValueError:
        print(f'"{text}" is not a whole number. Please type digits only, for example 3.')
        continue
    except ZeroDivisionError:
        print("A booking cannot have 0 nights, so there is no price per night. Please type 1 or more.")
        continue

    # A negative number is a valid int, but not a real number of nights
    if nights < 0:
        print("The number of nights cannot be negative. Please type 1 or more.")
        continue

    print(f"Total price: {TOTAL_PRICE:.2f} euros for {nights} nights")
    print(f"Price per night: {price:.2f} euros")
    result_found = True

# No acceptable value (attempts used up, or no more input): stop politely, no crash
if not result_found:
    print("No valid number of nights. The program stops without a result.")

# CHECK IT YOURSELF: four runs, four behaviours
# Run 1, normal number "3":
#    Total price: 360.00 euros for 3 nights
#    Price per night: 120.00 euros
#    -> the result is shown and the program ends.
# Run 2, zero "0":
#    A booking cannot have 0 nights, so there is no price per night. Please type 1 or more.
#    -> ZeroDivisionError is caught, the program asks again (attempt 2/3).
# Run 3, the word "abc":
#    "abc" is not a whole number. Please type digits only, for example 3.
#    -> ValueError is caught, the program asks again (attempt 2/3).
# Run 4, an empty line (just Enter):
#    You did not type anything. Please type a number of nights, for example 3.
#    -> the if catches it before int(), the program asks again (attempt 2/3).
# Extra run, three bad values in a row (0, abc, Enter):
#    No valid number of nights. The program stops without a result.
#    -> the program stops by itself, it does not ask for ever.
# None of these runs stopped the program with an error.