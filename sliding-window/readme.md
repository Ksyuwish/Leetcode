## Task 121: Best Time to Buy and Sell Stock

#### Description

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

#### Optimal solution
***Time complexity***  - O(n)
***Memory complexity*** - O(1)

Идем от первого эл-та, пробегаемся по листу и сравниваем, если текущий рассматриваемый эл-т меньше,
чем самый низкий, то делаем наименьшим эл-том текущий эл-т, при этом одновременно 
максимизируем текущий результат с разницей между текущим эл-ом и наименьшим 
и текущим результатом (счетчиком)


## Task 3: Longest Substring Without Repeating Characters 

#### Description

Given a string s, find the length of the longest
substring
without repeating characters.


#### Optimal solution
***Time complexity***  - O(n) т.к. проходимся по всем эл-ам в худшем случае
***Memory complexity*** - O(n) т.к. храним в памяти сет

Создаем пустой сет для хранения подстрок, а также счетчик для подсчета исторического максимума 
самой длинной подстроки и переменную для левого указателя. Идем от первого эл-та, 
пробегаемся по листу s и, пока текущий рассматриваемый элемент находится в сете, 
удаляем все эл-ты слева от повторяющегося эл-та. Когда все удалили, добавляем эл-ты в сет 
до тех пор, пока снова не попадем в цикл while и пока не увидим повторяющийся эл-т. Там же 
обновляем исторический максимум длины подстроки, если он оказался выше текущего историч максимума 
(r-l+1). В ф-ии возвращаем исторический максимум самой длинной подстроки.


## Task 424: Longest Repeating Character Replacement

#### Description

You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation at most 
k times.

Return the length of the longest substring containing the same letter you can get after 
performing the above operations.


#### Optimal solution
***Time complexity***  - O(2n) т.к. 2 указателя -> O(n)
***Memory complexity*** - O(26n) тк 26 букв-> O(n)

Создаем словарь для хранения кол-ва букв, переменную для историч максимума длины строки 
и левый указатель. Идем циклом по строке используя индексы в качестве правого указателя. 
добавляем в словарь букву если буквы нет, и увеличиваем кол-во на 1 если буква есть. 
Прописываем цикл while с условием:
длина окна (l-r+1) - наиболее часто встречающийся эл-т (max(count.values))
= кол-во букв, которые нам нужно заменить > k (разрешенные замены). 
Пока выполняется это условие, мы вычитаем из словаря 1 у того эл-та, на котором сейчас 
стоит левый указатель и прибавляем 1 к левому указателю, чтобы сдвинуть указатель вправо. 
Далее находим максимум между историческим максимумом и длиной окна (l-r+1).
Возвращаем в ответе исторический максимум.


## Task 567: Permutation In String 

#### Description

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


#### Optimal solution
***Time complexity***  - O(26)+O(n) -> O(n)
***Memory complexity*** - O(n)

Необходимо создать счетчик matches. Считаем кол-во букв в s1, и в s2 на каждой итерации 
рассматриваем столько кол-во букв, ск-ко len(s1). Считаем кол-во каждой буквы в s2. 
Сравниваем с кол-ом каждой буквы в s1. Считаем разницу:
26 - [кол-во букв, которые различаются в обоих строках]. Обновляем счетчик. 
Если matches == 26 возвращаем True, иначе - False.

#### Optimal solution проще
***Time complexity***  - O(26n)
***Memory complexity*** - O(n)


Генерим 2 листа s1_count и s2_count состоящие из 26 0 и в каждый индекс из этих строк
мы присвоим цифру - кол-во раз, которое эта буква встречается. Причем для s2_count мы 
рассматриваем столько же букв, сколько в s1. 
Ставим левый указатель на 0, а правым будем скользить по s2 (range(len(s1), len(s2))). 
Если `s1_count == s2_count` возвращаем True. Из `s2_count[ord(s2[l]) - ord("a")]` вычитаем 1 
(чтобы уменьшить кол-во букв на левом указателе,  тк мы сдвинули указатель) и к 
`s2_count[ord(s2[r]) - ord("a")]` прибавляем 1, тк правым указателем мы проскользили 
и добавили новую букву. В конце двигаем указатель l (l += 1). 
В итоге возвращаем s1_count == s2_count чтобы согласно этому выражению было `True` или `False`.
