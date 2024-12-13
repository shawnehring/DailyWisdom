import streamlit as st
import random
import json
from datetime import datetime
from pytz import timezone

st.title("Daily Wisdom")
st.write("A random proverb from the book of Proverbs per day.")

# Load proverbs from file
with open('new_proverbs.txt', 'r') as proverbs_file:
    proverbs = proverbs_file.readlines()

# Function to pick and format a proverb
def pick_scroll():
    scroll = random.choice(proverbs).strip('\n')
    return scroll

# Load stored state
def load_state():
    try:
        with open('state.json', 'r') as state_file:
            return json.load(state_file)
    except FileNotFoundError:
        return {}

# Save state to file
def save_state(state):
    with open('state.json', 'w') as state_file:
        json.dump(state, state_file)

# Get current date in CST
def get_current_date_cst():
    cst = timezone('US/Central')
    return datetime.now(cst).strftime("%Y-%m-%d")

current_date = get_current_date_cst()

# Prompt user for unique identifier
user_id = st.text_input("Enter your name:", key="user_id").lower()
if not user_id:
    st.warning("Please enter your name.")
    st.stop()

# Load global state
state = load_state()
user_data = state.get(user_id, {"last_pressed_date": None, "proverb": None})

# Display last proverb if available
if user_data["last_pressed_date"] != current_date:
    proverb = pick_scroll()
    user_data["last_pressed_date"] = current_date
    user_data["proverb"] = proverb
    state[user_id] = user_data
    save_state(state)

st.write(f"Today's proverb for {user_id}:\n\n{user_data['proverb']}")
