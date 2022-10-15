import matplotlib.pyplot as plt

data_file = open('data.csv', 'a')
data_file.close()
data_file = open('data.csv', 'r')

ls = []
dictionary = {}

data_file.readline()

for line in data_file:
	ls.append(line.strip().split(","))

for i in ls:
	if i[7] in dictionary:
		dictionary[i[7]] += float(i[2])
	else:
		dictionary[i[7]] = float(i[2])

list_of_prices = list(dictionary.values())
list_of_prices.sort(reverse = True)

list_of_countries = []

def get_key(val):
    for key, value in dictionary.items():
         if val == value:
             return key

for i in list_of_prices:
	list_of_countries.append(get_key(i))

y = list_of_prices[:10]
x = list_of_countries[:10]

plt.bar(x,y, 0.5, color = 'm')


plt.title("Money spent per country in dollars")
plt.subplots_adjust(bottom=0.3, top=0.9)
plt.xticks(rotation='vertical')
plt.savefig("money_country.png")


data_file.close()