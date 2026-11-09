import random
import time
import sys
def type_story(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()








names = ["Mr. Donavan", "Mr. Ethan", "Mr. William", "Mrs. Susie", "Mrs. Claire", "Mr. Andrew"]
rooms = ["bedroom", "kitchen", "dining room", "engine room"]
random.shuffle(names)
random.shuffle(rooms)
room1 = rooms[0]
room2 = rooms[1]
room3 = rooms[2]
room4 = rooms[3]

name1 = names[0] 
name2 = names[3]
name3 = names[2]
name4 = names[1]
name5 = names[4]
name6 = names[5]
random.choice(name1)
random.choice(room1)



print("What do you want your detective name to be")

nicname = input("\n I want my detective name to be ")

    



print(" Hello and Welcome to the ISS Lincoln. " +nicname+ " you have been asleep for 99 years.\n In the years that you have been asleep we have travled 99,000,000 miles and are deep in space.\n You are the last to wake up because you are a detective AND " +name1+ " HAS BEEN MERDERED. And YOU need to figure out who it is There names are Mr. Donavan, Mr. Ethan, Mr. William, Mrs. Susie, Mrs. Claire, Mr. Andrew but "+name1+ " is dead in the " +room1)

print("\n please intareagate them you will first start with "+name3+ "\n You will only get one question")
answer = input("Hello im "+name3+ " What do you want to know? (Where were you? Who were you with?) ")
#names 123 are done name 2 is the merder 
if answer == "where were you":
    print("I was in "+room2+ " with "+name4)
elif answer == "who were you with":
    print("I was with "+name4)
else:
    print("I dont know what your talking about")
print("\n now lets talk to "+name5)
talk2 = input("Hey im "+name5+ " whats up ")
if talk2 == "where were you":
    print("I was in "+room3)
elif talk2 == "who were you with":
    print("Nobody")
else:
    print("I dont know what your talking about")

























input("my guess on who killed " +name1+ " is ")
if input == name2:
    print("you did it")
else:
    print("nope its " +name2 )