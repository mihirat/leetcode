class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_rev = nums[::-1]
        for i, num in enumerate(nums_rev):
            for j, pair in enumerate(nums):
                if i + j == len(nums) -1:
                    break
                if num + pair == target:
                    return [j, len(nums) - i - 1]
