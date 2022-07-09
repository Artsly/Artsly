# Importing modules needed
import random
import time
import streamlit as st

# Lists of prompts
character = ["Lumbah Jack","Ice Witch","Fire Queen"]
environment = ["Treehouse","Underground bunker"]
prop = ["Laser gun","Diamond staff"]
number = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","Unlimited"]

st.title('Artsly')

st.button('Generate Prompts')
{st.write('Hello'),
time.sleep(1),
st.write("PLEASE NOTE THESE ARE PROMPTS -YOU  DON'T HAVE TO DO THEM OR DO ALL OF THEM."),
time.sleep(3),
st.write("Your next art piece is going to be of:"),
time.sleep(1),
st.write("......................................"),
time.sleep(1),
st.write("Character - ", random.choice(character)),
time.sleep(1),
st.write("Environment - ", random.choice(environment)),
time.sleep(1),
st.write("Prop - ", random.choice(prop)),
time.sleep(1),
st.write("Number of colours - ", random.choice(number)),
time.sleep(1),
st.write("Good Luck!"),
time.sleep(0.1),
st.write("And have fun!")}

# Showing the prompts that are randomly selected
# print("Hello")
# time.sleep(1)
# print("PLEASE NOTE THESE ARE PROMPTS -YOU  DON'T HAVE TO DO THEM OR DO ALL OF THEM.")
# time.sleep(1)
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# time.sleep(2)
# print("Your next art piece is going to be of:")
# time.sleep(1)
# print("......................................")
# time.sleep(1)
# print("Character - ", random.choice(character))
# time.sleep(1)
# print("Environment - ", random.choice(environment))
# time.sleep(1)
# print("Prop - ", random.choice(prop))
# time.sleep(1)
# print("Number of colours - ", random.choice(number))
# time.sleep(1)
# print("Good Luck!")
# time.sleep(0.1)
# print("And have fun!")
