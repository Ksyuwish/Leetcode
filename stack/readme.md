## Task 20: Valid Parentheses

#### Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
    
2. Open brackets must be closed in the correct order.
    
3. Every close bracket has a corresponding open bracket of the same type.


#### Optimal solution

***Time complexity*** - O(n)  т к мы проходим по всем эл-ам только 1 раз
***Memory complexity*** -  O(n) 


Создаем словарь со скобками: ключи - закрывающие скобки, значения - закрываюшие скобки. 
Двигаемся по строке и если это открывающая скобка, добавляем в stack.Если закрывающая скобка 
в нашем словаре, проверяем чтобы стек был не пустым и последний вошедший в стек эл-т равен 
открывающей скобке, в этом случае очищаем стек. Если условие не выполнеяется, возвращаем False. 
Сама ф-я вернет False если stack не пустой и True, если пустой
