

def quick_sort(arr, low, high):
    if low < high:
        # Find the correct index position of the pivot
        p = partition(arr, low, high)

        # Recursively sort the left and right parts
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  # last element is chosen as pivot 
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Example
arr = [10, 7, 8, 9, 1, 5,66,45,89,78,44,13]
print("Original array :", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
