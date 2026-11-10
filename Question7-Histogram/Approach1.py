import matplotlib.pyplot as plt

marks=[45,60,68,76,35,89,91]
bins=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(marks,bins=bins,edgecolor="black")
plt.xlabel("students")
plt.ylabel("intervals")
plt.title("Mark list")
plt.show()


### Algorithm – Draw Histogram of Student Marks

1. Start.
2. Import the Matplotlib library.
3. Initialize a list containing student marks.
4. Define the intervals (bins) for the histogram.
5. Draw the histogram using `plt.hist()` with the given marks and bins.
6. Add X-axis and Y-axis labels.
7. Add a title to the histogram.
8. Display the histogram using `plt.show()`.
9. Stop.