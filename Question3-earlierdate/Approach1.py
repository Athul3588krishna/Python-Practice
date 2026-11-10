from datetime import datetime
d1=input("Enter date 1 : ")
d2=input("Enter date 2: ")

date1=datetime.strptime(d1,"%d-%m-%Y")
date2=datetime.strptime(d2,"%d-%m-%Y")

if date1<date2:
    print("earlier date is ",date1.strftime("%d-%m-%Y"))
else:
    print("earlier date is ",date2.strftime("%d-%m-%Y"))


### Algorithm – Find the Earlier Date

1. Start.
2. Read two dates from the user.
3. Convert both dates into date objects using `strptime()`.
4. Compare the two dates.
5. If the first date is smaller, display the first date as the earlier date.
6. Otherwise, display the second date as the earlier date.
7. Stop.