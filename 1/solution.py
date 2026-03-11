with open("input.txt", "r", encoding="utf-8") as input_file:
    content = input_file.read()

result = content.upper()

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(result)