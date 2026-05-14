class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример
    assert solution.multiply("2", "3") == "6", "Тест 1 провален"
    
    # Тест 2: Пример с переносами
    assert solution.multiply("123", "456") == "56088", "Тест 2 провален"
    
    # Тест 3: Умножение на ноль
    assert solution.multiply("0", "456") == "0", "Тест 3 провален"
    
    # Тест 4: Умножение больших чисел
    assert solution.multiply("999", "999") == "998001", "Тест 4 провален"
    
    # Тест 5: Одна цифра на многозначное
    assert solution.multiply("5", "1234") == "6170", "Тест 5 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()