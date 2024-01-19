#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# Optimal solution
# Time complexity - O(2n) тк мы можем удалять эл-т и добавлять его -> O(n)
# Memory complexity - O(n)
# Idea: Создаем пустой стек (лист). Итерируемся по элементам листа. В условии else прописываем добавление эл-та в стек
# с типом данных int (добавляем цифпы в лист до тех пор, пока не натыкаемся на знак +/-/*//). В случае операции +/* мы
# добавляем в стек последние добавленные эл-ты a+b/a*b используя pop(), в случае "-" наоборот добавляем b-a, а в случае
# "/" обязательно делаем это через int(b/a) чтобы округлить до меньшего значения. Возвращаем в ответе stack[0].
# Суть Polish notation в том, чтобы применять операторы +/-/*// к двум соседствующим эл-ам.

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el == '+':
                stack.append(stack.pop()+stack.pop())
            elif el == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif el == '*':
                stack.append(stack.pop()*stack.pop())
            elif el == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(el))
        return stack[0]
