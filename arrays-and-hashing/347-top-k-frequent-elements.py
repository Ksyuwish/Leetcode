#https://leetcode.com/problems/top-k-frequent-elements/
from typing import List

# Naive solution with  sorting
# Time complexity - O(nlog(n))
# Memory complexity - O(n)
#Idea: Создаем словарь и считаем кол-во эл-ов из листа nums. Берем значения из словаря (частоты эл-ов),
#сортируем этот лист и берем к последних эл-ов. Если эл-ты одинаковые в листе, то сетом удаляем дубли.
#теперь по значениям будем брать ключи словаря, который мы создали изначально. Добавляем все ключи,
# котор нам подходят и добавляем их в лист, и возаращаем этот лист в ответе

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums #edgecase

        dict_freq = {}
        for num in nums:
            dict_freq[num] = dict_freq.get(num, 0) + 1
        res_val = sorted(list(dict_freq.values()))
        res_val = set(res_val[-k:]) #get lst k items from list

        def get_keys_from_val(d: dict, val: int):
            return [k for k,v in d.items() if v==val]

        final_list = []
        for i in res_val:
            final_list.extend(get_keys_from_val(dict_freq, i))
        return final_list

# Optimal solution Using Bucket Sort
# Time complexity - O(n)
# Memory complexity - O(n)

#Idea: Создать словарь длины len(nums) , где кол-во эл-ов - ключ (0, 1, 2...len(nums)), значения - сами эл-ты из nums
#Начать искать k эл-ов с конца отсортированных ключей

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

