from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            this_value = ""
            if i % 3 == 0:
                this_value = "Fizz"
            if i % 5 == 0:
                this_value += "Buzz"
            if not this_value:
                this_value = str(i)
            result.append(this_value)
        
        return result

sol = Solution()  
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(5))
print(sol.fizzBuzz(15))
print(sol.fizzBuzz(1))