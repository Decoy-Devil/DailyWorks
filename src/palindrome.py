x = int(input("enter something"))
print(x)
# we translate the int to str for loop iteration
s = str(x)
left = 0
right = 0
# 121
for i in range(len(s)):
    #print(i)
    print(s[i])
left = i
right = len(s) - 1 - i
sleft = s[left]
sright = s[right]
print(sleft, "printing sLeft")

if (sleft != sright):
    print("not equal ", sleft)

if (x < 0):     # not able to handle negative palindrome
    print(x , "is negative")

