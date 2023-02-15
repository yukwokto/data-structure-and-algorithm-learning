def shellSort(arr):
    # determines the length of the array
    ARR_LEN = len(arr)
    
    # finds out the maximum gap size of the array
    gap = ARR_LEN // 2
    
    #when the gap size is greater than 0, continuing to arranging the array
    while gap > 0:
    # traverse the array from gap to the end of the array
        for i in range(gap, ARR_LEN):
            # store the value of the particular element in case of swapping
            temp = arr[i]
            #set up pointer j for comparison
            j = i
            
            # 1.          j <= gap:    to ensure there are no elements on the left of j after the interval of gaps
            # 2. arr[j-gap] > temp:    if the elements at gap interval is greater than j, swapping required
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]   # swaps arr[j] with arr[j-gap] because arr[j-gap] is greater than temp
                j -= gap              # moves j gap interval forward

            # after determining the position of temp, swaps temp with arr[j]
            arr[j] = temp
        
    # reduce the gap size by dividing 2
        gap //= 2

######################################################################################################################
#testing the algorithm

if __name__ == '__main__':
     
    L = [12, 17, 11, 8, 5, 9]
    shellSort(L)
    print(L)
    
    
 ######################################################################################################################   
 
