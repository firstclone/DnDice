import random
all_dice = 4
top_dice = 3
sides = 6
dicey = {}
for i in range(0, all_dice):
    dicey[i] = random.randint(1,sides)
rolls = dicey.values()
rolls = sorted(rolls)[::-1]
top_rolls = 0
for x in range (top_dice):
    top_rolls = top_rolls + rolls[x]
print 'Str:', top_rolls
dicey = {}
for i in range(0, all_dice):
    dicey[i] = random.randint(1,sides)
rolls = dicey.values()
rolls = sorted(rolls)[::-1]
top_rolls = 0
for x in range (top_dice):
    top_rolls = top_rolls + rolls[x]
print 'Dex:', top_rolls
dicey = {}
for i in range(0, all_dice):
    dicey[i] = random.randint(1,sides)
rolls = dicey.values()
rolls = sorted(rolls)[::-1]
top_rolls = 0
for x in range (top_dice):
    top_rolls = top_rolls + rolls[x]
print 'Con:', top_rolls
dicey = {}
for i in range(0, all_dice):
    dicey[i] = random.randint(1,sides)
rolls = dicey.values()
rolls = sorted(rolls)[::-1]
top_rolls = 0
for x in range (top_dice):
    top_rolls = top_rolls + rolls[x]
print 'Int:', top_rolls
dicey = {}
for i in range(0, all_dice):
    dicey[i] = random.randint(1,sides)
rolls = dicey.values()
rolls = sorted(rolls)[::-1]
top_rolls = 0
for x in range (top_dice):
    top_rolls = top_rolls + rolls[x]
print 'Wis:', top_rolls
dicey = {}
for i in range(0, all_dice):
    dicey[i] = random.randint(1,sides)
rolls = dicey.values()
rolls = sorted(rolls)[::-1]
top_rolls = 0
for x in range (top_dice):
    top_rolls = top_rolls + rolls[x]
print 'Cha:', top_rolls
