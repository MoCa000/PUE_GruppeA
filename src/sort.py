def bubble_sort(arr):
    # Bubble sort algorithm
    # Sorts the input array in ascending order
    # Returns the sorted array
    # Time complexity: O(n^2)
    # Space complexity: O(1)
   
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr