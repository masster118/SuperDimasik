def quick_sort_two_pointers(arr, low, high):
    if low < high:
        pivot_index = partition_two_pointers(arr, low, high)
        quick_sort_two_pointers(arr, low, pivot_index)
        quick_sort_two_pointers(arr, pivot_index + 1, high)

def partition_two_pointers(arr, low, high):
    pivot = arr[(low + high) // 2]
    left = low - 1
    right = high + 1
    while True:
        left += 1
        while arr[left] < pivot:
            left += 1
        right -= 1
        while arr[right] > pivot:
            right -= 1
        if left >= right:
            return right
        arr[left], arr[right] = arr[right], arr[left]