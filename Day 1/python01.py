def solution(i):
    print(i)

if __name__ == '__main__':
    # EXERCISE 01 (LECTURE 08)
    # 1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
    # 2. Knead the dough for 10 minutes.
    # 3. Add 3g of Salt.
    # 4. Leave to rise for 2 hours.
    # 5. Bake at 200 degrees C for 30 minutes.

    print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
    print("2. Knead the dough for 10 minutes.")
    print("3. Add 3g of Salt.")
    print("4. Leave to rise for 2 hours.")
    print("5. Bake at 200 degrees C for 30 minutes.")
    print("\n")

    # HOW TO USE QUOTES IN STRING USING ESCAPE CHARACTER
    print("A 'single quote' inside a double quote")
    print('A "double quote" inside a single quote')
    print("Alternatively you can just \"escape\" the quote")

    # STRING MANIPULATION (LECTURE 09)
    print("Hello world! \nHello World!")
    # Concatenation (in python spaces are important)
    print("Hello" + " " + "Rishi")

    # INPUT FUNCTION
    name = input("What is your name? ")
    print("Entered name is", name)
    # another way
    print("Hello " + input("What is you name?") + "!")
