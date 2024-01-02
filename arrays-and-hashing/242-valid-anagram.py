#https://leetcode.com/problems/valid-anagram/


# Naive solution with  sorting
# Time complexity - O(nlog(n))
# Memory complexity - O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t: return True #edgecase - оптимизация до сортировки
        return sorted(s) == sorted(t)

# Optimal solution
# Time complexity - O(n)
# Memory complexity - O(1) - т.к 26 букв в англ алфавите - это константа
class Solution:
    def count_dict(self, s: str):
        dic = {}
        for l in s:
            dic[l] = dic.get(l, 0)+1 #dic.get(l, 0) берет ключ, если нет, 0
        return dic

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if t==s: return True
        return self.count_dict(s) == self.count_dict(t)
