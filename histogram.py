import matplotlib.pyplot as plt

marks = list(map(int, input("Enter marks: ").split()))

plt.hist(marks)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Student Marks Histogram")

plt.show()