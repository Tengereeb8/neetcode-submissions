class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  
        
        # Step 1: Calculate Prefix products
        # 'prefix' keeps track of the product of all elements seen so far from the left
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate Suffix products
        # 'suffix' keeps track of the product of all elements seen so far from the right
        suffix = 1
        for i in range(n - 1, -1, -1): # Moving backwards from the end
            res[i] *= suffix
            suffix *= nums[i]
            
        return res