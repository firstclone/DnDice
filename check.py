import random
def check():
    abscore = int(raw_input('Ability Score: '))
    proflvl = int(raw_input('Proficiency Level: '))
    adv = raw_input('Advantage(a), Disadvantage(d): ').lower()
    roll = 0
    abil = {1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10}
    prof = {0: 0, 1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6, 20: 6}
    if adv == 'a':
        roll = random.randint(1,20)
        roll2 = random.randint(1,20)
        if roll2 > roll:
            roll = roll2
    elif adv == 'd':
        roll = random.randint(1,20)
        roll2 = random.randint(1,20)
        if roll2 < roll:
            roll = roll2
    else:
        roll = random.randint(1,20)
    if roll == 20:
        print 'Critical Hit!'
    if roll == 1:
        print 'Critical Fail!'
    profbonus = prof.get(proflvl, 0)
    abbonus = abil.get(abscore, -5)
    score = roll + profbonus + abbonus
    print score
check()
