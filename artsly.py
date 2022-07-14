# Importing modules needed
import random
import time
import streamlit as st

# Lists of prompts
character = ["Lumbah Jack","Ice Witch","Fire Queen","Royal Dragon Groomer","Whale hunter","The world's worst super hero team"]
environment = ["Treehouse","Underground bunker"]
prop = ["Laser gun","Diamond staff"]
number = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","Unlimited"]
sentences = ["Elephant working in a cubicle","Grasshopper hopping over hurdles in the Olypics","A tiny elephant eating a huge banana","Frogs robbing bank while police aren't looking","Cats falling from the sun","People knitting scarves with knives","Mermaids being discovered on TV","A man jumping from the Statue of Liberty","Bookshelves leading to a portal","A dog jumping over a young child","A man pushing a kangaroo into an acid lake","A parade with gorillas and minions","An aliean librarian","An enourmous ant eating slugs at a dinner table","Frogs eating dragonflies with knives",]

st.title('Artsly')

st.write(random.choice(sentences))
st.button('Generate New Prompt')
#{
#st.write("Select one or more and get creative."),
#time.sleep(3),
#st.write("Your next art piece is going to be of:"),
#time.sleep(1),
#st.write("......................................"),
#time.sleep(1),
#st.write("Character - ", random.choice(character)),
#time.sleep(1),
#st.write("Environment - ", random.choice(environment)),
#time.sleep(1),
#st.write("Prop - ", random.choice(prop)),
#time.sleep(1),
#st.write("Number of colours - ", random.choice(number)),
#time.sleep(1),

#time.sleep(1),
#st.write("Good Luck!"),
#time.sleep(0.1),
#st.write("And have fun!")
#}
