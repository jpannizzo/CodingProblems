from typing import List
class SimpleSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = ""
        start = 0
        stop = 1
        counter = 0
        while counter < len(strs):
            if counter == 0:
                prefix += strs[counter][start:stop:1]
            if prefix != strs[counter][0:stop:1]:
                return prefix[0:stop-1:]
            counter +=1
            
            if counter == len(strs) and len(strs) > 1:
                start +=1
                stop +=1
                counter = 0

        return prefix

sol = SimpleSolution()

strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(sol.longestCommonPrefix(strs))
strs = []
print(sol.longestCommonPrefix(strs))
strs = [""]
print(sol.longestCommonPrefix(strs))
print("Simple Solution Finished\n")

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix
        
        for i in zip(*strs):
            if len(set(i)) == 1:
               prefix += i[0]
            else:
               return prefix
            
        return prefix
           
sol = Solution()

strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(sol.longestCommonPrefix(strs))
strs = []
print(sol.longestCommonPrefix(strs))
strs = [""]
print(sol.longestCommonPrefix(strs))