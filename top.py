def top(all_dice, top_dice, sides, bonus):
    if bonus == '':
        bonus = '0'
    if all_dice < top_dice:
        print 'ERROR: Total dice rolled fewer than dice kept.'
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = bonus
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print top_rolls
