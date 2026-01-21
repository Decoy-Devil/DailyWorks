# def hello_world_printer():
#     print("hello world")
#
# hello_world_printer()

# -------
# def name_printer(name):
#     name = input("enter name")
#     print(name)
#
#
# name_printer(name="damn")
# ------
# def name_printer (y):
#     print(y)
#
# name = input("Enter your name")
# name_printer(name)

# --------
# goal to calculate the volume of prism

# length = int(input("give length"))
# width = int(input("give width"))
# height = int(input("give height"))

def func_f3(length,width,height):
    vol = length * width * height
    return vol

y = func_f3( length =int(input("give length")), width = int(input("give width")),height = int(input("give height")))
print("The volume of the rectangular prism is "+ str(y))



"""
Do all of this in a .py file in Pycharm.
For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h where l, w, and h are length, width, and height, respectively.
First, create three variables representing length, width, and height.   Assign each of them an integer as user input using the input() function and int().
Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters representing length, width, and height and return the volume of a rectangular prism calculated using those 3 parameters.
Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.  You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.
"""
