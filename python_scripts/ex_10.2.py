
def char_frequencies(string):
    result = {}
    for char in string:
        # Option 1
        # result[char] = string.count(char)

        # Option 2
        # if char in result:
        #     result[char] = result[char] + 1
        # else:
        #     result[char] = 1

        result[char] = result.get(char, 0) + 1

    return result

print(char_frequencies("Hello World!"))