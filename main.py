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
    total_score = 0

    for round_number in range(3):
        print(f"\n--- Round {round_number + 1} ---")
        total_score += run_spin()

    print(f"\nTotal score: {total_score}")

if __name__ == "__main__":
    main()