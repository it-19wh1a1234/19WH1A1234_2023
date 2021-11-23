class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in dict and dict[res] != i:
                return [i, dict[res]]
