## Task 125: Valid Palindrome

#### Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

#### Naive solution c использованием встроенных ф-ий -> extra memory
***Time complexity*** - O(n)
***Memory complexity*** - O(n)

Создаем пустую строку и циклом проходимся по всем символам из первоначальной строки. 
Проверяем с помощью isalnum() символы и если это буква, добавляем ее в строку предварительно 
приведя к lower(). Далее сравниваем получившуюся строку с реверсивной версией newStr[::-1]

#### Optimal solution c использованием двух указателей
***Time complexity*** - O(n)
***Memory complexity*** - O(1)

Двигаемся по строке с двух концов: слева и справа до тех пор,
пока l<r (пока указатели не пересеклись). Отдельно нужно создать функцию для обработки символов 
используя `ord(): (ord('A') <= ord(letter) <= ord('Z')`. Если уперлись в символ, 
то должны сдвинуться на одну позицию (касается l и r). Если символ l != символ r, возвращаем False.
В конце основного цикла while обязательно сдвигаемся на 1 слева (+) и справа (-)


## Task 167: Two Sum II - Input Array Is Sorted

#### Description

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer 
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.

#### Optimal solution c использованием двух указателей
***Time complexity*** - O(n)
***Memory complexity*** - O(1)


Двигаемся по строке с двух концов: слева и справа до тех пор, пока l<r 
(пока указатели не пересеклись).
Считаем сумму `numbers[l]+numbers[r]`, и если получившаяся сумма больше таргета, 
то сдвигаем правый указатель r на 1 шаг до предпоследнего числа и так до тех пор, пока сумма 
не станет меньше таргета. В этом случае мы сдвигаем левый указатель l на 1 шаг вперед до второго 
элемента. И повторяем предыдущие шаги до тех пор, пока не найдем сумму равную таргету. 
Тогда возвращаем `[l+1, r+1]`. То есть при данном алгоритме и пробешаем наш лист с двух сторон до 
середины



## Task 15: 3 sum

#### Description


Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


#### Optimal solution c использованием двух указателей

***Time complexity*** - O(n^2) (использ-ся 2 цикла и сортировка O(nLog(n)+n^2 => O(n^2))
***Memory complexity*** -  O(1) O(n)


Двигаемся по строке с двух концов: слева и справа до тех пор, пока l<r (пока указатели 
не пересеклись). Сначала нам нужно отсортировать лист nums. Далее мы циклом бежим по индексам 
и значениям в листе. Нюанс в отсутствии дубликатов триплетов.
 Считаем сумму nums[l]+nums[r]+a, и если получившаяся сумма больше 0, то сдвигаем правый 
указатель r на 1 шаг до предпоследнего числа и так до тех пор, пока сумма не станет меньше 0. 
В этом случае мы сдвигаем левый указатель l на 1 шаг вперед до второго элемента. И повторяем 
предыдущие шаги до тех пор, пока не найдем сумму равную 0 . 
Тогда добавляем лист [a, nums[l], nums[r]]. То есть при данном алгоритме и пробегаем наш лист 
с двух сторон до середины.
