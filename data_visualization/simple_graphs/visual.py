import matplotlib.pyplot as plt

xlist = []
ylist_1 = []
ylist_2 = []
ylist_3 = []

for x in range(21):
	xlist.append(x)
	ylist_1.append(x)
	ylist_2.append(x**2)
	ylist_3.append(400 - x**2)

# plt.bar(xlist,ylist_2, 1, color = 'g', label = "y2 = x^2")
# plt.bar(xlist,ylist_3, 1, color = 'm', label = "400 - x^2")
# plt.bar(xlist,ylist_1, 1, color = 'r', label = "y1 = x")


plt.plot(xlist,ylist_1, color = 'r', label = "y1 = x")
plt.plot(xlist,ylist_2, color = 'g', label = "y2 = x^2")
plt.plot(xlist,ylist_3, color = 'm', label = "400 - x^2")

plt.ylabel("y")
plt.xlabel("x")
plt.xlim(0,20)
plt.ylim(0,400)
plt.legend()

plt.title("Graph #2")
plt.savefig("plotting_equations_2.png")
