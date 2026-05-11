class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n = len(haystack)
        m = len(needle)
        
        # Если needle длиннее haystack, сразу возвращаем -1
        if m > n:
            return -1
        
        # Пробегаем по всем возможным позициям начала
        for i in range(n - m + 1):
            # Проверяем совпадение подстроки
            if haystack[i:i + m] == needle:
                return i
        
        return -1