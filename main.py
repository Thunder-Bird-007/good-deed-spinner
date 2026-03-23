import random
import json

def load_tasks():
    with open("data/tasks.json", "r", encoding="utf-8") as file:
        return json.load(file)

SYMBOLS = ["🌙", "📘", "🤲", "⭐", "🕌"]
TASKS = load_tasks()

def spin_symbols():
    return [
        random.choice(SYMBOLS),
        random.choice(SYMBOLS),
        random.choice(SYMBOLS)
    ]

def get_rndm_task():
    """Returns a random task from a random category."""
    category = random.choice(list(TASKS.keys()))
    task = random.choice(TASKS[category])
    return category, task

def get_result(spin_result):
    a, b, c = spin_result
    if a==b==c:
        return 20, "Jackpot! You got three of the same symbol!"
    elif a==b or b==c or c==a:
        return 10, "Two of the same symbol! Not bad!"
    else:
        return 5, "No matches this time. But you still get a good deed task!"

def run_spin():
    spin_result = spin_symbols()
    score, msg = get_result(spin_result)
    category, task = get_rndm_task()

    print("Spinning...")
    print(" | ".join(spin_result))
    print(msg)
    print(f"Your score: {score}")
    print(f"Your good deed category: {category}")
    print(f"Your good deed task: {task}")

    return score

def main():
    print("\n=== GOOD DEED SPINNER ===")
    total_score = 0
    
    while True:
        print("Choose option:\n1. Spin\n2. View Total Score\n3. Exit ")

        usr_inp = input("What do you want to do? ")

        if usr_inp.isdigit():
            usr_inp = int(usr_inp)
    
            if usr_inp == 1:
                score = run_spin()
                total_score += score
            elif usr_inp == 2:
                print(f"Your total score is: {total_score}")
            elif usr_inp == 3:
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")

        else:
            print("Invalid input. Please enter a number (1, 2, or 3).")


if __name__ == "__main__":
    main()