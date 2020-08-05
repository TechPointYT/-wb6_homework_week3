class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bot = 0
        top = len(nums)-1
        while bot <= top:
            
            mid = bot + (top - bot) // 2
            print(f"bott {bot} mid {mid} top {top} ")
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                bot = mid + 1
            elif nums[mid] > target:
                top = mid - 1
        return -1
            
