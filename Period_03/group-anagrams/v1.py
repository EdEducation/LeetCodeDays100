from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashTable = {}
        
        for item in strs:
            key = "".join(sorted(item))

            if key in hashTable:
                hashTable[key].append(item)
            else:
                hashTable[key] = [item]

        return list(hashTable.values())


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример с несколькими анаграммами
    assert sorted([sorted(group) for group in solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])]) == \
           sorted([sorted(group) for group in [["bat"],["nat","tan"],["ate","eat","tea"]]]), "Тест 1 провален"
    
    # Тест 2: Пустая строка
    assert solution.groupAnagrams([""]) == [[""]], "Тест 2 провален"
    
    # Тест 3: Одиночный символ
    assert solution.groupAnagrams(["a"]) == [["a"]], "Тест 3 провален"
    
    # Тест 4: Нет анаграмм
    result = solution.groupAnagrams(["abc", "def", "ghi"])
    assert len(result) == 3 and all(len(group) == 1 for group in result), "Тест 4 провален"
    
    # Тест 5: Все строки одинаковые
    result = solution.groupAnagrams(["abc", "abc", "abc"])
    assert len(result) == 1 and len(result[0]) == 3, "Тест 5 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()