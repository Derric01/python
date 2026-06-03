target=int(input())
nums=list(map(int, input().split()))
class solution:
           def twosum(self,nums,target):
            n=len(nums)
            for i in range(n):
               for j in range(i+1,n):
                   if nums[i]+nums[j]==target:
                        return [i,j] 

sol = solution()
print(sol.twosum(nums,target))

