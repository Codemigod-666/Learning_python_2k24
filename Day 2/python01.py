# Goals: Data Types, Numbers, Operations, Type conversions and f-strings
# -------------------------- Date Types -----------------------------------------------
#            int
#            str
#            float
#            complex
#            list Mutable
#            tuple
#            range
#            dict Mutable
#            set Mutable
#            frozenset
#            bool
#            bytes
#            bytearray
#            memoryview
#            NoneType

# STRING ===============================

# "Hello World"
print("Hello"[0])
# OP:  H
print("124" + "567")
# OP:  124567
print("hello"+" "+"world")
# OP:  hello world


# Integer DATATYPE ============================

print(124+345)
# OP: 469

print(124_234_434)
# 124234434


# FLOAT DATATYPE

a = 3.23231
print(a)
# OP: 3.23231


# BOOLEAN DATATYPE

a = True
b = False
print(a, b)

# ------------------- type conversion ----------------------

# num_char = len(input("Enter your name"))
# print("There are " + num_char + " characters in the name")
# the above line will give the error
# print("There are " + str(num_char) + " characters in the string")
# here you have typecasted the variable from integer to string


# ----------------------- day 2 challenge --------------------
# write a program that adds the digits in a 2-digit number. e.g. If the input
# was 35, then the output should be 3+5 = 8........

two_digit_number = input("Enter a two digit number")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# ------------------------ Operations ----------------------

# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

