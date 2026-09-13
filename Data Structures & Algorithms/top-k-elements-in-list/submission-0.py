class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for index in range(len(nums)):
            if nums[index] not in count_map:
                count_map[nums[index]] = 1
            else:
                count_map[nums[index]] = count_map.get(nums[index]) + 1

        count_map_desc = dict(sorted(count_map.items(), key=lambda item: item[1], reverse=True))
        keys = list(count_map_desc)
        answer = []
        for index in range(k):
            answer.append(keys[index]) 
        
        return answer