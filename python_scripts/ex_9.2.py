
def check_even(number):
    if number %2 == 0:
        return True
    else:
        return False

for i in range(100):
    if check_even(i):
        print(i, "is even")