# текст задачи с примерами и объяснениями
# Given two binary strings a and b, return their sum as a binary string.
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# Именной алгоритм: классическое сложение "столбиком" с переносом (binary addition).
# Математическое решение за O(1) (но только если считать int() константным,
# что на практике неверно для длинных строк): 
# result = bin(int(a, 2) + int(b, 2))[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Сложение двух двоичных строк.
        
        Решение: классический алгоритм сложения "столбиком" с переносом.
        Время: O(max(len(a), len(b))) - проходим по каждому биту один раз.
        Память: O(max(len(a), len(b))) - для хранения результата.
        
        Альтернатива (если допустимо): 
        return bin(int(a, 2) + int(b, 2))[2:]
        Но это скрывает линейную сложность внутри int() и bin().
        """
        
        i = len(a) - 1  # указатель на последний символ строки a
        j = len(b) - 1  # указатель на последний символ строки b
        carry = 0       # перенос в следующий разряд
        result = []     # список для накопления битов результата (в обратном порядке)
        
        # Идем справа налево, пока есть биты в любой строке или есть перенос
        while i >= 0 or j >= 0 or carry:
            # Получаем текущие биты (если строка закончилась, то 0)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Сумма битов + перенос
            total = bit_a + bit_b + carry
            
            # Текущий бит результата: total % 2
            result.append(str(total % 2))
            
            # Новый перенос: total // 2
            carry = total // 2
            
            # Сдвигаем указатели влево
            i -= 1
            j -= 1
        
        # Результат накоплен в обратном порядке, разворачиваем и объединяем
        return ''.join(reversed(result))


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Обычный случай с переносом
    assert solution.addBinary("11", "1") == "100", "Тест 1 провален"
    
    # Тест 2: Пример из условия
    assert solution.addBinary("1010", "1011") == "10101", "Тест 2 провален"
    
    # Тест 3: Оба нуля
    assert solution.addBinary("0", "0") == "0", "Тест 3 провален"
    
    # Тест 4: Один ноль
    assert solution.addBinary("0", "111") == "111", "Тест 4 провален"
    
    # Тест 5: Разная длина с множественными переносами
    assert solution.addBinary("1111", "1") == "10000", "Тест 5 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()