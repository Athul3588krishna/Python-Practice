import matplotlib.pyplot as plt

marks=list(map(int,input("Enter marks : ").split()))
bins=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(marks,bins=bins,edgecolor="black")
plt.xlabel("students")
plt.ylabel("intervals")
plt.title("Mark list")
plt.show()