# your code goes here
def longestCommonPrefix(nums):
 
        ans = ""
        nums = sorted(nums)  
        first = nums[0]  
        last = nums[-1] 
 
 
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans  
            ans += first[i]  
 
        return ans  
 
# Test cases
strs1 = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs1))        # fl
 
strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs2))        # <Empty List>
