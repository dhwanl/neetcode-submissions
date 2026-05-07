class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hint 1: O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    vals = []
                    vals.append(i)
                    vals.append(j)
                    return vals