
def convert_temp(value, unit="C"):
    if unit == "C":
        print(value * 9/5 + 32)
    elif unit == "F":
        print((value - 32) * 5/9)
    else:
        print("Invalid unit")

convert_temp(104, "F")
convert_temp(40, "C")
convert_temp(40)
