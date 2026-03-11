days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("input.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

result = []
current_line = 0

for days in days_in_months:
    month_steps = []

    for i in range(days):
        steps = int(lines[current_line].strip())
        month_steps.append(steps)
        current_line += 1

    average = sum(month_steps) / days
    result.append(str(round(average)))

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(result))