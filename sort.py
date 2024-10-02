from random import randint as rnd
# Генерация случайной последовательности с сортировкой
def get_lst_1(cnt=100, a=1, b=10**6):
    return sorted(rnd(a, b) for _ in range(cnt))
# Генерация последовательности с приращением
def get_lst_2(cnt=100, a=1, b=10):
    lst = [1]
    for _ in range(cnt):
        lst += [lst[-1] + rnd(1, 10)]
    return lst
# Бинарный поиск
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, steps  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps 
# Интерполяционный поиск
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0
    while low <= high and target >= arr[low] and target <= arr[high]:
        steps += 1     
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low, steps
            else:
                return -1, steps
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos, steps  
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1, steps  

def compare_search_algorithms(arr, target):
    binary_result, binary_steps = binary_search(arr, target)
    interpolation_result, interpolation_steps = interpolation_search(arr, target)
    print(f"Бинарный поиск нашел элемент на позиции {binary_result} за {binary_steps} шагов")
    print(f"Интерполяционный поиск нашел элемент на позиции {interpolation_result} за {interpolation_steps} шагов")
# Генерация списка и запись в файл
lst = get_lst_2(100)
with open('./data.txt', 'w') as f:
    f.write(' '.join(str(num) for num in lst))
# Выбор случайного числа из списка для тестирования поиска
target = lst[rnd(0, len(lst)-1)]
# Сравнение поисковых алгоритмов
compare_search_algorithms(lst, target)