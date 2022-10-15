
words = input("Please enter 4 words of the same theme, separated by comma: ")
words_list = words.split(',')

word = input("Please enter another word of the same theme: ")
words_list.insert(0, word)

print("\n" * 100)
guess = input("Please guess a word: ")
outcome = guess in words_list

messsage = ["Sorry, wrong guess", "Congratulations"]
print(messsage[outcome])