if __name__ == "__main__":
    # This file is for python variables

    # simple program for example
    x = 5
    y = "John"
    print(x)
    print(y)

    # CASTING
    x = str(3)
    print(type(x))  # output <class 'str'> because it is not converted into string
    # type keyword is used to get the data type

    # RULES FOR VALID VARIABLE NAMES:

    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.

    # types of variables

    # x = 20                                           # int
    # x = "Hello World"                                # str
    # x = 20.5                                         # float
    # x = 1j                                           # complex
    # x = ["apple", "banana", "cherry"]                # list Mutable
    # x = ("apple", "banana", "cherry")                # tuple
    # x = range(6)                                     # range
    # x = {"name": "John", "age": 36}                  # dict Mutable
    # x = {"apple", "banana", "cherry"}                # set Mutable
    # x = frozenset({"apple", "banana", "cherry"})     # frozenset
    # x = True                                         # bool
    # x = b"Hello"                                     # bytes
    # x = bytearray(5)                                 # bytearray
    # x = memoryview(bytes(5))                         # memoryview
    # x = None                                         # NoneType