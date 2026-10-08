"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The hotel booking nights list from exercise 4.0
# 2. Process: Display the original order, reverse a copy,
# create an ascending sorted list, and sort a copy in descending order
# 3. Out: Four different orders, followed by the unchanged original list
# 4. My four orders, and which ones modify the original:
# Original order: Display the original list without changing it
# Reversed order: reverse() modifies a copy, not the original
# Ascending order: sorted() returns a new list
# Descending order: sort(reverse=True) modifies a copy, not the original
# None of these steps modifies my original list


# Your code below
# Use the same list as in exercise 4.0 and display its original order
booking_nights = [1, 7, 8, 6, 2, 3, 4, 5]
print("Original order:", booking_nights)

# Reverse a separate copy
reversed_nights = booking_nights.copy()
reversed_nights.reverse()
print("Reversed order:", reversed_nights)

# from smallest to largest
ascending_nights = sorted(booking_nights)
print("Ascending order:", ascending_nights)

# from largest to smallest
descending_nights = booking_nights.copy()
descending_nights.sort(reverse=True)
print("Descending order:", descending_nights)

# Display the original list last to check that its order is unchanged.
print("Original list at the end:", booking_nights)

#Original order: [1, 7, 8, 6, 2, 3, 4, 5]
#Reversed order: [5, 4, 3, 2, 6, 8, 7, 1]
#Ascending order: [1, 2, 3, 4, 5, 6, 7, 8]
#Descending order: [8, 7, 6, 5, 4, 3, 2, 1]
#Original list at the end: [1, 7, 8, 6, 2, 3, 4, 5]