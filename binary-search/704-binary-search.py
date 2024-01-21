#https://leetcode.com/problems/binary-search/description/

# Naive solution
# Time complexity - O(n)
# Memory complexity - O(n)
#Idea: Пробегаемся по индексам и значениям листа.
# Если текущее значение == target возвращаем текущее значение индекса, иначе - продолжаем искать.
# В итоге ф-ии возвращаем -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v==target:
                return i
            else:
                continue
        return -1


# Optimal solution
# Time complexity - O(log(n))
# Memory complexity - O(n)
#Idea: Используем два указателя l и r. Пока указатели не пересеклись (l <= r) ищем середину листа nums.
# Если эл-т посередине > target, сдвигаем правый указатель r на позицию m - 1, а если  эл-т посередине < target,
# сдвигаем левый указатель l на позицию m + 1, иначе - возвращаем m. Вся ф-я возвращает -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r: #<= использ-ся для случая маленькой длины nums
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
