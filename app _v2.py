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
st.markdown("A beginner-friendly halal spinner app for good deeds, study, health, and kindness tasks.")

if "total_score" not in st.session_state:
    st.session_state.total_score = 0
    
if "last_spin" not in st.session_state:
    st.session_state.last_spin = None

if "last_msg" not in st.session_state:
    st.session_state.last_msg = ""

if "last_points" not in st.session_state:
    st.session_state.last_points = 0

if "last_category" not in st.session_state:
    st.session_state.last_category = ""

if "last_task" not in st.session_state:
    st.session_state.last_task = ""

col1, col2 = st.columns(2)

with col1:
    if st.button("Spin"):
        spin_result = spin_symbols()
        score, msg = get_result(spin_result)
        category, task = get_rndm_task()

        st.session_state.last_spin = score
        st.session_state.last_msg = msg
        st.session_state.last_points = score
        st.session_state.last_category = category
        st.session_state.last_task = task
        st.session_state.total_score += score

with  col2:
    if st.button("Reset Score"):
        st.session_state.total_score = 0
        st.session_state.last_spin = None
        st.session_state.last_msg = ""
        st.session_state.last_points = 0
        st.session_state.last_category = ""
        st.session_state.last_task = ""
  
st.markdown(f"## Total Score: {st.session_state.total_score}")    

if st.session_state.last_spin is not None:
    st.markdown("Spin Result:")
    st.markdown(f"### {' | '.join(st.session_state.last_spin)}")

    st.success(st.session_state.last_msg)
    st.write(f"**Points earned this round:** {st.session_state.last_points}")
    st.write(f"**Task category:** {st.session_state.last_category}")    
    st.write(f"**Task:** {st.session_state.last_task}")

else:
    st.info("Click the Spin button to get your first result")
