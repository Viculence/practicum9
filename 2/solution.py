with open("input.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

result = []

for line in lines:
    if line.lower().startswith("a"):
        result.append(line.strip())

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(result))