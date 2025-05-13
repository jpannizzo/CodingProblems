from typing import List
def max_sum(nums: List[int], k: int):
    '''
    Given an array of integers and an integer k, return the maximum sum of any contiguous subarray of size k.

    Example:
    Input: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
    Output: 39 (because 10 + 23 + 3 + 1 = 37 is highest of any window of size 4)
    '''
    max_num = 0
    current_sum = 0
    left = 0

    print(nums)
    for right in range(len(nums)):
        if right < k:
            current_sum += nums[right]
            max_num = max(max_num, current_sum)
        else:
            current_sum -= nums[left]
            current_sum += nums[right]
            max_num = max(max_num, current_sum )
            left += 1
        # print(max_num)

    return max_num

print(max_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))