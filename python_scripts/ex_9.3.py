
def reverse_string(string):
    result = ''
    for char in range(len(string)-1, -1, -1):
        result = result + string[char]

    return result
    # return string[::-1]


my_string = "Hello World"
print(reverse_string(my_string))