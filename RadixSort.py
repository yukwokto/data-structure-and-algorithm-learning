def radixSort(arr):
    # find the length of the array
    ARR_LENGTH = len(arr)
    
    # find the digit of the maximum element
    DIGITS = len(str(max(arr)))
    
    # initalise a pool of bucket
    bins = [[]] * 10
    
    # sorting according to the number of digits
    for i in range(DIGITS):
        for j in range(ARR_LENGTH):
            digit_value = int((arr[j] / pow(10, i)) % 10)
            
            # If the list is not empty, it evaluates to True
            if bins[digit_value]:
                bins[digit_value].append(arr[j])
            else: 
                bins[digit_value] = [arr[j]]
        
        # change the elements in the original array according to sequence
        # of elements in the bucket
        k = 0
        # traverse the bins
        for x in range(len(bins)):
            # if bins are not empty, proceeds
            if bins[x]:
                # traverse the bucket in the bins
                for y in range(len(bins[x])):
                    # replace elements in the original array with the sorted elements
                    arr[k] = bins[x].pop(0)
                    # increment the pointer
                    k += 1
    
    return arr

################################################################################################################
# Testing the algorithm

L = [2, 7, 4, 6, 9, 12, 45, 67, 89, 123, 435, 567, 247, 145, 875, 134, 563]

print(radixSort(L))        
            
            
            
    
    
    
