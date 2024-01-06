from typing import List
from collections import defaultdict

# Naive solution with sorting
# Time complexity - O(nlog(n))
# Memory complexity - O(n)
# Idea: создаем ф-ю, которая сортирует эл-ты в строке. Отсортированное знач-е мы будем использовать в качестве ключа в
# словаре. Создаем пустой словарь и добавляем в него ключ-значение, где ключ-отсортированная строка, значение -
# лист с эл-ами из листа strs, которые отнносятся к данному хэшу. Если ключ есть в словаре, то мы аппендим просто эл-т
# из листа, если ключа нет, то добавляем и новый ключ, и значение

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_hash(s: str) -> str:
            rs = ''.join(sorted(s))
            return rs

        dict_anagr = {}
        for s in strs:
            hs = get_hash(s)
            if hs in dict_anagr.keys():
                dict_anagr[hs].append(s)
            else:
                dict_anagr[hs] = [s]

        return [item for item in dict_anagr.values()]

#Такое же решение, как и выше, только с ипольз-ем defaultdic

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_hash(s: str) -> str:
            rs = ''.join(sorted(s))
            return rs

        dict_anagr = defaultdict(list)
        for s in strs:
            dict_anagr[get_hash(s)].append(s)
        return [item for item in dict_anagr.values()]
