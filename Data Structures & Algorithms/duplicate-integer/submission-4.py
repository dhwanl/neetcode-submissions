class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        vals = []
        while (i < len(nums)):
            if (nums[i] in vals):
                return True
            vals.append(nums[i])
            i += 1
        return False