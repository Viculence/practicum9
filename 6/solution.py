with open("input.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

try:
    n = int(lines[0].strip())
except ValueError:
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("ERROR")
else:
    remaining_lines = len([line for line in lines[1:] if line.strip()])

    if remaining_lines == n:
        result = "YES"
    else:
        result = "NO"

    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(result)