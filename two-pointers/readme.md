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
