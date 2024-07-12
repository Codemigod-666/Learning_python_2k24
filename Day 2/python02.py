# create a program using  maths and f-string that tells us how many
# weeks we have left, iff  we live until 90 years old
# it will take your current age as the input and output a message
# with our time left in this format
# You have x weeks left.

age = input()
years = 90 - int(age)
# now each year have 52 weeks therefore
weeks = years * 52
print(f"You have {weeks} weeks left.")


# print(int(2.7))
# output 2