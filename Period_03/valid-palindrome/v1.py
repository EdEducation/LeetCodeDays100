class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Пропускаем неалфавитно-цифровые символы слева
            while left < right and not s[left].isalnum():
                left += 1
            
            # Пропускаем неалфавитно-цифровые символы справа
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Сравниваем символы в нижнем регистре
            if s[left].lower() != s[right].lower():
                return False
            
            # Двигаем указатели к центру
            left += 1
            right -= 1
        
        return True


# Тесты для задачи Valid Palindrome
def run_tests():
    solution = Solution()
    
    # Тест 1: Классический палиндром с символами
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True, "Тест 1 провален"
    
    # Тест 2: Не палиндром
    assert solution.isPalindrome("race a car") == False, "Тест 2 провален"
    
    # Тест 3: Пустая строка (только пробел)
    assert solution.isPalindrome(" ") == True, "Тест 3 провален"
    
    # Тест 4: Только цифры
    assert solution.isPalindrome("12321") == True, "Тест 4 провален"
    
    # Тест 5: Смесь цифр и букв
    assert solution.isPalindrome("1a2b2a1") == True, "Тест 5 провален"
    
    # Тест 6: Один символ
    assert solution.isPalindrome("a") == True, "Тест 6 провален"
    
    # Тест 7: Один символ с пробелами/знаками
    assert solution.isPalindrome(".,!? a .,!?") == True, "Тест 7 провален"
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()