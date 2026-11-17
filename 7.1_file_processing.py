"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - there are two empty lines, at lines 3 and 9.
# - Some names have extra spaces at the beginning.
# - Capitalisation is inconsistent, for example "ada LOVELACE".
# - "GUIDO van rossum" has a two-word surname, which must stay together.

# 1. In: names.txt, containing 10 lines, including two empty lines.
# 2. Process, problem by problem:
# - Skip empty lines.
# - Use strip() and split() to remove extra spaces.
# - Capitalise names consistently, keeping "van" lowercase.
# - Keep all words after the first name together as the surname.
# - Sort by the complete surname, ignoring case.
# - Write the cleaned names to a new file.
# 3. Out:
# names_sorted.txt, containing eight cleaned names, one per line.
# The original names.txt is not modified.
# 4. How I decide which word is the last name:
# For this file, I assume names are written in first-name-first order.
# When there are two words, the second word is the surname.
# For "GUIDO van rossum", the complete surname is "van Rossum".
# I include "van" when sorting, so this surname is sorted under V.
# This convention is suitable for this file, but not necessarily all names.


# Your code below
INPUT_FILE = "names.txt"
OUTPUT_FILE = "names_sorted.txt"
PARTICLES = ["van", "von", "de", "der", "da"]


def tidy_word(word):
    word = word.lower()
    if word in PARTICLES:
        return word
    return word.capitalize()


def split_name(line):
    words = line.split()
    first_name = tidy_word(words[0])
    last_words = []
    for word in words[1:]:
        last_words.append(tidy_word(word))
    last_name = " ".join(last_words)
    return [first_name, last_name]


# Read the original file (read mode only, so it is not modified)
with open(INPUT_FILE, "r") as infile:
    lines = infile.readlines()

# Clean every line
people = []
for line in lines:
    line = line.strip()
    if line == "":
        continue
    people.append(split_name(line))

# Sort by last name, ignoring upper/lower case
people.sort(key=lambda person: person[1].lower())

# Write the result to a new file
with open(OUTPUT_FILE, "w") as outfile:
    for person in people:
        outfile.write(person[0] + " " + person[1] + "\n")

print("Read", len(lines), "lines from", INPUT_FILE)
print("Wrote", len(people), "names to", OUTPUT_FILE)

# Check:
# - names.txt has 10 lines; names_sorted.txt has 8 lines.
#   The difference is 2 because the two empty lines (line 3 and line 9) were removed.
#   No real name was lost: I counted 8 people in names.txt by hand.
# - First name of the sorted list: Margaret Hamilton ("Hamilton" is the earliest
#   last name alphabetically: H-a comes before H-o of Hopper).
# - Last name of the sorted list: Guido van Rossum ("van Rossum" starts with V,
#   later than T of Torvalds and Turing).
# - names.txt is unchanged after running the program.