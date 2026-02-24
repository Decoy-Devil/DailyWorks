def find_left(nums, target):
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
        if nums[mid] == target:
            ans = mid
    return ans

def find_right(nums, target):
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1
        if nums[mid] == target:
            ans = mid
    return ans

def search_range(nums, target):
    return [find_left(nums, target), find_right(nums, target)]

if __name__ == "__main__":
    print(search_range([5,7,7,8,8,8], 8))  # [3,4]
    print(search_range([5,7,7,8,8,10], 6))  # [-1,-1]

    
