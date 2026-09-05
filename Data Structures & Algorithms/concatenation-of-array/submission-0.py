class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        for element in nums:
            ans.append(element)
        
        return ans