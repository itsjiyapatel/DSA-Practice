# def backtrack(start, path):
    # 1. Save the current path
    # 2. Iterate from 'start' to end
    #     a. Include current element
    #     b. Recurse
    #     c. Backtrack (remove last element)
#Q1. Subsets
from typing import List

class Solution:
    def subsets(self,nums):
        result=[]
        def backtrack(start,subset):
            result.append(subset[:])
            for i in range(start,len(nums)):
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return result
    
sol=Solution()
nums=[1,2,3]
print(sol.subsets(nums))

#Q2. Combination Sum
class Solution:
    def combinationSum(self,nums,target):
        result=[]
        def backtrack(start,path,length):
            if length==0:
                result.append(path[:])
                return
            if length<0:
                return
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i,path,length-nums[i])
                path.pop()
        backtrack(0,[],target)
        return result

sol=Solution()
nums = [3,4,5]
target=16
print(sol.combinationSum(nums,target))

#Q3. Combination sum II
class Solution:
    def combinationSum2(self,nums,target):
        nums.sort()
        result=[]

        def backtrack(start,path,length):
            if length==0:
                result.append(path[:])
                return
            if length<0:
                return 
            
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(i+1,path,length-nums[i])
                path.pop()
        backtrack(0,[],target)
        return result
    
sol = Solution()
candidates = [9,2,2,4,6,1,5]
target = 8
print(sol.combinationSum2(candidates, target))

#Q4. Permutations
class Solution:
    def permute(self,nums):
        result=[]
        def backtrack(path,remaining):
            if not remaining:
                result.append(path)
                return 
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return result
    
sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))

#Q5. Subsets 2

class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()  

        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack

        backtrack(0, [])
        return result

sol = Solution()
nums = [1, 2, 1]
print(sol.subsetsWithDup(nums))


#Q6 Word Search
class Solution:
    def exists(self,board,word):
        rows,columns=len(board), len(board[0])
        visited=set()

        def backtrack(r,c,i):
            if i==len(word):
                return True
            if ( r<0 or c<0 or r>=rows or c>=columns or word[i]!=board[r][c] or (r,c) in visited):
                return False
            
            visited.add((r,c))
            res = (backtrack(r+1, c, i+1) or
                   backtrack(r-1, c, i+1) or
                   backtrack(r, c+1, i+1) or
                   backtrack(r, c-1, i+1))
            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(columns):
                if backtrack(r, c, 0):
                    return True
        return False
    
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"

sol=Solution()
print(sol.exists(board,word))

#Q7. Palindrome partioning
class Solution:
    def partition(self,s):
        result=[]

        def isPalindrome(word):
            return word==word[::-1]
        
        def backtrack(start, path):
            if start==len(s):
                result.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                if isPalindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result
s = "aab"
sol=Solution()
print(sol.partition(s))

#Q8. Letter Combinations of Phone No.
class Soltuion:
    def letterCombo(self,digits):
        if not digits:
            return []
        
        phone_map={
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result
digits = "34"
sol=Soltuion()
print(sol.letterCombo(digits))