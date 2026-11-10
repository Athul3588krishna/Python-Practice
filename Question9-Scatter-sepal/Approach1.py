import matplotlib.pyplot as plt
from sklearn.datasets  import load_iris
iris=load_iris()

sepal_length=iris.data[:,0]
sepal_width=iris.data[:,1]

plt.scatter(sepal_length,sepal_width)
plt.show()
