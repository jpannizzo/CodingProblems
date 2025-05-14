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

def max_sum2(nums: List[int], k: int) -> int:
    compare_num = 0
    max_num = 0
    left = 0

    for right in range(len(nums)):
        compare_num += nums[right]

        if right >= k:
            compare_num -= nums[left]
            left += 1

        # print(compare_num)

        max_num = max(max_num, compare_num) 

    return max_num 

print(max_sum2([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))