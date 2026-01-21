def Alternate_print (arr):
    if(len(arr) == 0):
        print("array is empty")
        return # note to explicity exit the function
    x = 0
    y = len(arr) - 1
    # print ("printing initial", x, y, len(arr))
    while (x <= y):
        if (x != y):
            print(arr[x],arr[y])
        else:
            print(arr[x])
        x += 1
        y -= 1



        # test cases ~~ empty/0 , single , odd , even, max limits




# TEST CASES
# arr = [10,11,12,13,14]
# arr = []
# arr = [1]
# arr = [2,3,4]
# arr = [6,7]
# arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
arr = ['a','b','c','d','e']

print(arr)
Alternate_print (arr)

# very tiny no. of ppl will think of the test cases while writing

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# why did it handled char array without code change,
# python doesnt have char, it treats array of int and char as objects of strings, follows duck typing to handle all types of sequences
# how its handling datatypes ?????
# will check later