class solution:
    def maxarr(self,nums):
        if not nums:
            return None
        max_num=nums[0]
        for num in nums:
            if num>max_num:
                max_num=num
        return max_num