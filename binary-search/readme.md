## Task 704: Binary Search 

#### Description

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

#### Naive solution

***Time complexity*** - O(n) 
***Memory complexity*** -  O(n) 

Пробегаемся по индексам и значениям листа.
Если текущее значение == target возвращаем текущее значение индекса, иначе - продолжаем искать.
В итоге ф-ии возвращаем -1


#### Optimal solution

***Time complexity*** - O(log(n))
***Memory complexity*** -  O(n) 


Используем два указателя l и r. Пока указатели не пересеклись (l <= r) ищем середину листа nums.
Если эл-т посередине > target, сдвигаем правый указатель r на позицию m - 1, 
а если  эл-т посередине < target, сдвигаем левый указатель l на позицию m + 1, 
иначе - возвращаем m. Вся ф-я возвращает -1
