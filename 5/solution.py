try:
    with open("input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    a = int(lines[0].strip())
    b = int(lines[1].strip())
    c = int(lines[2].strip())

    result = a / b + c

    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(str(result))

except ZeroDivisionError:
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("division by 0")

except ValueError:
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("data error")