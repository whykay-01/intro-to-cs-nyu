import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []
y3 = []

for i in range(21):
    x.append(i)
    y1.append(i)
    y2.append(i**2)
    y3.append(400 - i**2)

# plt.plot(x, y1, color='r', label="y1 = x")
# plt.plot(x, y2, color='g', label="y2 = x^2")
# plt.plot(x, y3, color='m', label="y1 = 400 - x^2")


plt.bar(x, y2, 1, color='g', label="y2 = x^2")
plt.bar(x, y3, 1, color='m', label="y1 = 400 - x^2")
plt.bar(x, y1, 1, color='r', label="y1 = x")

plt.xlim(0,20)
plt.ylim(0,400)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig("fig.pdf")