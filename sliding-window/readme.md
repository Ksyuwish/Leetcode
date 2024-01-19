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
