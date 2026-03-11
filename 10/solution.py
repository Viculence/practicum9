days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def date_to_days(date_str):
    day = int(date_str[:2])
    month = int(date_str[3:])

    total = 0
    for i in range(month - 1):
        total += days_in_months[i]
    total += day
    return total


with open("input.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

current_date = lines[0].strip()
n = int(lines[1].strip())

current_days = date_to_days(current_date)

result = []

for i in range(2, n + 2):
    parts = lines[i].strip().split()
    cell_number = parts[0]
    cell_date = parts[1]

    cell_days = date_to_days(cell_date)
    difference = current_days - cell_days

    if difference > 3:
        result.append(cell_number)

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(result))