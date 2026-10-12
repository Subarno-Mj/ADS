# incresing order sort 

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        # Compare adjacent elements
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if no swaps occurred
        if not swapped:
            break

    return arr


# Example
arr = [5, 1, 4, 2, 8]

print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))