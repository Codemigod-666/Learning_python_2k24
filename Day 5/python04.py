# range
# total = 0
# for i in range(101):
#     total += i
#
# print(total)


# write a program to write calculate the sum of all the  even number between 1 , 100

total = 0
limit = int(input("Enter the limit upto which you want to calculate the even sum: "))

for i in range(0, limit + 1, 2):
    total += i

print(f"The sum of all the even numbers from 1 to 100 is : {total}")
