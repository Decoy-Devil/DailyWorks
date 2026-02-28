# F = 1.8 * C +32

# y = float(input("enter the float"))
# print(y)

"""


F = 0
def Ffahren(y):
    F = float(1.8 * y + 32)
    print ("F before return is ",F)
    return F

y = int(input("enter a int for degree centigrade"))
print("The Fahrenheit equivalent of "+ str(y) +" degrees Celsius is " + str(Ffahren(y)))

"""
# i always have to lessen the code number of lines

y = int(input("enter a int for degree centigrade"))

def Ffahren(y):
    F = float(1.8 * y + 32)
    return (18 * y + 320) / 10


print("The Fahrenheit equivalent of "+ str(y) +" degrees Celsius is " + str(Ffahren(y)))
