class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i in range(len(nums)):
            for index_j in range(index_i+1, len(nums)):
                if nums[index_i] + nums[index_j] == target:
                    return [index_i, index_j]