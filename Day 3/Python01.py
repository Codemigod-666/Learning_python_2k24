# CONDITIONAL STATEMENTS
print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Your can ride the rollercoaster!!")
    print("Welcome to ticket counter")
    age = int(input("Enter you age"))

    if age < 12:
        print("Child tickets are $5")
    elif age <= 18:
        print("Youth tickets are $7")
    elif 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ride on us.")
    else:
        print("Adult tickets are $12")
else:
    print("Sorry, you have to grow taller before you can ride.")

# exercise
# write a program that works out whether if a given number is an odd or even number
#
# num = int(input("Enter a number: "))
# print("Even" if number % 2 == 0 else "Odd")
