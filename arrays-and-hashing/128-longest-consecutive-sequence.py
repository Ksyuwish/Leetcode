#https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

# Naive solution with sorting
# Time complexity - O(nlogn)
# Memory complexity - O(n)
#Idea: Сортируем лист nums, избавляем от дублей превращая в сет. Далее идем по каждому эл-ту листа и сравниваем эл-т
#nums[i+1] и nums[i] если разница =1 (остаемся в рамках последовательности, увеличиваем счетчик n на 1 и увеличиваем
# счетчик max_n = max(max_n, n)). Если выходим из последовательности, то снова начинаем считать с длины n=1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        n = 1
        max_n = 1
        nums = sorted(set(nums))
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                n += 1
                max_n = max(max_n, n)
            else:
                n = 1
        return max_n



# Optimal solution
# Time complexity - O(n)
# Memory complexity - O(n)
# Idea: Схлопываем дубли используя set. Проверяем у каждого эл-та наличие соседа слева. Если соседа нет, то длина = 1.
# Далее мы переходим к кейсам, когда есть сосед справа, т.е пока эл-т+ length есть в нашем сете, мы ищем максимум между
# длиной и самыой длинной последовательностью: longest = max(length, longest)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        nums_set = set(nums)
        longest = 1
        for num in nums_set:
            if num-1 not in nums_set:
                length = 1
                while num+length in nums_set:
                    length += 1
                    longest = max(length, longest)
        return longest


solution = Solution()
assert (solution.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1])) == 9
