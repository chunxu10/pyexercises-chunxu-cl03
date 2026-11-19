"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: three values typed by the user for a hotel booking:
#    a booking reference, a mobile phone number and an email address
# 2. Process: clean each value (remove extra spaces), then check its shape
#    with a regular expression. Collect every value that is not acceptable.
# 3. Out: if all three are acceptable, they are saved as one line in
#    10.0_guest_contacts.csv (columns: booking_reference;phone;email).
#    If at least one is not acceptable, the program says which one and saves nothing.
# 4. My three fields and their rules:
#    Booking reference: the letters BK, a hyphen, then exactly 4 digits.
#      Accept: BK-0042. Reject: BK-42 (too few digits), BK0042 (no hyphen).
#      Small letters are accepted: bk-0042 is turned into BK-0042 first.
#    Phone: a French mobile number: exactly 10 digits, starting with 06 or 07.
#      Spaces are removed first, so 06 12 34 56 78 is accepted.
#      Reject: 0112345678 (landline, starts with 01), 061234567 (only 9 digits).
#    Email: some text without spaces, one @, some text, a dot,
#      then at least 2 letters at the end.
#      Accept: chunxu@gmail.com. Reject: chunxu.gmail.com (no @), chunxu@gmail (no dot ending).
#      Borderline case: I do not check if the email really exists,
#      only that it has the right shape.


# Your code below
import csv
import os
import re

# The file where valid contacts are saved
FILE_NAME = "10.0_guest_contacts.csv"

# Booking reference pattern: BK-\d{4}
#   BK     the two letters B and K, exactly
#   -      a hyphen, exactly
#   \d     one digit (0 to 9)
#   {4}    the thing just before must appear exactly 4 times -> 4 digits
REFERENCE_PATTERN = r"BK-\d{4}"

# Phone pattern: 0[67]\d{8}
#   0      the digit 0
#   [67]   ONE character, either 6 or 7 (square brackets = "one of these")
#   \d{8}  exactly 8 more digits -> 1 + 1 + 8 = 10 digits in total
PHONE_PATTERN = r"0[67]\d{8}"

# Email pattern: [^@\s]+@[^@\s]+\.[A-Za-z]{2,}
#   [^@\s]     ONE character that is NOT @ and NOT a space (^ inside [] means "not")
#   +          the thing just before, 1 or more times -> the name part
#   @          the @ sign, exactly
#   [^@\s]+    again: 1 or more characters that are not @ or space -> the domain
#   \.         a real dot (a dot alone means "any character", so \ is needed)
#   [A-Za-z]   ONE letter, small or capital
#   {2,}       the thing just before, 2 or more times -> com, fr, org...
EMAIL_PATTERN = r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}"