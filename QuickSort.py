def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_numbers = quick_sort(numbers)

print("Sorted list:", sorted_numbers)