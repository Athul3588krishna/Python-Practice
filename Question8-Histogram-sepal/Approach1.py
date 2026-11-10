import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
length=iris.data[:,0]

plt.hist(length,bins=10,edgecolor='black')
plt.xlabel("Frequency")
plt.ylabel("Sepal length ")
plt.show()

### Algorithm – Draw Histogram of Sepal Length Using Iris Dataset

1. Start.
2. Import Matplotlib and Iris dataset.
3. Load the Iris dataset using `load_iris()`.
4. Extract the sepal length values from the dataset.
5. Draw a histogram using `plt.hist()` with 10 bins.
6. Add X-axis and Y-axis labels.
7. Display the histogram using `plt.show()`.
8. Stop.
