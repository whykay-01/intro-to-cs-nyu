import matplotlib.pyplot as plt

def findValueInDictionary(value):
    for key in sales:
        if sales[key] == value:
            del sales[key]
            return key


file = open('ex_22.2_SalesJan2009.csv', 'r')

sales = {}

file.readline()
for line in file:
    line = line.strip().split(",")
    if line[7] in sales:
        sales[line[7]] += int(line[2])
    else:
        sales[line[7]] = int(line[2])

file.close()
print(sales)

y = list(sales.values())

y.sort(reverse=True)
x= []

for value in y:
    country = findValueInDictionary(value)
    x.append(country)

print(y)
print(x)


plt.bar(x[:10],y[:10],0.5)

plt.subplots_adjust(bottom=0.3, top=0.9)
plt.xticks(rotation='vertical')
plt.savefig("sales.png")