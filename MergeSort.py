#merge sort
def mergeSort(arr):
    arr_length = len(arr)
    
    if arr_length == 1:
        return arr
    
    mid = arr_length//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)
    

def merge(a,b):
    sorted_list = []

    # initiate 2 pts for each array
    pt1 = pt2 = 0
    
    while pt1 < len(a) and pt2 < len(b):
        if a[pt1] <= b[pt2]:
            sorted_list.append(a[pt1])
            pt1 += 1
        else: 
            sorted_list.append(b[pt2])
            pt2 += 1
    
    #for the remaining element left in the array
    sorted_list.extend(a[pt1:])
    sorted_list.extend(b[pt2:])
    
    return sorted_list
            
    
L = [1, 9, 5, 6, 3, 6, 3, 5, 9, 14, 1,7,9,3,534,23,78,23,10]

print(mergeSort(L))
