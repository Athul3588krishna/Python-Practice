import matplotlib.pyplot as plt
from sklearn.datasets  import load_iris
iris=load_iris()

sepal_length=iris.data[:,0]
sepal_width=iris.data[:,1]

plt.scatter(sepal_length,sepal_width)
plt.show()


### Algorithm – Draw Scatter Plot of Sepal Length vs Sepal Width Using Iris Dataset

1. Start.
2. Import Matplotlib and Iris dataset.
3. Load the Iris dataset using `load_iris()`.
4. Extract sepal length values from the dataset.
5. Extract sepal width values from the dataset.
6. Draw a scatter plot using `plt.scatter()` with sepal length and sepal width.
7. Display the scatter plot using `plt.show()`.
8. Stop.