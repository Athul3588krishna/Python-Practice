import matplotlib.pyplot as plt


roll_no=list(map(int,input("Enter roll no:").split()))
marks=list(map(int,input("Enter marks no:").split()))

plt.scatter(roll_no,marks,color='green')
plt.show()