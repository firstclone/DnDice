import random
def roll(d,s,b):
    total = 0
    while d > 0:
        total = total + random.randint(1,s)
        d = d - 1
    final = total + b
    print final
    
roll(1,6,0)
