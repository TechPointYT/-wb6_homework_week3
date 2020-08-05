class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sums = 0
        for i in range(1,len(nums),2):
            cur_sum = min([nums[i], nums[i-1]])
            sums += cur_sum
        return sums
            
