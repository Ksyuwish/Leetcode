#https://leetcode.com/problems/generate-parentheses/description/

# Optimal solution
# Time complexity - O(n)
# Memory complexity - O(n)
#Idea:
# 1) Мы можем добавить "(" если кол-во "("<n
# 2) Мы можем добавить ")" если кол-во ")" < кол-во "("
# 3) Когда кол-во "(" == кол-во ")" == n получаем окончательный результат
# В задаче используется рекурсия.Создаем ф-ю с несколькими условиями if:
# - 1) Если кол-во "(" == кол-во ")" == n Добавляем в пустой лист res строку с последовательностью скобок
# - 2) Если кол-во "("<n добавляем в стек "(" , применяем снова эту же ф-ю с openN+1 и попаем стек
# - 3) Если кол-во ")" < кол-во "(" добавляем в стек ")" применяем снова эту же ф-ю с closedN+1 и попаем стек

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open<n
        #only add a closing paranthesis if closed<open
        # valid if open==closed==n
        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0, 0)

        return res
