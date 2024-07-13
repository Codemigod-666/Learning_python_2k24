import random

names_list = input("Enter the names: ")
list = names_list.split(',')

index = random.randint(0, (len(list) - 1))
print(f" {list[index]} is going to buy meal today!!")
