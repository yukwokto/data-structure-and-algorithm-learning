# This is the function to creat partition and sort the pivot in the given array
# pivot is selected from the start
def partition(arr, start, end):
    # select the pivot (the first element of the array)
    pivot = arr[start]
    
    # set 2 pointers
    # pointer at the start, just behind the pivot
    i = start + 1
    # pointer at the end
    j = end
    
    # start traversing the whole array
    # remember i can always be smaller than or equal to j
    while True:
        # move the pointer (i) at the start when the pointer is smaller than or equal to pivot 
        # and i is smaller than the length of the array.
        while arr[i] <= pivot and i <= j:
            i += 1
        
        # move the pointer (j) at the end when the pointer is greater than or equal to pivot
        # and j is greater than the start of the array.
        while arr[j] >= pivot and i <= j:
            j -= 1
        
        # after both pointers stopped, and if i is smaller or equal to j,
        # we need to swap the elements at i and j elements.
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

        # if i is greater than j, the rearrangement of array is completed,
        # which means the elements on the left half is lower than pivot, and vice versa.
        # It's time to break out of the while loop
        else:
            break
    
    # Now, place the pivot element at the correct position
    # arr[j] is swappped with the pivot because j is always the pointer for elements smaller than pivot
    arr[start], arr[j] = arr[j], arr[start]
    # return the pivot position, which is poiinter j
    return j
    
############################################################################################################
# quick sort function
def quickSort(arr, start, end):
    if start >= end:
        return 
    
    # sort the position of the pivot
    # return the sorted position
    p = partition(arr, start, end)
    
    # sort the portion of the array left to p,
    # hence start will remain the same,
    # but end will be p - 1
    quickSort(arr, start, p - 1)
    
    # sort the portion of the array right to p,
    # hence end will remain the same,
    # but start will be p + 1
    quickSort(arr, p + 1, end)
    
############################################################################################################
# testing the algorithm

L = [7, 3, 1, 9]

quickSort(L, 0, len(L) - 1)

print(L)
