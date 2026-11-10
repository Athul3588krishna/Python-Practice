from datetime import datetime

d1 = input("Enter first date (dd-mm-yyyy): ")
d2 = input("Enter second date (dd-mm-yyyy): ")

date1 = datetime.strptime(d1, "%d-%m-%Y")
date2 = datetime.strptime(d2, "%d-%m-%Y")

if date1 < date2:
    print("Earlier date:", d1)
else:
    print("Earlier date:", d2)