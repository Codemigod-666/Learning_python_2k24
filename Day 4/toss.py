# You are going to write a virtual coin toss program, It will randomly
# tell  the user "heads" or "Tails"
#
# there are many way of doing this. But to practice what we learnt, you
# should generate a random number. either 0 or 1. then use that number to priint out
# heads and tails

import random

result = random.randint(0,1)
print("Heads" if result == 1 else "Tails")