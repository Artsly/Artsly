# Importing modules needed
import random
import time
import streamlit as st

# Lists of prompts
prompts = ["Lumbah Jack","Ice Witch","Fire Queen","Royal Dragon Groomer","Whale hunter","The world's worst super hero team","Treehouse","Underground bunker","Laser gun","Diamond staff","Elephant working in a cubicle","Grasshopper hopping over hurdles in the Olypics","A tiny elephant eating a huge banana","Frogs robbing bank while police aren't looking","Cats falling from the sun","People knitting scarves with knives","Mermaids being discovered on TV","A man jumping from the Statue of Liberty","Bookshelves leading to a portal","A dog jumping over a young child","A man pushing a kangaroo into an acid lake","A parade with gorillas and minions","An alien librarian","An enourmous ant eating slugs at a dinner table","Frogs eating dragonflies with knives","A cabbage that can suddenly walk and talk","DanTDM gaining the ability to fly","A famous actor flying through New York City","A snowball fight but with meatballs","A hidden portal under the sea","A suspicious looking woman selling rare frogs at a school","A giraffe holding a young child","A man teaching a gorilla to dance",]

st.title('Artsly')

st.write(random.choice(prompts))
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
