class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(s: str):
            if not s:
                return False
            if s:
                if not ((s >= 'a' and s <= 'z') or (s >= '0' and s <= '9')):
                    return False
            return True
        
        s = list(s.lower())
        l_ptr, r_ptr = 0, len(s)-1
        while l_ptr < r_ptr:
            while l_ptr < r_ptr and not isAlpha(s[l_ptr]):
                l_ptr += 1
            
            while r_ptr > l_ptr and not isAlpha(s[r_ptr]):
                r_ptr -= 1

            if s[l_ptr] != s[r_ptr]:
                return False
            else:
                l_ptr += 1
                r_ptr -= 1

        return True