def quick_sort_filter(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = list(filter(lambda x: x < pivot, arr[1:]))
    greater = list(filter(lambda x: x >= pivot, arr[1:]))
    return quick_sort_filter(less) + [pivot] + quick_sort_filter(greater)