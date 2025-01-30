import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    n = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    
    for _ in range(iterations):
        neighbor = [xi + random.uniform(-0.1, 0.1) for xi in current]
        # Обмеження координат у межах bounds
        neighbor = [max(b[0], min(b[1], x)) for x, b in zip(neighbor, bounds)]
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value
        else:
            # Перевірка на збіжність
            if abs(current_value - neighbor_value) < epsilon:
                break
    return current, current_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    n = len(bounds)
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)
    
    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)
        
        if candidate_value < best_value:
            best, best_value = candidate, candidate_value
        # Перевірка на збіжність
        if abs(best_value - candidate_value) < epsilon:
            break
    return best, best_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    n = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    best = current.copy()
    best_value = current_value
    
    for i in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break
        
        neighbor = [xi + random.uniform(-0.1, 0.1) for xi in current]
        neighbor = [max(b[0], min(b[1], x)) for x, b in zip(neighbor, bounds)]
        neighbor_value = func(neighbor)
        
        # Обчислення ймовірності переходу
        delta = neighbor_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_value = neighbor, neighbor_value
            if current_value < best_value:
                best, best_value = current, current_value
    return best, best_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]  # Приклад для 2D
    random.seed(42)
    
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", [round(x, 6) for x in hc_solution], "Значення:", hc_value)
    
    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", [round(x, 6) for x in rls_solution], "Значення:", rls_value)
    
    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", [round(x, 6) for x in sa_solution], "Значення:", sa_value)