import streamlit as st
import random
import time
import json

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
        return {"last_pressed_date": None, "proverb": None}

# Save state to file
def save_state(state):
    with open('state.json', 'w') as state_file:
        json.dump(state, state_file)

# Get current date
current_date = time.strftime("%Y-%m-%d")

# Prompt user for unique identifier
user_id = st.text_input("Enter your username or email:", key="user_id")
if not user_id:
    st.warning("Please enter your username or email to proceed.")
    st.stop()

# Load state
state = load_state()
user_data = state.get(user_id, {"last_pressed_date": None, "proverb": None})

# Check if button should be disabled
disabled_button = user_data["last_pressed_date"] == current_date

# Display last proverb if available
if user_data["proverb"] and user_data["last_pressed_date"] == current_date:
    st.write(f"Today's proverb for {user_id}:\n\n{user_data['proverb']}")

# Button to generate a new proverb
if st.button("Scroll 📜", disabled=disabled_button):
    proverb = pick_scroll()
    user_data["last_pressed_date"] = current_date
    user_data["proverb"] = proverb
    state[user_id] = user_data
    save_state(state)
    st.session_state['disabled_button'] = True
    st.write(f"Today's proverb for {user_id}:\n\n{proverb}")
