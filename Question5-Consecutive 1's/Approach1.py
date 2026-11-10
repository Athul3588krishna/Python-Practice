filename = input("Enter file name: ")

f = open(filename, "r")

for line in f:
    if "11" in line:
        print("Consecutive 11 is:", line)

f.close()