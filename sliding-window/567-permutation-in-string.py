#https://leetcode.com/problems/permutation-in-string/description/

# Optimal solution
# Time complexity - O(26)+O(n) -> O(n)
# Memory complexity - O(n)
#Idea: Необходимо создать счетчик matches. Считаем кол-во букв в s1, и в s2 на каждой итерации рассматриваем столько
# кол-во букв, ск-ко len(s1). Считаем кол-во каждой буквы в s2. Сравниваем с кол-ом каждой буквы в s1. Считаем разницу:
# 26 - [кол-во букв, которые различаются в обоих строках]. Обновляем счетчик. Если matches == 26 возвращаем True,
# иначе - False.



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False #edgecase
        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i]==s2Count[i] else 0)

        l = 0 #sliding window part

        for r in range(len(s1), len(s2)): #тк в цикле выше мы проходили до len(s1), то ставим правый указатель range(len(s1), len(s2))
            if matches == 26:  return True
            index = ord(s2[r]) - ord('a') #это нужно для корректного отображения индекса при движении правым указателем
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]+1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]-1 == s2Count[index]:
                matches -= 1

            l += 1
        return matches == 26

