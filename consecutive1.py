f=open("sample.txt","r")
for line in f:
    if "11" in line:
        print(line.strip())
f.close()
