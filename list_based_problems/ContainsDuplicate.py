#Problem Statement

#Given an integer array nums, return:

#True if any value appears at least twice in the array.
#False if every element is distinct.
nums=list(map(int,input().split()))
class solution:
    def ContainsDuplicate(self,nums):
        n = len(nums)
        for i in range(n):
            for j in range(1+1,n):
                if nums[i]==nums[j]:
                    return True
        return False
    
sol = solution()
print(sol.containsDuplicate(nums))