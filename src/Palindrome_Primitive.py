arr = [10,11,12,13,14,15]
# print(arr[3])
# primitive straight array (not reverse)

i = 0
x = 1
y = len(arr) # out of bound (at end) index fixed by y = len -1, mistake y = len X !

while (i <= y - 1 ): # out of bound index fixed by y - 1 , mistake i <= y, where y exists but printing array y doesn't exist !
    print("printing i =", i ,"that is" , arr[i])
    i += 1
    x += 1

print("print finished")

