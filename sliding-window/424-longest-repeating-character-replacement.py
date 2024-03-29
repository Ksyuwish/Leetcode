#https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Optimal solution
# Time complexity - O(2n) т.к. 2 указателя -> O(n)
# Memory complexity - O(26n) тк 26 букв-> O(n)
#Idea: Создаем словарь для хранения кол-ва букв, переменную для историч максимума длины строки и левый указатель.
# Идем циклом по строке используя индексы в качестве правого указателя. добавляем в словарь букву если буквы нет,
# и увеличиваем кол-во на 1 если буква есть. Прописываем цикл while с условием:
# длина окна (l-r+1) - наиболее часто встречающийся эл-т (max(count.values))
# = кол-во букв, которые нам нужно заменить > k (разрешенные замены). Пока выполняется это условие, мы вычитаем
# из словаря 1 у того эл-та, на котором сейчас стоит левый указатель и прибавляем 1 к левому указателю, чтобы сдвинуть
# указатель вправо. Далее находим максимум между историческим максимумом и длиной окна (l-r+1)
# Возвращаем в ответе исторический максимум


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #добавляем в словарь кол-во каждой буквы
        max_length = 0 #исторический максимум длины подстроки
        l = 0 #левый указатель

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #на каждой итерации увеличиваем кол-во букв в словаре

            while r-l+1-max(count.values()) > k: #r-l+1(window length) - max(count.values) more frequent element = кол-во букв, которые нам нужно заменить
                count[s[l]] -= 1
                l +=1

            max_length = max(max_length, r-l+1)

        return max_length

