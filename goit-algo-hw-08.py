import heapq

def min_cost_to_connect_cables(cable_lengths):

    total_cost = 0
    
    # Перетворюємо список довжин кабелів на купу (heap)
    heapq.heapify(cable_lengths)
    
    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Вилучаємо два найкоротші кабелі з купи
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Обчислюємо вартість з'єднання цих двох кабелів
        cost = first + second
        # Додаємо цю вартість до загальної вартості
        total_cost += cost

        # Додаємо новий кабель (результат з'єднання) назад до купи
        heapq.heappush(cable_lengths, cost)
       
    return total_cost

if __name__ == '__main__':
    # Приклад списку довжин кабелів
    cable_lengths = [15, 4, 4, 2, 1]
    
    # Виведення мінімальних витрат на об'єднання кабелів
    print('Мінімальні витрати на об’єднання:', min_cost_to_connect_cables(cable_lengths))