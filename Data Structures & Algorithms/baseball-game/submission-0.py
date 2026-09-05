class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def plus(num1: int, num2: int):
            return str(num1+num2)
        
        def d(num: int):
            return str(2*num)

        def c(arr: list[str]):
            return arr.pop()
        
        new_list = []
        for element in operations:
            if element == "+":
                new_list.append(plus(int(new_list[-2]), int(new_list[-1])))
            elif element == "C":
                c(new_list)
            elif element == "D":
                new_list.append(d(int(new_list[-1])))
            else:
                new_list.append(element)
        sum = 0
        for element in new_list:
            sum += int(element) 
        return sum