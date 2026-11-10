filename = input("Enter file name: ")

f = open(filename, "r")

for line in f:
    if "11" in line:
        print("Consecutive 11 is:", line)

f.close()


### Algorithm – Retrieve Lines Having Two Consecutive 1's

1. Start.
2. Read the file name from the user.
3. Open the file in read mode.
4. Read the file line by line.
5. Check whether each line contains two consecutive 1's (`11`).
6. If found, display the corresponding line.
7. Close the file.
8. Stop.