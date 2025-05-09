from typing import List

class Powerset:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int])->List[List[int]]:
        '''
            This works in the following way for example [1,2]
                Start:    [] → Save it
                    - this is due to backtrack(0, []) which creates the empty set. This empty set instantly gets saved
                Add 1 →   [1] → Save it
                    - this is the 1st element in nums. It appends to an empty list and calls backtrack so it instantly gets saved
                Add 2 →   [1, 2] → Save it
                    - this is the 2nd element in nums. It appends to [1] and calls backtrack so it instantly gets saved
                Pop →     [1]     → undo 2
                    - i = 2 which is <= start (2) but it is not < len(nums) so we skip the loop and continue from the 2nd backtrack call which then pops the last element off the list.
                Pop →     []      → undo 1
                    - Continue from the 1st backtrack call which pops the first element off the stack
                Add 2 →   [2]     → Save it
                    - i = 1 and appends the 2nd element in nums to an empty list
                Pop →     []      → undo 2
                    - i = 2 which is <= start (2) but it is not < len(nums) so we skip the loop and pop after the only backtrack call
                    - this ends the recursion
        '''
        def backtrack(start, path: List[int]):
            # add copy of current subset(path) to result
            # this list is constantly updated and added to self.result to create the next subset
            self.result.append(path[:])

            # this loop only runs when i <= start < len(nums). range(start,stop,step) so i <= start and i < stop
            # when i = len(nums) the loop is skipped and we resume from the last call of backtrack(i + 1, path)
            for i in range(start, len(nums)):
                path.append(nums[i])
                # this itterates to the next element in the list
                backtrack(i + 1, path)
                # every recursive call to backtrack has a corresponding pop so that all items are removed and the next
                path.pop()

        backtrack(0, [])
        return self.result
        

ps = Powerset()
print(ps.subsets([1,2]))
print(ps.subsets([1,2,3,4,5]))