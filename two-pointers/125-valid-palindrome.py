#https://leetcode.com/problems/valid-palindrome/description/

# Naive solution c использованием встроенных ф-ий -> extra memory
# Time complexity - O(n)
# Memory complexity - O(n)
#Idea: Создаем пустую строку и циклом проходимся по всем символам из первоначальной строки. Проверяем с помощью
# isalnum() символы и если это буква, добавляем ее в строку предварительно приведя к lower(). Далее сравниваем
# получившуюся строку с реверсивной версией newStr[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #edgecases
        if len(s) <= 1: return True
        newStr = ""
        for l in s:
            if l.isalnum(): #если строка содержит букву
                newStr += l.lower() #приводим к lowercase и добавляем в нов строку
        return newStr == newStr[::-1]

# Optimal solution c использованием двух указателей
# Time complexity - O(n)
# Memory complexity - O(1)
#Idea: Двигаемся по строке с двух концов: слева и справа до тех пор, пока l<r (пока указатели не пересеклись). Отдельно
# нужно создать функцию для обработки символов используя ord(): (ord('A') <= ord(letter) <= ord('Z'). Если уперлись
# в символ, то должны сдвинуться на одну позицию (касается l и r). Если символ l != символ r, возвращаем False.
# В конце основного цикла while обязательно сдвигаемся на 1 слева (+) и справа (-)



class Solution:
    def isPalindrome(self, s: str) -> bool:
        #edgecases
        if len(s) <= 1: return True
        def alpfaNum(letter):
            return ((ord('A') <= ord(letter) <= ord('Z')) or
            (ord('a') <= ord(letter) <= ord('z')) or
            (ord('0') <= ord(letter) <= ord('9')))
        l, r = 0, len(s) - 1 #обозначаем указатели
        while l<r: #пока указатели не пересеклись
            while l<r and not alpfaNum(s[l]): #если один из указателей не alphanum сдвигаемся на 1 позицию
                l += 1
            while r>l and not alpfaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): #если l и r не совпадают, возвращаем False
                return False
            l, r = l+1, r-1
        return True
