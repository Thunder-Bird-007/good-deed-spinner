import random
import json
import streamlit as st

from main import run_spin

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
    
st.set_page_config(page_title="Good Deed Spinner", page_icon="🌟")

st.title("🌟 Good Deed Spinner")
st.write("A beginner-friendly halal spinner app for good deeds, study, health, and kindness tasks.")

if "total_score" not in st.session_state:
    st.session_state.total_score = 0

if st.button("Spin"):
    spin_result = spin_symbols()
    score, msg = get_result(spin_result)
    category, task = get_rndm_task()

    st.write("Spinning...")
    st.write(" | ".join(spin_result))
    st.write(msg)
    st.write(f"Your score: {score}")
    st.write(f"Your good deed category: {category}")
    st.write(f"Your good deed task: {task}")

    st.session_state.total_score += score
st.write(f"Total Score: {st.session_state.total_score}")