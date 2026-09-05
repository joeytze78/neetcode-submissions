class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            # closing(key) : opening(value)
            ")": "(",
            "}": "{",
            "]": "[",            
        }

        # opening  opening closing
        new_list = []
        for element in s:
            if element in bracket_dict.values():
                new_list.append(element)
            elif element in bracket_dict.keys():
                if len(new_list) > 0:
                    match_open = bracket_dict[element]
                    if match_open != new_list.pop():
                        return False
                else:
                    return False
        if len(new_list) == 0:
            return True
        else:
            return False