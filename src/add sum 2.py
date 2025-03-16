
nums = [0,2,7,8,11]
target = 9
x = 0
y = 0
# print ('x is ',x)
while y != target:
    y = nums[x] + nums[x+1]
    # print('y is ', y)
    x =x+1


print ('Output:[',x-1,x,']')

# Output: [0,1]
# print ( 'nums 1 is ', nums[1] )
# print ( 'nums 0 is ', nums[0] )