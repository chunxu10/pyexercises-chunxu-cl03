"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The booking nights list from exercise 4.0
# and a sample nightly price of 90 euros
# 2. Process: 
# Loop through the list, number each booking,
# and multiply its nights by the nightly price.
# 3. Out: One line per booking showing its position,
# number of nights, and total accommodation cost in euros
# 4. What I compute for each item, and why it is worth showing: 
# I calculate the accommodation cost for each booking.
# This lets the reader see how much each stay costs
# at the assumed fixed nightly price.


# Your code below
# Copy my booking nights list from exercise 4.0.
booking_nights = [1, 7, 8, 6, 2, 3, 4, 5]

# Use a sample fixed price of 90 euros per night.
price_per_night = 90

# Number each booking from 1 and calculate its accommodation cost.
for position, nights in enumerate(booking_nights, start=1):
    total_cost = nights * price_per_night
    print("Booking", position, "-", nights, "nights -", total_cost, "EUR")

#Booking 1 - 1 nights - 90 EUR
#Booking 2 - 7 nights - 630 EUR
#Booking 3 - 8 nights - 720 EUR
#Booking 4 - 6 nights - 540 EUR
#Booking 5 - 2 nights - 180 EUR
#Booking 6 - 3 nights - 270 EUR
#Booking 7 - 4 nights - 360 EUR
#Booking 8 - 5 nights - 450 EUR