class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for element in nums:
            if element != val:
                # edit the specific k index element to the element that is not "val"
                nums[k] = element 
                k += 1
        return k