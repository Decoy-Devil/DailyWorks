import sys

nums = [1,2,3,1]
# n =
a = b = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        # n = 1 + j
        if nums[i] == nums[j] and i != j :
            a += 1
            print("true", nums[i], "=", nums[j])
            sys.exit()    # // return <> exits the function not the program // but leet code doesnt want sys.exit
        else:
            b += 1
            print("false", nums[i],  nums[j])

