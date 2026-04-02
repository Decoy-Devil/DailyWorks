def three_sum_smaller(nums, target):
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n - 2): #
        left = i + 1
        right = n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            print(i, left, right)

            if s < target:
                # Since nums is sorted, nums[left+1..right] are <= nums[right]
                # So (i, left, k) is valid for all k in [left+1, right]
                count += (right - left)
                print(right, left ,"R-L= C" ,count)
 
                left += 1 # if sum is small, increase left
            else:
                right -= 1 # if sum is large, decrease right

    return count


# Example tests
if __name__ == "__main__":
    print(three_sum_smaller([-2, 0, 1, 3,8], 13))          # 2
    # print(three_sum_smaller([0, 0, 0], 1))              # 1  (only one triplet)
    # print(three_sum_smaller([3, 1, 0, -2], 4))          # try it