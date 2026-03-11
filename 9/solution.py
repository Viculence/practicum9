import os

os.makedirs("simple", exist_ok=True)

with open("input.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

result = []

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        result.append(lines[i].strip())

with open("simple/output.txt", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(result))