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



