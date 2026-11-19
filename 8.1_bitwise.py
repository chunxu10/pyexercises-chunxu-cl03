"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In:
#    Four permissions for staff using the hotel booking system.
#    Each permission is one bit (one position in a binary number):
#      VIEW_BOOKING   = 1  -> 0001  can see a booking
#      EDIT_BOOKING   = 2  -> 0010  can change dates or room of a booking
#      CANCEL_BOOKING = 4  -> 0100  can cancel a booking
#      APPLY_DISCOUNT = 8  -> 1000  can give a price discount
#    Each value is a power of 2, so each permission uses its own bit
#    and two permissions never overlap.
#
# 2. Process:
#    Step 1: give a receptionist VIEW and EDIT, combined with | (OR).
#    Step 2: test whether the receptionist can CANCEL, with & (AND).
#    Step 3: add CANCEL with |.
#    Step 4: test CANCEL again.
#    Step 5: remove EDIT with & ~ (AND NOT).
#
# 3. Out:
#    After each step: the permission value as a normal number and in binary
#    (4 bits), plus the list of permissions that are switched on.
#
# 4. What my permissions are about:
#    Who may do what in the hotel booking system. A receptionist needs to view
#    and edit bookings. A manager can also cancel bookings and give discounts.
#    Storing them as bits means one number holds all the permissions of a person.
#
# How the operators work, bit by bit:
#    a | b   (OR)  a bit is 1 if it is 1 in a OR in b        -> switch a bit ON
#    a & b   (AND) a bit is 1 only if it is 1 in a AND in b  -> TEST a bit
#    ~b      (NOT) turns every 1 into 0 and every 0 into 1
#    a & ~b        keeps everything in a except the bits of b  -> switch a bit OFF

# Your code below
# One bit for each permission
VIEW_BOOKING = 1     # 0001
EDIT_BOOKING = 2     # 0010
CANCEL_BOOKING = 4   # 0100
APPLY_DISCOUNT = 8   # 1000

# Names used to display which permissions are switched on
PERMISSION_NAMES = [
    (VIEW_BOOKING, "VIEW_BOOKING"),
    (EDIT_BOOKING, "EDIT_BOOKING"),
    (CANCEL_BOOKING, "CANCEL_BOOKING"),
    (APPLY_DISCOUNT, "APPLY_DISCOUNT"),
]


def show(step, permissions):
    """Display the permissions as a number, in 4-bit binary, and by name."""
    names = []
    for bit, name in PERMISSION_NAMES:
        # & keeps only this bit: the result is not 0 if the bit is on
        if (permissions & bit) != 0:
            names.append(name)
    binary = format(permissions, "04b")   # "04b" = binary, at least 4 digits
    print(f"{step:<28} value={permissions:<3} binary={binary}  {names}")


# Step 1: combine two permissions with | (OR)
#   0001
# | 0010
# = 0011  -> 3
receptionist = VIEW_BOOKING | EDIT_BOOKING
show("1. VIEW | EDIT", receptionist)

# Step 2: test whether CANCEL (0100) is present, with & (AND)
#   0011
# & 0100
# = 0000  -> 0, so CANCEL is NOT present
can_cancel = (receptionist & CANCEL_BOOKING) != 0
print(f"{'2. Can cancel?':<28} {can_cancel}")

# Step 3: add CANCEL with | (OR)
#   0011
# | 0100
# = 0111  -> 7
receptionist = receptionist | CANCEL_BOOKING
show("3. add CANCEL", receptionist)

# Step 4: test CANCEL again
#   0111
# & 0100
# = 0100  -> 4, not 0, so CANCEL is present now
can_cancel = (receptionist & CANCEL_BOOKING) != 0
print(f"{'4. Can cancel now?':<28} {can_cancel}")

# Step 5: remove EDIT with & ~ (AND NOT)
#   ~0010 = ...1101 (every bit flipped)
#   0111
# & 1101
# = 0101  -> 5: VIEW and CANCEL stay, EDIT is gone
receptionist = receptionist & ~EDIT_BOOKING
show("5. remove EDIT", receptionist)

# Extra check: a full manager has all four bits on
manager = VIEW_BOOKING | EDIT_BOOKING | CANCEL_BOOKING | APPLY_DISCOUNT
show("Manager (all four)", manager)

# Output when I ran it (I read the bits myself, right to left:
#1. VIEW | EDIT               value=3   binary=0011  ['VIEW_BOOKING', 'EDIT_BOOKING']
#2. Can cancel?               False
#3. add CANCEL                value=7   binary=0111  ['VIEW_BOOKING', 'EDIT_BOOKING', 'CANCEL_BOOKING']
#4. Can cancel now?           True
#5. remove EDIT               value=5   binary=0101  ['VIEW_BOOKING', 'CANCEL_BOOKING']
#Manager (all four)           value=15  binary=1111  ['VIEW_BOOKING', 'EDIT_BOOKING', 'CANCEL_BOOKING', 'APPLY_DISCOUNT']