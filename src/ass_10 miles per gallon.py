from random import  randint
F = randint(10,25) # max liter gas a vehicle holds
M = randint(250 ,400) # miles can travel on full tank

# MPG = miles driven / gallons used
print(str(F) + " is the total gallons of gas car's feul tank can hold")
print(str(M) + " is the miles it can travel on a full tank")
print("Miles per gallon MPG is " + str(M//F)) # print(mpg with floor division)

# M = gallons of gas in the car's fuel tank
#   miles = miles it can travel on a full tank

# print(5//2) floor division

