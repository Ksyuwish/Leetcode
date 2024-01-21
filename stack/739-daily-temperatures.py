#https://leetcode.com/problems/daily-temperatures/

# Optimal solution
# Time complexity - O(n)
# Memory complexity - O(n)
#Idea: Создаем 2 листа: res с нулями (той же длины, что и len(temperatures)) и stack (pair: [temp, index]). Проходимся
# по индексам и значениям листа temperatures. Прописывем цикл while: пока стек не пустой и
# текущее значение температуры > предыдыдущей температуры из стека (тк пара,берем 0-ой эл-т).
# Сохраняем попнутые значения из стека в переменные stackT, stackInd. В лист res на место индекса stackInd
# добавляем разницу между текущим индексом и попнутым идексом из стека stackInd. В конце цикла for аппедним в стек
# текущее значение температуры из temperatures и текущий индекс. В ответе возвразаем лист res.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures) #т.к. ответ будет той же длины, что и len(temperatures)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #t>предыдыдущей температуры из стека. тк пара,берем 0-ой эл-т
                stackT, stackInd = stack.pop()
                res[stackInd] = i-stackInd
            stack.append([t, i])
        return res
