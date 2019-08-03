class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return
        res = maxn = minn = nums[0]
        for num in nums[1:]:
            if num < 0:
                maxn, minn = minn, maxn
            maxn = max(maxn*num, num)
            minn = min(minn*num, num)
            res = max(maxn, res)
        return res