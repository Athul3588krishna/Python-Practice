import matplotlib.pyplot as plt


roll_no=list(map(int,input("Enter roll no:").split()))
marks=list(map(int,input("Enter marks no:").split()))

plt.scatter(roll_no,marks,color='green')
plt.show()

### Algorithm – Draw Scatter Plot of Roll Numbers vs Marks

1. Start.
2. Import the Matplotlib library.
3. Read roll numbers from the user.
4. Read student marks from the user.
5. Convert the input values into integer lists.
6. Draw a scatter plot using `plt.scatter()` with roll numbers and marks.
7. Display the scatter plot using `plt.show()`.
8. Stop.