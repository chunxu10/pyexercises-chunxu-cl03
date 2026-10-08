"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A dictionary describing a hotel booking with five fields
# 2. Process:
# read a value, update a value, remove a field,
# handle a missing field, and display all remaining fields
# 3. Out: The guest's name, a missing-field message,
# and all fields and values in the updated booking
# 4. My object, my five fields, and why those:
# guest_name identifies the guest.
# room_number identifies the booked room.
# nights records the length of the stay.
# price_per_night records the nightly room price in euros.
# special_request records a guest preference for staff to consider.

# Your code below
# Create a sample hotel booking with five useful fields.
booking = {
    "guest_name": "chunxu",
    "room_number": 203,
    "nights": 3,
    "price_per_night": 90.0,
    "special_request": "Quiet room"
}

# Read and display the guest's name.
print("Guest name:", booking["guest_name"])

# Update the booking from three nights to four nights.
booking["nights"] = 4

# Remove the special request after the guest withdraws it.
del booking["special_request"]

# Try to read a missing field and handle the error without stopping.
try:
    print("Email:", booking["email"])

# File "/workspaces/pyexercises/4.2_dictionaries.py", line 60
#    print("Email:", booking["email"])
#SyntaxError: expected 'except' or 'finally' block

except KeyError:
    print("The booking has no email field.")

# Display every remaining field and its value.
for field, value in booking.items():
    print(field, ":", value)

#Guest name: chunxu
#The booking has no email field.
#guest_name : chunxu
#room_number : 203
#nights : 4
#price_per_night : 90.0