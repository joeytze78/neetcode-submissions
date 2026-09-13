class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = nums[:]
        product = 1
        for i in range(len(nums)):
            answer[i] = product
            product = nums[i] * product

            # nums   = [1,2,4,6]
            # answer = [1,1,2,8]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * product
            product = nums[i] * product

            # nums   = [1,2,4,6]
            # answer = [48,24,12,8]
        return answer