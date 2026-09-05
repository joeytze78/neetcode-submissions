class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_list = []
        for element in operations:
            if element == "+":
                new_list.append(new_list[-2] + new_list[-1])
            elif element == "C":
                new_list.pop()
            elif element == "D":
                new_list.append(new_list[-1]*2)
            else:
                new_list.append(int(element))
        
        return sum(new_list)