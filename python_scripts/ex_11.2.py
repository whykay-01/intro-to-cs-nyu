
try:
    input_file = open("ex_11.2_intnumbers.txt", "r")

    total = 0
    counter = 0

    for line in input_file:

        try:
            total = total + int(line.strip())
            counter = counter + 1
        except ValueError:
            print("Non-numeric data found:", line.strip())

    average = total/counter

    print("Average:", average)

    input_file.close()
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("File is empty or does not contain numeric data")
    input_file.close()