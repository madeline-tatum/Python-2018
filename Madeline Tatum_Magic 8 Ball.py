import random
import time

name = input("What's your name: ")
print(f"Hi {name} welcome to the magic 8 ball.")

r1 = f"Nope, no hope for you {name}."
r2 = "Eh, it's pretty unlikely man."
r3 = "I'm not sure, I mean, it's not impossible."
r4 = "Maaaaaybe..."
r5 = "Yasssssss!!!"
r6 = f"Oh absolutely! Yes yes YES {name}!"
responses = [r1,r2,r3,r4,r5,r6]

while True:
    ques = input("Ask me any yes/no question (When you are done, type stop): ")
    if ques == "stop":
        print(f"Thanks for asking, goodbye {name}!")
        break
    else:
        print("Hmmm...")
        time.sleep (2)
        print(random.choice(responses))
