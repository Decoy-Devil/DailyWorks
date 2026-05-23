def maxArea(heights):
        n = len(heights)
        max_area = l = 0
        r = n - 1

        while (l < r):
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            max_area = max(max_area, a)

            if (heights[l] < heights[r]):
                l += 1

            else:
                r -= 1
        return max_area

height = [1, 4, 6, 7, 8, 4, 4, 3, 2]
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))



"""
Container With Most Water
{You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).}

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1




"""