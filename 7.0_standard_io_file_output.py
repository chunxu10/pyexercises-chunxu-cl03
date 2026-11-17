"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: The guest's name, check-in date, number of nights and room type.
# 2. Process: 
# Ask for each value and check whether it is acceptable.
# If a value is invalid, explain why and ask the user to enter it again.
# Create the CSV with a header if it does not exist or is empty.
# Append the booking without overwriting previous entries.
# What counts as invalid:
# - guest name: empty, or contains anything other than letters, spaces and hyphens
# - check-in date: not in the DD/MM/YYYY format, day not 1-31 or month not 1-12
#   (it does not check that the day exists in that month, so 31/02/2026 is accepted)
# - nights: not a whole number, or less than 1
# - room type: not single, double or suite (upper or lower case is accepted)
# 3. Out, file name and columns:
# File: hotel_bookings.csv
# Columns: guest_name;check_in_date;nights;room_type

# 4. Why these columns, and what this file is for: 
# These columns identify the guest, arrival date, length of stay
# and requested room type.
# With 200 bookings, I could calculate the total and average nights,
# compare demand for different room types and identify busy arrival dates.
# This would help me decide when to add staff, which rooms to promote,
# and whether to offer a weekly rate for long stays.



# Your code below
import os

FILE_NAME = "hotel_bookings.csv"
HEADER = "guest_name;check_in_date;nights;room_type\n"
ROOM_TYPES = ["single", "double", "suite"]


def is_valid_name(text):
    letters_only = text.replace(" ", "").replace("-", "")
    return letters_only != "" and letters_only.isalpha()


def is_valid_date(text):
    if len(text) != 10 or text[2] != "/" or text[5] != "/":
        return False
    day = text[0:2]
    month = text[3:5]
    year = text[6:10]
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    return 1 <= int(day) <= 31 and 1 <= int(month) <= 12


def is_valid_nights(text):
    return text.isdigit() and int(text) >= 1


def ask_guest_name():
    while True:
        name = input("Guest name: ").strip()
        if is_valid_name(name):
            return name
        print("  Not accepted: use letters, spaces or hyphens only, and do not leave it empty.")


def ask_check_in_date():
    while True:
        date = input("Check-in date (DD/MM/YYYY): ").strip()
        if is_valid_date(date):
            return date
        print("  Not accepted: write the date as DD/MM/YYYY, for example 05/12/2026.")


def ask_nights():
    while True:
        nights = input("Number of nights: ").strip()
        if is_valid_nights(nights):
            return nights
        print("  Not accepted: type a whole number of nights, 1 or more.")


def ask_room_type():
    while True:
        room = input("Room type (single, double, suite): ").strip().lower()
        if room in ROOM_TYPES:
            return room
        print("  Not accepted: choose single, double or suite.")


def file_needs_header(file_name):
    return not os.path.exists(file_name) or os.path.getsize(file_name) == 0


print("Please fill in the booking details:")
guest_name = ask_guest_name()
check_in_date = ask_check_in_date()
nights = ask_nights()
room_type = ask_room_type()

needs_header = file_needs_header(FILE_NAME)

with open(FILE_NAME, "a") as file:
    if needs_header:
        file.write(HEADER)
    file.write(guest_name + ";" + check_in_date + ";" + nights + ";" + room_type + "\n")

print("Booking saved to " + FILE_NAME)

# Check: I ran the program three times with different bookings.
# In run 2 I left the name empty: it was refused and asked again.
# In run 3 I typed "zero" and 0 for nights, and "family" for the room type:
# each was refused and asked again.
# hotel_bookings.csv then had 4 lines: exactly one header line and three bookings.