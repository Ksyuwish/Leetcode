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


# Optimal solution проще
# Time complexity - O(26n)
# Memory complexity - O(n)
#Idea: Генерим 2 листа s1_count и s2_count состоящие из 26 0 и в каждый индекс из этих строк мы присвоим цифру - кол-во
# раз, которое эта буква встречается. Причем для s2_count мы рассматриваем столько же букв, сколько в s1.
# Ставим левый указатель на 0, а правым будем скользить по s2 (range(len(s1), len(s2))). Если s1_count == s2_count
# возвращаем True. Из s2_count[ord(s2[l]) - ord("a")] вычитаем 1 (чтобы уменьшить кол-во букв на левом указателе,
# тк мы сдвинули указатель) и к s2_count[ord(s2[r]) - ord("a")] прибавляем 1, тк правым указателем мы проскользили
# и добавили новую букву. В конце двигаем указатель l (l += 1). В итоге возвращаем s1_count == s2_count
# чтобы согласно этому выражению было True или False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        l = 0
        for r in range(len(s1), len(s2)): # O(n)
            if s1_count == s2_count: # O(26)
                return True
            s2_count[ord(s2[l]) - ord("a")] -= 1
            s2_count[ord(s2[r]) - ord("a")] += 1
            l += 1

        return s1_count == s2_count #adc vs dcda (чтобы сделать проверку на правом крае)
