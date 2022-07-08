# Importing modules needed
import random
import time

# Lists of prompts
character = ["Lumbah Jack","Ice Witch","Fire Queen"]
environment = ["Treehouse","Underground bunker"]
prop = ["Laser gun","Diamond staff"]
number = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","Unlimited"]

# Showing the prompts that are randomly selected
print("Hello - you're next art piece is going to be of:")
time.sleep(1)
print("...")
time.sleep(1)
print("Character - ", random.choice(character))
time.sleep(1)
print("Environment - ", random.choice(environment))
time.sleep(1)
print("Prop - ", random.choice(prop))
time.sleep(1)
print("Number of colours - ", random.choice(number))
time.sleep(1)
print("Good Luck")
