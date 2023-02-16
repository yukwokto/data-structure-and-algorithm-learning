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

##########################################################################################

# count sort with negative number using dictionary

def negative_count_sort(arr):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict.update({num: (occurance := count_dict.get(num)) + 1})
        else:
            count_dict.update({num: 1})
    
    # sorted the count dictionary by key
    count_dict = dict(sorted(count_dict.items()))
    
    # set up pointer for changing element in the unsorted array
    i = 0
    
    for k, v in count_dict.items():
        while v > 0:
            arr[i] = k
            i += 1
            v -= 1
    
    return arr
            
######################################################################################    

# implementation
if __name__ ==  '__main__':

    Ln = [-4, -3, -2, -12, -13, -5, 4, 2, 12, 4, 6, 7, -5, -5, -5]
    print(negative_count_sort(Ln))

# result
# [-13, -12, -5, -5, -5, -5, -4, -3, -2, 2, 4, 4, 6, 7, 12]
    
    
