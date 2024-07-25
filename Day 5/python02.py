# you are going ro write a program  that calculates the average student height from a list of heights:

student_height = [100, 133, 133, 124, 143, 145, 152, 122, 131]

# the average height can be calculated by adding all the heights together and dividing by the total number of heights

height_sum = 0
for height in student_height:
    height_sum = height_sum + height

average_height = height_sum / len(student_height)
print("The average height is : ", round(average_height, 2))
