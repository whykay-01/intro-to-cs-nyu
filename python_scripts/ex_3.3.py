name = input("Please enter your first and last name (all lower case): ")
birthday = input("Please you birthday date as an 8-digit number: ")

name = name.title()
day = birthday[6:]
month = birthday[4:6]
year = birthday[:4]

print(name, "was born on", day + "/" + month + "/" + year)
