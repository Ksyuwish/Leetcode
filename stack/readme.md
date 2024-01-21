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


## Task 150: Evaluate Reverse Polish Notation 

#### Description


You are given an array of strings tokens that represents an arithmetic expression 
in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

* The valid operators are '+', '-', '*', and '/'.
* Each operand may be an integer or another expression. 
* The division between two integers always truncates toward zero. 
* There will not be any division by zero. 
* The input represents a valid arithmetic expression in a reverse polish notation. 
* The answer and all the intermediate calculations can be represented in a 32-bit integer.

#### Optimal solution

***Time complexity*** - O(n)  O(2n) тк мы можем удалять эл-т и добавлять его -> O(n)
***Memory complexity*** -  O(n) 

Создаем пустой стек (лист). Итерируемся по элементам листа. В условии else прописываем 
добавление эл-та в стек с типом данных int (добавляем цифпы в лист до тех пор, пока не 
натыкаемся на знак +/-/*//). В случае операции +/* мы добавляем в стек последние добавленные 
эл-ты a+b/a*b используя pop(), в случае "-" наоборот добавляем b-a, а в случае
"/" обязательно делаем это через int(b/a) чтобы округлить до меньшего значения. 
Возвращаем в ответе stack[0].
Суть Polish notation в том, чтобы применять операторы +/-/*// к двум соседствующим эл-ам.


## Task 22: Generate Parentheses 

#### Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed 
parentheses.

***Time complexity*** - O(n) 
***Memory complexity*** -  O(n) 

1. Мы можем добавить "(" если кол-во "("<n

2. Мы можем добавить ")" если кол-во ")" < кол-во "("

3. Когда кол-во "(" == кол-во ")" == n получаем окончательный результат

В задаче используется рекурсия.Создаем ф-ю с несколькими условиями if:

* Если кол-во "(" == кол-во ")" == n Добавляем в пустой лист res строку с последовательностью скобок 
* Если кол-во "("<n добавляем в стек "(" , применяем снова эту же ф-ю с openN+1 и попаем стек 
* Если кол-во ")" < кол-во "(" добавляем в стек ")" применяем снова эту же ф-ю с closedN+1 
* и попаем стек



## Task 739: Daily Temperatures 

#### Description


Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the 
ith day to get a warmer temperature. If there is no future day for which this is possible, 
keep answer[i] == 0 instead.


#### Optimal solution

***Time complexity*** - O(n)
***Memory complexity*** -  O(n) 

Создаем 2 листа: res с нулями (той же длины, что и `len(temperatures)`) 
и stack (pair: [temp, index]). Проходимся по индексам и значениям листа temperatures. 
Прописывем цикл while: пока стек не пустой и 
текущее значение температуры > предыдыдущей температуры из стека (тк пара,берем 0-ой эл-т).
Сохраняем попнутые значения из стека в переменные stackT, stackInd. 
В лист res на место индекса stackInd добавляем разницу между текущим индексом 
и попнутым идексом из стека stackInd. В конце цикла for аппедним в стек текущее значение 
температуры из temperatures и текущий индекс. В ответе возвразаем лист `res`.
