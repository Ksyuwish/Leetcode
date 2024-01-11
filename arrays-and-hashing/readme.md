## Task 217: contains duplicate

#### Description

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

#### Naive solution with  set(list)
***Time complexity*** - O(n)
***Memory complexity*** - O(n)

Перегоняем array в set() => если длина сета = длина листа, то дубликатов нет, иначе - есть

#### Optimal solution
***Time complexity*** - O(n)
***Memory complexity*** - O(n)

Создаем пустой сет set(), идем по элементам в листе циклом: если элемент есть в сете, 
то возвращаем True, иначе: добавляем эл-т в set `new.add(num)`

## Task 242: valid anagram

#### Description

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

#### Naive solution with  sorting
***Time complexity***  - O(nlog(n))
***Memory complexity*** - O(n)

Если s == t возвращаем True (edgecase - оптимизация до сортировки)

Далее сортируем строки. Если после сортировки строки равны, возвращаем True

#### Optimal solution
***Time complexity*** - O(n)
***Memory complexity*** - O(1) - т.к 26 букв в англ алфавите - это константа

Создаем функцию. Идея: создаем пустой словарь. Циклом добавляем в него каждую букву из строки. 
Ключ-буква из строки, значение- ск-ко раз встречается в справочнике (`dic[l] = dic.get(l, 0)+1`
dic.get(l, 0) берет ключ, если нет, 0. в случае, если встречаем букву неск-ко раз, добавляем 1 
на каждой итерации). Ф-я возвращает словарь.

Далее применяем функцию к каждой строке (s, t) и сравниваем оба словаря между собой. Если они 
равны, возвращаем True. 

Также важно прописать edge cases: 

- Если длины строк не равны, возвращаем False. 
- Если s == t возвращаем True 

## Task 1: two sum

#### Description

Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same 
element twice.

You can return the answer in any order.

#### Naive solution: перебираем все эл-ты, суммируя их между собой
***Time complexity***  - O(n^2)
***Memory complexity*** - O(n)

- Прописываем edge case: Если всего 2 эл-та в листе, то возвращаем индексы [0, 1]
- Далее идем циклом по всем эл-там (2 цикла i, j) чтобы просуммировать все комбинации эл-ов


#### Optimal solution: val = target - nums[i]. Check val in nums, using dictionary (add to dictionary val:index)
***Time complexity***  - O(n)
***Memory complexity*** - O(n)

Создаем пустой словарь и проходимся по индексам и значениям листа добавляя эл-ты в словарь 
по следующей логике val:index. Ищем разницу: diff = target - val.
Если diff  разница в нашем словаре, возвращаем индекс эл-та из разницы и индекс эл-та из цикла

## Task 49: Group Anagrams

#### Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

#### Naive solution with sorting
***Time complexity***  - O(nlog(n))
***Memory complexity*** - O(n)

Создаем ф-ю, которая сортирует эл-ты в строке. Отсортированное знач-е мы будем использовать 
в качестве ключа в словаре. Создаем пустой словарь и добавляем в него ключ-значение, 
где ключ-отсортированная строка, значение - лист с эл-ами из листа strs, 
которые относятся к данному хэшу. Если ключ есть в словаре, то мы аппендим просто эл-т 
из листа, если ключа нет, то добавляем и новый ключ, и значение

#### Optimal solution
***Time complexity***  - O(n)
***Memory complexity*** - O(n)

Ключами являются листы (переведенные в строки) с хэштрованием юникода. Создаем словарь
и циклом добавляем к каждому ключу элемент из листа strs. Возвращаем values словаря


## Task 347: Top K Frequent Elements

#### Description

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

#### Naive solution with sorting
***Time complexity***  - O(n^2)
***Memory complexity*** - O(n)

Создаем словарь и считаем кол-во эл-ов из листа nums. Берем значения из словаря (частоты эл-ов),
сортируем этот лист и берем к последних эл-ов. Если эл-ты одинаковые в листе, 
то сетом удаляем дубли.
Теперь по значениям будем брать ключи словаря, который мы создали изначально. Добавляем все ключи,
 котор нам подходят и добавляем их в лист, и возаращаем этот лист в ответе


#### Naive solution with sorting
***Time complexity***  - O(nlog(n))
***Memory complexity*** - O(n)

Создаем словарь и считаем кол-во эл-ов из листа nums. Сортируем значения из словаря 
по ключу реверсивно и вызываем по первому ключу получившийся лист

#### Optimal solution Using Bucket Sort
***Time complexity***  - O(n)
***Memory complexity*** - O(n)

Создать словарь и считаем кол-во эл-ов из листа nums. Далее создаем корзинки с листами длины 
len(nums) , где кол-во корзинок - ключ (0, 1, 2...len(nums)), значения - 
сами эл-ты из nums. Начать искать k эл-ов с конца корзинок до тех пор пока длина листа из корзины 
не станет равна k.

## Task 128: Longest Consecutive Sequence

#### Description

Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.

#### Naive solution with sorting
***Time complexity***  - O(nlog(n))
***Memory complexity*** - O(n)

Сортируем лист nums, избавляем от дублей превращая в сет. 
Далее идем по каждому эл-ту листа и сравниваем эл-т `nums[i+1]` и `nums[i]` если разница =1 
(остаемся в рамках последовательности), увеличиваем счетчик n на 1 и увеличиваем
счетчик max_n = max(max_n, n)). Если выходим из последовательности, 
то снова начинаем считать с длины n=1

#### Optimal solution 
***Time complexity***  - O(n)
***Memory complexity*** - O(n)

Схлопываем дубли используя set. Проверяем у каждого эл-та наличие соседа слева. 
Если соседа нет, то длина = 1.
 Далее мы переходим к кейсам, когда есть сосед справа, т.е пока эл-т+ length есть в нашем сете, 
мы ищем максимум между длиной и самой длинной последовательностью: 
`longest = max(length, longest)`
