import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
length=iris.data[:,0]

plt.hist(length,bins=10,edgecolor='black')
plt.xlabel("Frequency")
plt.ylabel("Sepal length ")
plt.show();