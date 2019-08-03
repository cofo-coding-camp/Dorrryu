class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in nums_dict:
                return [nums_dict[remain], idx]
            nums_dict[num] = idx
        return []