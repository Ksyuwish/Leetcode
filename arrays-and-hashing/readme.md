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
