class Solution:
    def romanToInt(self, s: str) -> int:
        # реализовать
        pass


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Простое число
    assert solution.romanToInt("III") == 3, "Тест 1 провален"
    
    # Тест 2: Число с добавлением
    assert solution.romanToInt("LVIII") == 58, "Тест 2 провален"
    
    # Тест 3: Сложное число с вычитаниями
    assert solution.romanToInt("MCMXCIV") == 1994, "Тест 3 провален"
    
    # Дополнительные тесты
    assert solution.romanToInt("IV") == 4, "Тест 4 провален"
    assert solution.romanToInt("IX") == 9, "Тест 5 провален"
    assert solution.romanToInt("XL") == 40, "Тест 6 провален"
    assert solution.romanToInt("XC") == 90, "Тест 7 провален"
    assert solution.romanToInt("CD") == 400, "Тест 8 провален"
    assert solution.romanToInt("CM") == 900, "Тест 9 провален"
    assert solution.romanToInt("MCMXC") == 1990, "Тест 10 провален"
    assert solution.romanToInt("MMMCMXCIX") == 3999, "Тест 11 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()