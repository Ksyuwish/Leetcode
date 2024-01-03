#https://leetcode.com/problems/two-sum/submissions/

# Naive solution: перебираем все эл-ты, суммируя их между собой
# Time complexity - O(n^2)
# Memory complexity - O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                currsum = nums[i]+nums[j]
                if currsum == target:
                    return [i, j]


# Optimal solution: val = target - nums[i]. Check val in nums, using dictionary (add to dictionary val:index)
# Time complexity - O(n)
# Memory complexity - O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        MapDict = {} #val:index
        for i, n in enumerate(nums): #i - index, n-value
            diff = target - n #ищем разницу
            if diff in MapDict: #если разница в нашем словаре, возвращаем индекс эл-та из разницы и индекс эл-та из цикла
                return [MapDict[diff], i]
            MapDict[n] = i #если не нашли эл-та diff, добавляем в словарь val:indx
