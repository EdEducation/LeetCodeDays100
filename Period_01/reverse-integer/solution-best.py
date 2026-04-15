#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задача: Reverse Integer (LeetCode 7)

Дано 32-битное знаковое целое число x. Верните число x с переставленными в обратном порядке цифрами.
Если при перевороте число выходит за пределы 32-битного знакового целочисленного диапазона [-2^31, 2^31 - 1],
то верните 0.

Предполагается, что среда выполнения НЕ позволяет хранить 64-битные целые числа (ни знаковые, ни беззнаковые).

Примеры:
- Вход: x = 123    -> Выход: 321
- Вход: x = -123   -> Выход: -321
- Вход: x = 120    -> Выход: 21

Ограничения:
- -2^31 <= x <= 2^31 - 1

Примечание:
- Ведущие нули в перевёрнутом числе отбрасываются (как в примере с 120 -> 21).
- Для Python, где целые числа не ограничены по размеру, необходимо самостоятельно эмулировать 32-битное переполнение.
"""

from termcolor import colored


class Solution:
    def reverse(self, x: int) -> int:
        #INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        result = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Проверка переполнения перед умножением на 10
            if result > INT_MAX // 10:
                return 0
            # Дополнительная проверка для последней цифры (7 для INT_MAX)
            if result == INT_MAX // 10 and digit > 7:
                return 0
            
            result = result * 10 + digit
        
        return sign * result


# Тесты
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # Переполнение
        (-2147483648, 0),  # Переполнение
        (1463847412, 2147483641),  # Максимальное возможное
        (2147483647, 0),  # Переполнение
        (-2147483412, -2143847412),  # Работает в границах
    ]
    
    print("Запуск тестов для reverse integer:")
    print("-" * 50)
    
    passed = 0
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = solution.reverse(input_val)
        console_color = "green"

        if result == expected:
            status = "✓"
        else:
            status = "✗"
            console_color = "red"

        
        print(colored(f"Тест {i}: {status}", console_color))
        print(f"  Вход: {input_val}")
        print(f"  Ожидалось: {expected}")
        print(f"  Получено: {result}")
        print()
        if result == expected:
            passed += 1
    
    print("-" * 50)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")