#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List

# Optimal solution c использованием двух указателей
# Time complexity - O(n)
# Memory complexity - O(1)
#Idea: Двигаемся по строке с двух концов: слева и справа до тех пор, пока l<r (пока указатели не пересеклись).
# Считаем сумму numbers[l]+numbers[r], и если получившаяся сумма больше таргета, то сдвигаем правый указатель r на 1 шаг
# до предпоследнего числа и так до тех пор, пока сумма не станет меньше таргета. В этом случае мы сдвигаем левый
# указатель l на 1 шаг вперед до второго элемента. И повторяем предыдущие шаги до тех пор, пока не найдем сумму
# равную таргету . Тогда возвращаем [l+1, r+1]. То есть при данном алгоритме и пробешаем наш лист с двух сторон до
# середины


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2: return [1, 2] #edgecase
        l, r = 0, len(numbers)-1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1s]
