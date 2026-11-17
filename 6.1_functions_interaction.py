"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the same list as in exercise 4.0 and 6.0: the number of nights for each
# hotel booking, e.g. [1, 7, 8, 6, 2, 3, 4, 5], plus the minimum number of nights
# that counts as a "long stay" (7 nights, i.e. one week or more).
# 2. Process, function by function:
# - count_bookings returns how many bookings are in the list.
# - count_long_stays returns how many bookings last at least min_nights nights.
# - calculate_percentage returns what percentage one number is of another.
# - percentage_of_long_stays calls count_long_stays, then count_bookings, then
# calculate_percentage on those two results.
# 3. Out: the percentage of bookings that are long stays, as a float (e.g. 25.0),
# or None if there are no bookings at all.
# 4. The question my fourth function answers:
# "What percentage of our bookings are long stays of 7 nights or more?"
# If this share is high, the hotel could offer a weekly rate.
# Splitting it into three makes it easier to check because each small function
# can be tested on its own with a tiny input I can work out by hand. If the final
# percentage is wrong, I can see which of the three steps is wrong (the count of
# long stays, the total count, or the percentage maths) instead of searching
# through one big function.


# Your code below
def count_bookings(nights):
    return len(nights)


def count_long_stays(nights, min_nights):
    count = 0
    for stay in nights:
        if stay >= min_nights:
            count = count + 1
    return count


def calculate_percentage(part, whole):
    if whole == 0:
        return None
    return part / whole * 100


def percentage_of_long_stays(nights, min_nights):
    long_stays = count_long_stays(nights, min_nights)
    total_bookings = count_bookings(nights)
    return calculate_percentage(long_stays, total_bookings)


# Test each small function on its own first
# Test 1: count_bookings([1, 7, 8])  -> expected 3 (three bookings in the list)
print("Test 1 count_bookings:", count_bookings([1, 7, 8]))
# Test 2: count_long_stays([1, 7, 8], 7)  -> expected 2 (7 and 8 are at least 7)
print("Test 2 count_long_stays:", count_long_stays([1, 7, 8], 7))
# Test 3: calculate_percentage(2, 8)  -> expected 25.0 (2 / 8 = 0.25, x 100 = 25)
print("Test 3 calculate_percentage:", calculate_percentage(2, 8))
# Result: the program printed 3, 2 and 25.0, matching all three expected outputs.

# Now combine them to answer the question
booking_nights = [1, 7, 8, 6, 2, 3, 4, 5]

# By hand: long stays are 7 and 8 -> 2 out of 8 bookings -> 2 / 8 * 100 = 25.0
print("Long stays (7+ nights) as % of all bookings:",
      percentage_of_long_stays(booking_nights, 7))

# Empty list: calculate_percentage returns None instead of dividing by zero
print("Long stays with no bookings:", percentage_of_long_stays([], 7))