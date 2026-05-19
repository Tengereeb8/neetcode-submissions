class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newNums=set(nums)
        return len(newNums)!=len(nums)
        