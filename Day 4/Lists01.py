fruits = ["apple", "banana"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # banana
print(fruits[-2]) # apple

# see the positive index
# also see the negative index

fruits.extend((["mango", "grapes"]))
print("\n")
for i in fruits:
    print(i)
