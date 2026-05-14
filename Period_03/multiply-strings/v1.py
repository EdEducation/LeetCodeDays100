class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Если один из множителей ноль, результат ноль
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Результат может содержать максимум m + n цифр
        result = [0] * (m + n)
        
        # Идем с конца строк (с младших разрядов)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Умножаем текущие цифры
                mul = int(num1[i]) * int(num2[j])
                # Позиции в массиве результата
                p1 = i + j      # старший разряд произведения
                p2 = i + j + 1  # младший разряд произведения
                # Складываем с уже имеющимся значением
                total = mul + result[p2]
                # Младший разряд сохраняем на месте
                result[p2] = total % 10
                # Перенос добавляем к старшему разряду
                result[p1] += total // 10
        
        # Пропускаем ведущие нули
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        # Преобразуем цифры в строку
        return ''.join(str(digit) for digit in result[start:])


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