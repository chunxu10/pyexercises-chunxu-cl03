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
# 1. In:
#    Three values entered by a hotel guest: a booking reference,
#    a French mobile phone number, and an email address.
#
# 2. Process:
#    Remove leading and trailing whitespace from all three values.
#    Convert the booking reference to uppercase.
#    Remove ordinary spaces inside the phone number.
#    Check each cleaned value against its regular expression.
#    Save one record only when all three values pass.
#
# 3. Out:
#    Valid records are appended to 10.0_guest_contacts.csv.
#    Columns: booking_reference;phone;email.
#    Invalid records produce error messages and are not saved.
#
# 4. My fields and acceptance rules:
#    Booking reference:
#      BK, a hyphen, and exactly four ASCII digits from 0 to 9.
#      Lowercase letters are accepted after conversion to uppercase.
#      Pass: bk-0042. Fail: BK-42 and BK0042.
#
#    Phone:
#      Exactly ten ASCII digits, starting with 06 or 07.
#      Ordinary spaces are removed before checking.
#      Pass: 06 12 34 56 78.
#      Fail: 0112345678 and 061234567.
#      Borderline: +33612345678 is rejected because this program
#      accepts the national format only.
#
#    Email:
#      A nonempty part without whitespace or @, exactly one @,
#      a nonempty domain part without whitespace or @, a dot,
#      and at least two ASCII letters at the end.
#      Pass: chunxu@gmail.com.
#      Fail: chunxu.gmail.com and chunxu@gmail.
#      This is a simple shape check, not a complete email standard.
#      It does not prove that the address exists.
#
# Self-check:
#    Run: python 10.0_regular_expressions.py --test
#    There are nine cases: one accepted and two rejected per field.
#    The test command does not create or change the CSV file.
#    Expected result: 9/9 tests passed.
#    After running, record any unexpected result here in your own words.
#
#    Surprise: a@b..com is accepted, although it is not a real email.
#    The domain part [^@\s]+ also accepts dots, so "b." counts as the domain.
#    I keep it, because my rule only checks the general shape of an email.


# Your code below
import csv
import re
import sys
from pathlib import Path


# BK matches the literal letters B and K.
# - matches a literal hyphen.
# [0-9] matches one ASCII digit; {4} requires exactly four.
REFERENCE_PATTERN = r"BK-[0-9]{4}"

# 0 matches the initial zero.
# [67] accepts either 6 or 7.
# [0-9]{8} requires eight more ASCII digits, making ten in total.
PHONE_PATTERN = r"0[67][0-9]{8}"

# [^@\s]+ requires one or more characters that are neither @ nor whitespace.
# @ matches the single separator between the local part and the domain.
# The second [^@\s]+ requires a nonempty domain part.
# \. matches a literal dot.
# [A-Za-z]{2,} requires at least two ASCII letters at the end.
EMAIL_PATTERN = r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}"


def validate_contact(reference, phone, email):
    # Normalize the inputs according to the rules stated above.
    contact = {
        "booking_reference": reference.strip().upper(),
        "phone": phone.strip().replace(" ", ""),
        "email": email.strip(),
    }

    # Associate each chosen field with its pattern and error message.
    rules = [
        (
            "booking_reference",
            REFERENCE_PATTERN,
            "Booking reference must be BK- followed by exactly four digits.",
        ),
        (
            "phone",
            PHONE_PATTERN,
            "Phone must contain ten digits and start with 06 or 07.",
        ),
        (
            "email",
            EMAIL_PATTERN,
            "Email must contain one @ and a dot followed by at least two letters.",
        ),
    ]

    # Check the whole value and collect every validation error.
    errors = []
    for field, pattern, message in rules:
        if re.fullmatch(pattern, contact[field]) is None:
            errors.append(message)

    # Return the cleaned record and the errors so the caller can decide what to do.
    return contact, errors


def save_contact(file_path, contact):
    # A missing or empty output file needs a header.
    needs_header = not file_path.exists() or file_path.stat().st_size == 0
    columns = ["booking_reference", "phone", "email"]

    # Append one record without overwriting earlier bookings.
    with file_path.open("a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=columns,
            delimiter=";",
        )
        if needs_header:
            writer.writeheader()
        writer.writerow(contact)


def run_tests():
    # Use valid defaults so each case changes only the field being tested.
    valid_contact = {
        "reference": "BK-0042",
        "phone": "0612345678",
        "email": "chunxu@gmail.com",
    }

    # Test one acceptable value and two unacceptable values for each field.
    tests = [
        ("reference", "bk-0042", True),
        ("reference", "BK-42", False),
        ("reference", "BK0042", False),
        ("phone", "06 12 34 56 78", True),
        ("phone", "0112345678", False),
        ("phone", "061234567", False),
        ("email", "chunxu@gmail.com", True),
        ("email", "chunxu.gmail.com", False),
        ("email", "chunxu@gmail", False),
    ]

    # Compare each actual result with its expected result.
    passed = 0
    for field, value, expected in tests:
        inputs = valid_contact.copy()
        inputs[field] = value
        _, errors = validate_contact(**inputs)
        accepted = not errors

        if accepted == expected:
            passed += 1
            status = "PASS"
        else:
            status = "FAIL"

        print(
            f"{status}: {field} = {value!r}; "
            f"expected accepted={expected}, actual accepted={accepted}"
        )

    # Report the total and return an exit code for the test command.
    print(f"\n{passed}/{len(tests)} tests passed.")
    return 0 if passed == len(tests) else 1


def main():
    # Collect the three pieces of information from the user.
    reference = input("Booking reference, for example BK-0042: ")
    phone = input("French mobile phone number: ")
    email = input("Email address: ")

    # Reject the entire record if any field fails validation.
    contact, errors = validate_contact(reference, phone, email)
    if errors:
        print("\nNothing was saved. Please correct these problems:")
        for message in errors:
            print(f"- {message}")
        return

    # Save valid contacts beside this Python script and report file errors.
    file_path = Path(__file__).with_name("10.0_guest_contacts.csv")
    try:
        save_contact(file_path, contact)
    except OSError as error:
        print(f"Could not save the contact: {error}")
        return

    print(f"\nContact saved to {file_path.name}.")


# Run the nine checks with --test; otherwise start interactive data collection.
if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        sys.exit(run_tests())
    main()