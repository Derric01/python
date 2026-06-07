target=int(input())
nums=list(map(int,input().split()))

class Solution:
    def twosum(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []  # No pair found

sol = Solution()
print(sol.twosum(nums, target))