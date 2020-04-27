# Date: 16-03-2020
# 
# Description:
# Transform an array to min heap and sort in descending order. Min heap has
# smallest element at 0th index always. In sorting we can copy 0th index
# element to last index and run min-heapify again to have next min at 0th
# index.
# So min heap is used to sort array in descending order and max heap can be
# used to sort array in ascending order.
# Complexity:
# Building heap has O(n)
# Sorting takes O(n*log(n))
# 

def heapify(arr, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[smallest] > arr[l]:
        smallest = l

    if r < n and arr[smallest] > arr[r]:
        smallest = r
    
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, n, smallest)

def heapSort(arr):
    n = len(arr)
    # Building min heap. Building min heap has total complexity of O(n).
    # Refer: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
    # This loop is run from n/2 down to 0 with an assumption that lower level
    # elements (from n/2+1 to n) in heap is already heapfied.
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7]    
heapSort(arr) 
n = len(arr)
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 