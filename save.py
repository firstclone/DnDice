import random
def save():
    roll = random.randint(1,20)
    if roll == 1:
        print 'Double Fail!'
    if roll > 1 and roll < 10:
        print 'Fail'
    if roll > 9 and roll < 20:
        print 'Success'
    if roll == 20:
        print 'Critical Success! +1 HP'
        
save()
