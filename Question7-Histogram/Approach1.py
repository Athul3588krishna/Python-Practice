import matplotlib.pyplot as plt

marks=[45,60,68,76,35,89,91]
bins=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(marks,bins=bins,edgecolor="black")
plt.xlabel("students")
plt.ylabel("intervals")
plt.title("Mark list")
plt.show()