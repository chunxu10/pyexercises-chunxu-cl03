# First name: Chunxu
# Last name: DAI
# Group number: CL03
# Scenario group: B

# 1. What goes in?
# My program reads scenarios_B.csv.
# The file uses a semicolon as the separator and has 14 columns.
# The first line is the header. Some text fields are wrapped in double quotes
# because they contain quotes or commas; the csv module handles this.
# Num contains the scenario number, and Situation describes the event.
# Each option, A, B and C, has four fields:
# Choice contains the option text, Money contains the budget change,
# Buzz contains the reputation change, and Reaction contains the feedback.
# The file currently contains 30 scenarios. I will add scenarios 31 to 33.
# Budget and reputation changes are written as integers.
# Negative numbers decrease the gauges, positive numbers increase them,
# and zero means no change.
# I convert these values from strings to integers before calculating.
# The player also enters their name, difficulty and daily choices.

# 2. What happens?
# At the start, I ask for the player's name and difficulty.
# Easy mode starts with 15000 EUR, and hard mode starts with 6000 EUR.
# Reputation starts at 50 in both modes.
# I load all scenarios, shuffle them and use the first ten.
# Each day, I display the day number, budget and reputation.
# I display the situation and the three options.
# I ask the player to choose A, B or C.
# I accept lowercase letters and ask again if the choice is invalid.
# I get the selected option and unpack its tuple.
# I add its budget change and reputation change to the current gauges.
# I limit reputation to a maximum of 100.
# I display the feedback and the updated gauges.
# I store the move in the history as a tuple.
# I check whether budget or reputation is zero or below.
# If either is zero or below, I stop the game immediately.
# Otherwise, I continue until the player has completed ten days.

# 3. What comes out?
# At the end, I display the final budget and reputation.
# If the player is fired, I explain which gauge reached zero or below.
# If both gauges reached zero or below, I mention both reasons.
# If the player is fired, the title is "Fired" and it is also saved in results.csv.
# If the player survives ten days, I calculate the final score:
# score = reputation + budget // 200.
# A score below 95 gives the title Eternal Intern.
# A score from 95 to 119 gives the title Growth Hacker.
# A score from 120 to 139 gives the title CMO Material.
# A score of 140 or more gives the title Viral Legend.
# I also display the best and worst moves, based on reputation changes.
# I append one row to results.csv with the player's name, final budget,
# final reputation, title and date.
# Example header: name,budget,reputation,title,date
# Example row: Alex,6350,100,CMO Material,2026-11-16
# Example row (fired): Sam,-300,40,Fired,2026-11-16

# 4. What could go wrong?
# The player might enter an invalid choice or leave it blank.
# I remove extra spaces, convert the input to uppercase,
# and keep asking until the player enters A, B or C.
# The player might enter an invalid difficulty.
# I keep asking until they choose easy or hard.
# The player might leave their name blank.
# I ask again until they enter a non-empty name.
# Budget or reputation might reach zero or become negative.
# I stop the game immediately and explain why the player is fired.
# Reputation might rise above 100.
# I cap it at 100 after applying the change.
# The scenario file might be missing.
# I catch the file error, show a clear message and stop safely.
# A required column might be missing or a number might be invalid.
# I report the data problem and stop instead of using incorrect data.
# There might be fewer than ten scenarios.
# I check the number of scenarios before starting the game.
# The results file might not exist yet.
# I create it and write the header before saving the first result.
# If saving fails, I display an error message instead of claiming success.

# Chosen feature: D - Difficulty selection.
# The player chooses easy mode with 15000 EUR or hard mode with 6000 EUR.
# I chose this feature because it lets players choose their challenge
# and lets me practise input validation and if/elif statements.

# Missing: nothing, the game is complete.


import csv
import random
import os
from datetime import date

# Settings of the game, so I can change them in one place
SCENARIO_FILE = "scenarios_B.csv"
RESULTS_FILE = "results.csv"
DAYS = 10
START_REPUTATION = 50
MAX_REPUTATION = 100


