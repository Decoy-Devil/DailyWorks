# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
#

# talking about set

# 5 in s

# s = set([1,17,3,1])
# s = set([1,3,2,4,5,1,1])
s = {1,3,2,4,5,1,1}
# s.add(8)
# s.remove(1)
# s.discard(4)
print (s)
# print (5 in s)

for value in s: # for i in len(s):
  print( value in s, value)  # i will always start from 0

# print(s.remove(2), "2 removed")
print(s)
print(1 in s)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# nums = [1, 2, 3, 3, 4, 2]
nums = [1]
s = set()

print(len(nums))
if (len(nums) <= 1):    # () is a list not an array, [] isnt array too but can be a empty set,
    print ("worked")

for x in nums:
    if x in s:
        print(x, "true")
        exit(x in s)
    else:
        s.add(x)
        print(x, "false")
# ~~~~~~~~~~~~~~~~~~~~~~
class Solution(object):
    def containsDuplicate(self, nums):
        # nums = [1, 2, 3, 3, 4, 2]
        s = set()

        if (len(nums) <= 1):    # () is a list not an array, [] isnt array too but can be a empty set,
            return("false")
        for x in nums:
            if x in s:
                print(x, "true")
                return(x in s)
            else:
                s.add(x)
                print(x, "false")
