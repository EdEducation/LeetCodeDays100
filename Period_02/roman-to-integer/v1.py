class Solution:
    def romanToInt(self, s: str) -> int:
        # реестр цифр
        rim = dict()
        rim["M"] = 1000 
        rim["D"] = 500
        rim["C"] = 100
        rim["L"] = 50
        rim["X"] = 10
        rim["V"] = 5
        rim["I"] = 1

        total = 0
        n = len(s)
        
        # Итерируем по строке
        for i in range(n):
            current_value = rim[s[i]]
            
            # Проверяем, нужно ли вычитать текущее значение
            # Вычитаем, если следующий символ существует и его значение больше текущего
            if i + 1 < n and rim[s[i + 1]] > current_value:
                total -= current_value
            else:
                total += current_value
        
        return total


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