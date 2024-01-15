#https://leetcode.com/problems/3sum/

from typing import List

# Optimal solution c использованием двух указателей
# Time complexity - O(n^2) (использ-ся 2 цикла и сортировка O(nLog(n)+n^2 => O(n^2))
# Memory complexity - O(1) O(n)
#Idea: Двигаемся по строке с двух концов: слева и справа до тех пор, пока l<r (пока указатели не пересеклись). Сначала
# нам нужно отсортировать лист nums. Далее мы циклом бежим по индексам и значениям в листе. Нюанс в отсутствии
# дубликатов триплетов.
# Считаем сумму nums[l]+nums[r]+a, и если получившаяся сумма больше 0, то сдвигаем правый указатель r на 1 шаг
# до предпоследнего числа и так до тех пор, пока сумма не станет меньше 0. В этом случае мы сдвигаем левый
# указатель l на 1 шаг вперед до второго элемента. И повторяем предыдущие шаги до тех пор, пока не найдем сумму
# равную 0 . Тогда добавляем лист [a, nums[l], nums[r]]. То есть при данном алгоритме и пробешаем наш лист с двух
# сторон до середины.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #if len(nums) == 3: return nums
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            #skip positive integers
            if a>0:
                break
            if i>0 and a == nums[i-1]: #для предупреждения дублей
                continue
            l, r = i+1, len(nums) - 1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -=1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
