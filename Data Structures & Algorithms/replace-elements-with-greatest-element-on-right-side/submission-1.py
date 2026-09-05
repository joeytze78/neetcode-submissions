class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output_arr = arr[:]
        
        for index in range(len(output_arr)):
            if index == (len(output_arr)-1):
                output_arr[-1] = -1
            else:
                arr.pop(0)
                output_arr[index] = max(arr)

        return output_arr
