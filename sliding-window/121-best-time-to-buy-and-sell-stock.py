#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List

# Optimal solution
# Time complexity - O(n)
# Memory complexity - O(1)
#Idea: Идем от первого эл-та, пробегаемся по листу и сравниваем, если текущий рассматриваемый эл-т меньше, чем самы
# низкий, то делаем наименьшим эл-том текущий эл-т, при этом одновременно максимизируем текущий результат с разницей
# между текущим эл-ом и наименьшим и текущим результатом (счетчиком)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price-lowest)
        return res
