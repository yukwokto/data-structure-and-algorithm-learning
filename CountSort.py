def count_sort(arr):
    # find out the array size of array by figuring out the maximum element of the array
    ARR_SIZE = max(arr) + 1
    
    # create a counting array for counting the occurance of each element
    count_array = [0 for i in  range(ARR_SIZE)]
    
    # traverse the array and count the occurance of each element
    for x in range(len(arr)):
        count_array[value := arr[x]] += 1  
    
    # set up a pointer for the original array
    j = 0
    
    # traverse the count array
    for i in range(len(count_array)):
        # if the occurance of an element is greater than 1,
        # then we swap the element with the unsorted array,
        # then we decrement the occurance of the element by 1.
        while count_array[i] > 0:
            arr[j] = i
            j += 1
            count_array[i] -= 1
            
    return arr
    
##########################################################################################
#implementation of count sort

if __name__ ==  '__main__':
    L = [4, 7, 8, 9, 1, 2, 1, 3, 4, 7, 6, 5, 14, 23, 56, 13]
    print(count_sort(L))
    
# result: [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 13, 14, 23, 56]
