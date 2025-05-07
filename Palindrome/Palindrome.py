class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            x_reversed = int(str(x)[::-1])
        except ValueError:
            # Negative numbers can't be palindromes because -x != x-
            return False

        if x == x_reversed:
            return True
        
        return False

sol = Solution()

print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))
print("\n")

import math

class SolutionNoString:
    def isPalindrome(self, x: int) -> bool:  
        try:
            # get number of digits
            num_digits = int(math.log10(x)+1)
            # get 10^(number of digits)
            divisor = 10 ** (num_digits-1)
        except ValueError:
            # Negative numbers can't be palindromes because -x != x-
            return False
        
        while x > 0:
            last_digit = x % 10
            first_digit = x // (10 ** int(math.log10(x)))
            if first_digit != last_digit:
                return False
            x = x % divisor
            x = x // 10

        return True

sol = SolutionNoString()

print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))