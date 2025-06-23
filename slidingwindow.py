#Q1. best time to buy and sell stock
class Solution():
    def maxProfit(self,prices):
        n=len(prices)
        left=0
        max_profit=0
        for right in range(1,n):
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                max_profit=max(max_profit,profit)
            else:
                left=right
        return max_profit
sol=Solution()
prices = [10,1,5,6,7,1]
print(sol.maxProfit(prices))

#Q2. longest substring without repeating characters
class Solution():
    def lengthOfLongestSubstring(self, s: str):
        char_set=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len
sol=Solution()
s = "zxyzxyz"
print(sol.lengthOfLongestSubstring(s))

#Q3. longest repeating character replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0  # Left pointer of the sliding window
        max_len = 0  # To store the maximum length of the valid window
        char_count = {}  # Dictionary to store frequency of characters in the window
        max_freq = 0  # To store the frequency of the most frequent character in the window

        for right in range(len(s)):
            # Increase the frequency of the current character
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            # Update the frequency of the most frequent character in the current window
            max_freq = max(max_freq, char_count[s[right]])

            # If the number of characters to replace exceeds k, shrink the window
            if (right - left + 1) - max_freq > k:
                # Decrease the frequency of the character at the left pointer and move left pointer
                char_count[s[left]] -= 1
                left += 1

            # Calculate the maximum length of the valid window
            max_len = max(max_len, right - left + 1)

        return max_len
sol=Solution()
s = "AAABABB"
k = 1
print(sol.characterReplacement(s,k))

#Q4. permutation in a string
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x,y=len(s1),len(s2)
        if x>y:
            return False
        s1_count=Counter(s1)
        window_count=Counter()
        for i in range(y):
            window_count[s2[i]]+=1
            if i>=x:
                left_char=s2[i-x]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1

            if window_count == s1_count:
                return True
        
        return False
sol=Solution()
s1 = "abc"
s2 = "lecabee"
print(sol.checkInclusion(s1,s2))

#Q5. minimum window substring
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        l,r=0,0
        formed=0
        window_counts={}
        ans = float("inf"), None, None
        while r<len(s):
            character=s[r]
            window_counts[character]=window_counts.get(character,0)+1
            if character in dict_t and window_counts[character]==dict_t[character]:
                formed+=1
            while l<=r and formed==required:
                character=s[l]
                if r-l+1<ans[0]:
                    ans=(r-l+1,l,r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1  # Contract from the left

            r += 1  # Expand from the right

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

#Q6. Sliding Window Maximum
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []

        deq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            while deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove elements smaller than current nums[i] from the right of deque
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            # Starting from i >= k-1, append the max for the current window
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result
sol=Solution()
nums = [1,2,1,0,4,2,6]
k = 3
print(sol.maxSlidingWindow(nums,k))