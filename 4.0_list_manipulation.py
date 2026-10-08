"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list containing the number of nights for eight hotel bookings
# 2. Process: Select one item, sort the list, and calculate the total nights
# 3. Out: The whole list, the first item, the sorted list, and the total nights
# 4. What my list is about, and what I computed from it: 
# I calculated the total number of nights booked.
# This total helps the hotel understand the volume of booked stays


# Your code below
# the number of nights for eight sample hotel bookings. use []
booking_nights = [1, 7, 8, 6, 2, 3, 4, 5]
# display the whole list
print("all booking nights", booking_nights)
# display the number of nights for the first booking
print("first booking", booking_nights[0])
# Display the nights in ascending order without changing the original list
print("Sorted booking nights:", sorted(booking_nights))
# Calculate and display the total number of nights booked
total_nights = sum(booking_nights)
print("total nights booked:", total_nights)

# Check the calculation on the first three items
# By hand: 1+7+8=16
print("Total for the first three bookings:", sum(booking_nights[:3]))
# Test: The program returned 16 for the first three bookings,
# matching my handwritten calculation of 1 + 7 + 8