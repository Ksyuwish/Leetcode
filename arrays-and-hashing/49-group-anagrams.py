#https://leetcode.com/problems/group-anagrams/
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


# Optimal solution
# Time complexity - O(n)
# Memory complexity - O(n)
#Idea: ключами являются листы (переведенные в строки) с хэштрованием юникода. Создаем словарь
# и циклом добавляем к каждому ключу элемент из листа strs. Возвращаем values словаря
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_list(s: str) -> str:
            counter = [0]* 26
            for l in s:
                counter[ord(l)-ord("a")] += 1
            return counter

        res = {}
        for s in strs:
            key_str = ','.join(map(str, count_list(s)))
            if key_str not in res.keys():
                res[key_str] = [s]
            else:
                res[key_str].append(s)
        return res.values()
