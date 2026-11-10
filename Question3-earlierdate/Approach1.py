from datetime import datetime
d1=input("Enter date 1 : ")
d2=input("Enter date 2: ")

date1=datetime.strptime(d1,"%d-%m-%Y")
date2=datetime.strptime(d2,"%d-%m-%Y")

if date1<date2:
    print("earlier date is ",date1.strftime("%d-%m-%Y"))
else:
    print("earlier date is ",date2.strftime("%d-%m-%Y"))
