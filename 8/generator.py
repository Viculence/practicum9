import random

with open("input.txt", "w", encoding="utf-8") as f:
    for i in range(365):
        steps = random.randint(2000, 20000)
        f.write(str(steps) + "\n")