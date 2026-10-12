# here sorting in incresing order 

def insertion_sort(arr):
    for i in range(1, len(arr)): # key is chosen from 1 to last
        key = arr[i]
        j = i - 1

        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key into its correct position
        arr[j + 1] = key

    return arr


# Example
arr = [5, 2, 4, 1, 3]

print("Original array:", arr)
print("Sorted array:", insertion_sort(arr))