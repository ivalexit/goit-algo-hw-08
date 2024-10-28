
"""
Кожне зʼєднання утворює новий дріт. За логікою задачі обʼєднання довгих дротів
призводить до більших витрат, а нам не вигідно накопичувати 
великі суми на початку роботи. Отже, обʼєднувати дроти краще починати
з найкоротших. Програмно для цього застосовуємо мінімальну купу, яка дає
можливість швидко діставати два найменші елементи для виконання операцій над ними.
(Хорошою альтернативою міг би бути жадібний алгоритм)

"""



import heapq

def minimize_costs(cables):
    heapq.heapify(cables)
    total_costs = 0

    while len(cables) > 1:
        first_shortest = heapq.heappop(cables)
        second_shortest = heapq.heappop(cables)

        costs = first_shortest + second_shortest
        total_costs += costs

        heapq.heappush(cables, costs)
    return total_costs


cables = [3, 6, 7, 2, 8, 4, 9, 5, 11, 1]
print("The least possible amount spent on connection of all the cables can be:", minimize_costs(cables), "bucks.")
