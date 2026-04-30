class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_of_nums={}
        for num in nums:
            if num in count_of_nums:
                count_of_nums[num]+=1
            else:
                count_of_nums[num]=1
        
        sorted_keys = sorted(count_of_nums, key=count_of_nums.get, reverse=True)
        return sorted_keys[:k]



