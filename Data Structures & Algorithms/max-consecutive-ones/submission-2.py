class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        counter = 0
        max_counter = 0
        for i in nums: 
            if i == 1:
                if counter == 0:
                    counter += 1
                    prev = i
                elif counter > 0 and prev == 1:
                    counter += 1
                    prev = 1
            else: 
                counter = 0
                prev = i
            if counter > max_counter:
                max_counter = counter


        return max_counter

