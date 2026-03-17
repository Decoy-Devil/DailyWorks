"""Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time."""

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

nums = [100, 4, 200, 1, 3, 2,7,6,4,3,7,8,9,0,1]
#
# we are checking for longest snake found
# 2 approach : look for head continuity
count, cur_order = 0 , 0

for i in range(len(nums) -1 ):
    print("comparing => ",nums[i],"and ", nums[i + 1])
    if (nums[i] < nums[i+1]):
        cur_order += 1
        print("true")
        if (cur_order > count):  # assign count with cur order if cur order is big
            count = cur_order
            print("count incremented to ___________ ", count)
        # print(cur_order, nums[i], nums[i+1] )
    else:
        print("false", cur_order)
        cur_order = 0




print(count+1)


        # cur_order

# 1 approach : look for the tail




""" example: 
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
 Therefore its length is 4.
 
 Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109 """


# ______________________brute____force___________________
# nums = [1, 2, 3, 4, 100, 200] # sorted array
# count = 0
#
#
# for i in range(len(nums) - 1):
#     if (nums[i+1] > nums[i]):  # out of bounds error handling with range -1
#         count += 1
#         print( nums[i] ,count)
#     else:
#         count = 0
#
# print("final count = ", count +1 )
# # return (count +1)
