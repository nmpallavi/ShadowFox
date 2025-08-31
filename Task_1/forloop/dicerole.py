import random
rolls = [random.randint(1, 6) for _ in range(30)]
count_6 = rolls.count(6)
count_1 = rolls.count(1)
count_two_6s = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        count_two_6s += 1
print("Rolls:", rolls)
print("Number of times rolled 6:", count_6)
print("Number of times rolled 1:", count_1)
print("Number of times rolled two 6s in a row:", count_two_6s)
