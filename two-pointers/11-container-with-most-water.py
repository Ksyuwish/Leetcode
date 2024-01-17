#https://leetcode.com/problems/container-with-most-water/

#Optimal solution c использованием двух указателей
# Time complexity - O(n)
# Memory complexity - O(1) - т.к. хранение переменных не занимает память
#Idea: Двигаемся по листу с двух концов: слева и справа до тех пор, пока l<r (пока указатели не пересеклись).
# Обязательно заводим счетчик s_max = 0. Этот счетчик нужен для того, чтобы искать максимальную площадь области (на
# каждой итерации ищем максимум между s_max и рассчитанной текущей площадью s). s рассчитываем как
# s = min(height[l], height[r]) * (r-l) (разность между индексами, умноженное на минимальное значение из листа (двух
# указателей)). Если height[l] < height[r] , то сдвигаем указатель слева, в остальных случаях - справа (так как нам
# важно взять наибольшую высоту столбца). В итоге функция возвращает максимальное значение нашего счетчика s_max

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        s_max = 0
        l, r = 0, len(height)-1
        while l<r:
            s = min(height[l], height[r]) * (r-l)
            s_max = max(s_max, s)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1 #можем схлопнуть elif и else в одну строку else: r -=1,
                #т.к. если l=r, то можем сдвинуть указатель l или r
        return s_max

