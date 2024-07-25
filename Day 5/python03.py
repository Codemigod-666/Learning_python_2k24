# You are going to write a program that calculates the highest score from a list of scores.
# going advance in this thing::::::::::::::::::::::::::::


n = int(input("Enter the Number of scores: "))
scores = []


# 'range' is the keyword we use when we want to run the loop independent of the list:
# we can run the loop just as many times as we wants with just defining the range....


for _ in range(n):
    while True:
        try:
            num = int(input(f"Enter score {_ + 1}: "))
            scores.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


highest_score = -1
#
for score in scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")


