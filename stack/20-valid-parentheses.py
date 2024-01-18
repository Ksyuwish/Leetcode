#https://leetcode.com/problems/valid-parentheses/description/

#Optimal solution
# Time complexity - O(n) т к мы проходим по всем эл-ам 1 раз
# Memory complexity - O(n)
#Idea: Создаем словарь со скобками: ключи - закрывающие скобки, значения - закрываюшие скобки. Двигаемся по строке и
# если это открывающая скобка, добавляем в stack.Если закрывающая собка в нашем словаре, проверяем чтобы стек был не
# пустым и последний вошедший в стек эл-т равен открывающей скобке, в этом случае очищаем стек. Если условие
# не выполнеяется, возвращаем False. Сама ф-я вернет False если stack не пустой и True, если пустой



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        MapOpenClose = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in MapOpenClose: #Проверяем есть ли закрывающая скобочка
                if stack and stack[-1] ==  MapOpenClose[c]: #Если последний добавленный эл-т =закрывающая скобка
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True
