arr = [10,11,12,13,14,15]
# __________________________ for forward
# i = 10
# # for value in arr
#
# for i in arr:  ## current learning : i is not index, but i is value
#     print(i)

# __________________________ for reverse


# i = len (arr) - 4
i = 14
print ("printing first i as = ", i)
x = 0

for i in arr: # going outbound as i isnt indexing but is a value that doesnt exits
    # i = i - 1  ## python is taking control over i and doesn't allow operations over i
    print(arr[x])
    print(arr)
    i -= 1

    print ("printing new i",i)
    # if (i <= 0):
    #     exit()

# constraint language cannot be done from for loop ##### _________________-