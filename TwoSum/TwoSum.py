from typing import List

class SimpleSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current_index = 0
        next_val = None

        while current_index < len(nums):
            current_val = nums[current_index]
            next_index = current_index+1
            while next_index < len(nums):
                next_val = nums[next_index]
                if target == current_val+next_val:
                    return [current_index,next_index]
                next_index+=1
            current_index+=1
        
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []


simsol = SimpleSolution()
sol = Solution()

test_case1 = [2,7,11,15]
target1 = 9
print(test_case1)
print(f"Target = {target1}")
print(f"test_case1: {simsol.twoSum(test_case1, target1)}")
print(f"test_case1: {sol.twoSum(test_case1, target1)}", end="\n\n")

test_case2 = [3,2,4]
target2 = 6
print(test_case2)
print(f"Target = {target2}")
print(f"test_case2: {simsol.twoSum(test_case2, target2)}")
print(f"test_case2: {sol.twoSum(test_case2, target2)}", end="\n\n")

test_case3 = [3,3]
target3 = 6
print(test_case3)
print(f"Target = {target3}")
print(f"test_case3: {simsol.twoSum(test_case3, target3)}")
print(f"test_case3: {sol.twoSum(test_case3, target3)}", end="\n\n")

test_case4 = [3,4,9,6,4]
target4 = 8
print(test_case4)
print(f"Target = {target4}")
print(f"test_case4: {simsol.twoSum(test_case4, target4)}")
print(f"test_case4: {sol.twoSum(test_case4, target4)}", end="\n\n")


test_case5 = [3,5,1,4,-8]
target5 = 5
print(test_case5)
print(f"Target = {target5}")
print(f"test_case5: {simsol.twoSum(test_case5, target5)}")
print(f"test_case5: {sol.twoSum(test_case5, target5)}", end="\n\n")

test_case6 = [4, -2, 5, 0, 6, 3, 2, 7]
target6 = 1
print(test_case6)
print(f"Target = {target6}")
print(f"test_case5: {simsol.twoSum(test_case6, target6)}")
print(f"test_case5: {sol.twoSum(test_case6, target6)}", end="\n\n")

#failure case
test_case_fail = [0, 1]
target_fail = 2
print(test_case_fail)
print(f"Target = {target_fail}")
print(f"test_case5: {simsol.twoSum(test_case_fail, target_fail)}")
print(f"test_case5: {sol.twoSum(test_case_fail, target_fail)}")