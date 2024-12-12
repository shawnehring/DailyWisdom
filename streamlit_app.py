import streamlit as st
import random
import time
import json

st.title("Daily Wisdom")
st.write(
    "A random proverb from the book of Proverbs per day."
)
#Open file
proverbs = open('new_proverbs.txt','r')
pick = proverbs.readlines()
proverbs.close()

#picks the verse
def pick_scroll():
    scroll = random.choice(pick)
    some_scroll = scroll.strip('\n')
    list_scroll = some_scroll.strip(' ')
    list_scroll[len(list_scroll)//2:len(list_scroll)//2] = '\n'
    new_scroll = ' '.join(list_scroll)
    st.write(new_scroll)
    return new_scroll

# Load stored data
def load_state():
    try:
        with open('state.json', 'r') as state_file:
            return json.load(state_file)
    except FileNotFoundError:
        return {"last_pressed_date": time.strftime("%Y-%m-%d"), "proverb": None}

# Save stored data
def save_state(state):
    with open('state.json', 'w') as state_file:
        json.dump(state, state_file)



#clock part
state = load_state()
current_date = time.strftime("%Y-%m-%d")

#if clock is disabled
disabled_button = state.get("last_pressed_date") == current_date


#creates button
if st.button('Scroll', key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", icon='📜', disabled=disabled_button, use_container_width=False):
    proverb = pick_scroll()
    state["last_pressed_date"] = current_date
    state["proverb"] = proverb
    save_state(state)

#if already pressed it that day
if state.get("proverb"):
    st.write(state["proverb"])


