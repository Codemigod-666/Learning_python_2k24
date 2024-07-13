# Write a program that works out whether if a given year is a leap
# A normal year has 365 days, leap years have 366, with an extra day in February.

year = int(input("Enter the year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")

else:
    print("Not Leap Year")
