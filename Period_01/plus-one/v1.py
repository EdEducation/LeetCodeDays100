# https://leetcode.com/problems/plus-one/submissions/1980836275

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # суммируемое число, инициируем значением 1
        
        # перебор справа налево
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            if total > 9:
                digits[i] = total % 10  # остаток от деления на 10
                carry = total // 10     # целочисленное деление на 10
            else:
                digits[i] = total
                carry = 0
                break  # если переноса нет, можно выйти
        
        # Если после перебора остался перенос, добавляем в начало
        if carry > 0:
            digits.insert(0, carry)
        
        return digits


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример без переноса
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4], "Тест 1 провален"
    
    # Тест 2: Пример с переносом в последнем разряде
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2], "Тест 2 провален"
    
    # Тест 3: Однозначное число 9 -> 10 (увеличение длины)
    assert solution.plusOne([9]) == [1, 0], "Тест 3 провален"
    
    # Тест 4: Однозначное число не 9
    assert solution.plusOne([5]) == [6], "Тест 4 провален"
    
    # Тест 5: Все цифры 9 ([9,9,9] -> [1,0,0,0])
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0], "Тест 5 провален"
    
    # Тест 6: Несколько девяток в конце
    assert solution.plusOne([1, 2, 9, 9]) == [1, 3, 0, 0], "Тест 6 провален"
    
    # Тест 7: Ноль в середине
    assert solution.plusOne([1, 0, 0, 1]) == [1, 0, 0, 2], "Тест 7 провален"
    
    # Тест 8: Большое число без переноса
    assert solution.plusOne([7, 8, 9, 1, 2, 3]) == [7, 8, 9, 1, 2, 4], "Тест 8 провален"
    
    # Тест 9: Каскадный перенос через несколько разрядов
    assert solution.plusOne([1, 9, 9, 9]) == [2, 0, 0, 0], "Тест 9 провален"
    
    # Тест 10: Минимальная длина [0]
    assert solution.plusOne([0]) == [1], "Тест 10 провален"
    
    # Тест 11: Перенос не с последней позиции
    assert solution.plusOne([2, 9, 3]) == [2, 9, 4], "Тест 11 провален"
    
    # Тест 12: Перенос через несколько цифр но не всех
    assert solution.plusOne([1, 9, 9, 2]) == [1, 9, 9, 3], "Тест 12 провален"
    
    # Тест 13: Две девятки
    assert solution.plusOne([9, 9]) == [1, 0, 0], "Тест 13 провален"
    
    # Тест 14: Число из одной цифры 8
    assert solution.plusOne([8]) == [9], "Тест 14 провален"
    
    # Тест 15: Длинное число с переносом в середине
    assert solution.plusOne([1, 2, 3, 9, 9, 9]) == [1, 2, 4, 0, 0, 0], "Тест 15 провален"
    
    # Тест 16: Максимальная длина (100 девяток) - проверка увеличения длины
    digits_max = [9] * 100
    expected_max = [1] + [0] * 100
    assert solution.plusOne(digits_max) == expected_max, "Тест 16 провален"
    
    # Тест 17: Число с нулями в конце
    assert solution.plusOne([1, 0, 0, 0]) == [1, 0, 0, 1], "Тест 17 провален"
    
    # Тест 18: Число 199 -> 200
    assert solution.plusOne([1, 9, 9]) == [2, 0, 0], "Тест 18 провален"
    
    # Тест 19: Число 999 -> 1000
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0], "Тест 19 провален"
    
    # Тест 20: Число 1099 -> 1100
    assert solution.plusOne([1, 0, 9, 9]) == [1, 1, 0, 0], "Тест 20 провален"

    # Тест 21: Число 9999.... 100 раз -> 10000 (0 сто раз) 
    datain = [9] * 100
    dataout = [1] + [0] * 100
    assert solution.plusOne(datain) == dataout, "Тест 20 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()