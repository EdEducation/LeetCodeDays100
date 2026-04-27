class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0
        
        # 2. Handle sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 3. Read digits
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        
        # 4. 
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result