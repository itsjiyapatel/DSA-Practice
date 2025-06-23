# #Q1. Valide Palindrome
class Solution:
    def isPalindrome(self,s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned==cleaned[::-1]
    
sol=Solution()
s = "Was it a car or a cat I saw?"
print(sol.isPalindrome(s))

#Q2. Three sum
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]

                if total==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1
                
                elif total<0:
                    left+=1
                else:
                    right-=1
        return res

sol=Solution()
nums = [0,0,0]
print(sol.threeSum(nums))

#Q3. Container with most water
class Solution:
    def maxArea(self, heights):
        left=0
        right=len(heights)-1
        max_water=0
        while left<right:
            height=min(heights[left],heights[right])
            width=right-left
            max_water=max(max_water,height*width)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water
    
sol=Solution()
height = [1,7,2,5,4,7,3,6]
print(sol.maxArea(height))

#Q4. two sum II
class Solution:
    def twoSum(self, nums,target):
        left=0
        right=len(nums)-1
        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                return [left+1,right+1]
            elif total<target:
                left+=1
            else:
                right-=1

        return []

sol = Solution()
numbers = [1,2,3,4] 
target = 3
print(sol.twoSum(numbers, target))

#Q5. Trap raining water
class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped_water = 0

        while left<right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                
                else:
                    trapped_water += left_max - height[left]
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water

sol=Solution()
height = [0,2,0,3,1,0,1,3,2,1]
print(sol.trap(height))