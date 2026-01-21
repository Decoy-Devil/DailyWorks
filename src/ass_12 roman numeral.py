# Roman numeral equivalent
"""For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.
Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.
For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output."""

from random import randint
# x = randint(1,10)
x = int(3)

if x == 10:
    print(x, " X")
elif x == 9:
    print(x, "is IX")
elif x == 8:
    print(x, " VIII")
elif x == 7:
    print(x, " VII")
elif x == 6:
    print(x, " VI")
elif x == 5:
    print(x, " V")
else:
    print("The roman numeral equivalent of " + str(x) + " is to I")



# doing ascending logic
# else:
#     if x >= 6:
#         if x == 6:
# #             print("XI")



"""
doing linear search, sequential search 

if x == 10:
    print(x, "X")
elif x == 9:
        print(x, "IX")
elif (x == 8):
        print(x, "VIII")
elif (x == 7):
        print(x, "VII")
elif (x == 6):
        print(x, "Vi")
elif (x == 5):
        print(x , "V")
elif (x == 4):
        print(x, "IV")
elif (x == 3):
        print(x, "III")
elif (x == 2):
        print(x, "II")
elif (x == 1):
        print(x, "I")
else:
    print(x)

"""


"""

#doing descending
if x == 10:
    print( x, "X")
else:
    if x == 9:
        print( x, "IX")
    else:
        if x == 8:
            print( x, "VIII")
        else:
            if x == 7:
                print( x, "VII")
            else:
                if x == 6:
                    print( x, "VI")
                else:
                    if x == 5:
                        print( x, "V")
                    else:
                        if x == 4:
                            print( x, "IV")
                        else:
                            if x == 3:
                                print( x, "III")
                            else:
                                if x == 2:
                                    print( x, "II")
                                else:
                                    if x == 1:
                                        print( x, "I")
                                    else:
                                        print("out of bounds")





"""