# print("Welcome to the tip calculator")
# a = input("What was the total bill? ")
# b = input("How much tip would you like to give? 10, 12 or 15? ")
# c = input("How many people to split the bill?")
# print("Each person should pay: ", a)


# BMI calculator
weight = input("Enter the weight: ")
height = input("Enter the height: ")

weight_in_int = int(weight)
height_in_float = float(height)

# This is the use of f-String

bmi = weight_in_int / (height_in_float ** 2)
print(f"The BMI is {bmi}")
