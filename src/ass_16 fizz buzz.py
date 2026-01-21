# x = 9
# y = 0

# while (x < 51):
#     print(x)
#     x += 1
# y = x//3
#
#  if (== 0):
#      print("FizzBuzz")


# Write a program that iterates over the integers 1 through 50 using a loop.
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.
# For example, 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz".  For numbers which are multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.  For the numbers that are multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.
# All of the integers which are not multiples of 3 or 5 should just be printed as themselves.

# example:
# 42 by 3 fizz
# 20 by 5 buzz
# 15 by 3,5 fizzbuzz


# x = int(input("number"))
# x = range(5)
# x = 50
# r = 0
# # y = x % 3
# # z = x % 5
#
# while (x > 0):
#     y = x % 3
#     z = x % 5
#
#
#     if y == 0:
#         print("Fizz", x)
#         r += 1
#     if z ==0:
#             print("buzz", x)
#             r += 1
#     if (r == 2):
#         print("FuzzBuzz")
#     else:
#         print(x)
#
#     x = x - 1
#     r = 0

# print(42%5)

# -----------------------------

# Write a program that iterates over the integers 1 through 50
# using a loop. # However, for numbers which are multiples of both 3
# and 5 print “FizzBuzz” in the output. For example, 15 is divisible
# by both 3 and 5, so instead of printing 15, print "FizzBuzz".
# For numbers which are multiples of 3 but not 5 (such as 42)
# print “Fizz” instead of the number.  For the numbers that are
# multiples of 5 but not 3 (such as 20) print “Buzz” instead of
# the number. # All of the integers which are not multiples of 3
# or 5 should just be printed as themselves.



x = 15 # x = int(input("enter int"))
while x > 0:



    if(x % 5 == 0 and x % 3 == 0 ):
        print("FizzBuZZ", x)
    elif x % 3 == 0:
        print("Fizz", x)
    elif x % 5 == 0:
        print("Buzz", x)
    else:
        print(x)
    x -= 1