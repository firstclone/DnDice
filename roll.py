import random
import json
def roll(d,s,b):
    total = 0
    d = int(d)
    s = int(s)
    b = int(b)
    while d > 0:
        total = total + random.randint(1,s)
        d = d - 1
    final = total + b
    final = str(final)
    output = 'Roll = '
    output = output + final
    return output
    
dpos = text.index('d')
try: pluspos = text.index('+')
except:
    text = text + '+0'
    pluspos = text.index('+')
d = text[:dpos]
s = text[dpos+1:pluspos]
b = text[pluspos+1:]
roll(d,s,b)