# Read the scenario file and return a list of scenarios.
# Each scenario is a dictionary with its number, its situation and its options.
# Each option (A, B, C) is stored as a tuple:
# (text, budget_change, reputation_change, feedback)
def load_scenarios(filename):
    scenarios = []
    with open(filename, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            options = {}
            for letter in ("A", "B", "C"):
                options[letter] = (
                    row[letter + "_Choice"],
                    int(row[letter + "_Money"]),
                    int(row[letter + "_Buzz"]),
                    row[letter + "_Reaction"],
                )
            scenarios.append({
                "num": int(row["Num"]),
                "situation": row["Situation"],
                "options": options,
            })
    return scenarios


# Ask the player's name until it is not empty
def ask_name():
    while True:
        name = input("What is your name? ").strip()
        if name:
            return name
        print("Please type your name.")


# Feature d: ask the difficulty and return the starting budget
def ask_difficulty():
    while True:
        answer = input("Difficulty, easy (15000 EUR) or hard (6000 EUR)? ").strip().lower()
        if answer in ("easy", "e"):
            return 15000
        elif answer in ("hard", "h"):
            return 6000
        print("Please type easy or hard.")


# Show the day number, both gauges, the situation and the three options
def show_day(day, budget, reputation, scenario):
    print(f"\n--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/{MAX_REPUTATION}]")
    print(scenario["situation"])
    for letter in ("A", "B", "C"):
        text = scenario["options"][letter][0]
        print(f"  {letter}: {text}")


# Ask for A, B or C until the answer is valid (lowercase is accepted)
def ask_choice():
    while True:
        answer = input("Your choice (A, B or C): ").strip().upper()
        if answer in ("A", "B", "C"):
            return answer
        print("Please type A, B or C.")


# Apply the impact of the chosen option and return the new gauges as a tuple.
# Reputation can never go above the maximum.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation


# Play up to ten days. Stop at once if a gauge reaches 0 or less.
# Return the final gauges and the history (one tuple per day).
def play_game(scenarios, budget, reputation):
    random.shuffle(scenarios)
    history = []
    for day in range(1, DAYS + 1):
        scenario = scenarios[day - 1]
        show_day(day, budget, reputation, scenario)
        letter = ask_choice()
        option = scenario["options"][letter]
        budget, reputation = apply_choice(budget, reputation, option)
        text, budget_change, reputation_change, feedback = option
        print(feedback)
        print(f"Budget {budget_change:+} EUR, Reputation {reputation_change:+}")
        print(f"Now: {budget} EUR, reputation {reputation}/{MAX_REPUTATION}")
        history.append((reputation_change, day, text))
        if budget <= 0 or reputation <= 0:
            break
    return budget, reputation, history


# Turn the final score into a title, using the table of the brief
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


# Show the end of the game: fired (and why) or the final score and title.
# Return the title so I can save it in results.csv later.
def show_result(name, budget, reputation):
    print("\n==============================")
    if budget <= 0 or reputation <= 0:
        if budget <= 0 and reputation <= 0:
            print("You are fired: no money left and no reputation left.")
        elif budget <= 0:
            print("You are fired: the budget is empty.")
        else:
            print("You are fired: your reputation hit zero.")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        title = "Fired"
    else:
        print("Quarter survived!")
        score = reputation + budget // 200
        title = get_title(score)
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print(f"Final score: {score}")
        print(f"{name}, your title: {title}")
    return title


# Find the best and the worst move in the history.
# Each tuple starts with the reputation change, so max() and min() compare it first.
def show_best_and_worst(history):
    best_change, best_day, best_text = max(history)
    worst_change, worst_day, worst_text = min(history)
    print(f'\nBest move:  day {best_day}, "{best_text}" ({best_change:+})')
    print(f'Worst move: day {worst_day}, "{worst_text}" ({worst_change:+})')


# Append one line to results.csv: name, budget, reputation, title, date.
# Write the header only when the file does not exist yet.
def save_result(name, budget, reputation, title):
    new_file = not os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# Run the whole game in order.
# If something goes wrong, show a clear message instead of crashing.
def main():
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
        if len(scenarios) < DAYS:
            print(f"Error: the file needs at least {DAYS} scenarios.")
            return
        name = ask_name()
        start_budget = ask_difficulty()
        budget, reputation, history = play_game(scenarios, start_budget, START_REPUTATION)
        title = show_result(name, budget, reputation)
        show_best_and_worst(history)
        save_result(name, budget, reputation, title)
        print(f"Saved in {RESULTS_FILE}")
    except FileNotFoundError:
        print(f"Error: the file {SCENARIO_FILE} was not found.")
    except (KeyError, ValueError):
        print(f"Error: {SCENARIO_FILE} has a missing column or an invalid number.")
    except (KeyboardInterrupt, EOFError):
        print("\nGame stopped. See you next quarter!")
    except OSError:
        print(f"Error: could not save the result in {RESULTS_FILE}.")


if __name__ == "__main__":
    main()