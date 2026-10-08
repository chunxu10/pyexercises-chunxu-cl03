"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the message "chunxu" 
# 2. Process:repeats the message five times and number each line
# 3. Out:five statements numbered
# 4. My message, and why:my name is chunxu,learning how to print in python


# Your code below

print("1. chunxu")
print("2. chunxu")
print("3. chunxu")
print("4. chunxu")
print("5. chunxu")


# range(1,count+1): generates integers from 1 to 5. 
# range includes the start value but excludes the end value, 
# so the end value must be 6, which is count +1

# i--> number, 
for i in range(1,6):
    print(i,"chunxu")

# 3 times
for i in range(1,4):
    print(i,"chunxu")
