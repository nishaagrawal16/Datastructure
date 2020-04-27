# Date: 16-03-2020
# 
# Description:
# Transform an array to max heap and sort in ascending order. Max heap has
# largest element at 0th index always. In sorting we can copy 0th index element
# to last and run max-heapify again to have next max at 0th index.
# So max heap is used to sort array in ascending order and min heap can be used
# to sort array in descending order.
# 
# Complexity:
# Building heap has O(n)
# Sorting takes O(n*log(n))
#  
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[largest] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr)

    # Build heap from an array, loop is ran from n/2 to 0 as elements from
    # n/2 + 1 to n are leaf nodes and assumed to already heapified.
    # Building heap has a complexity of O(n) although hepify has O(logn)
    # complexity and it loops from n/2 to 0.    
    # Build a maxheap. 
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0)
  
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7]    
heapSort(arr) 
n = len(arr)
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
