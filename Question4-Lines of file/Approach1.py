f=open("samplee.txt","r")
lines=f.readlines()
print("The number of lines",len(lines))
f.close

### Algorithm – Count the Number of Lines in a File

1. Start.
2. Open the file in read mode.
3. Read all lines from the file using `readlines()`.
4. Count the number of lines using `len()`.
5. Display the total number of lines.
6. Close the file.
7. Stop.