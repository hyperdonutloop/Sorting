# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i, j, k = 0, 0, 0
   # traverse both arrays
    while i < len(arrA) and j < len(arrB):
       # check if current element of first array 
       # is smaller than current element of second array.
       # if yes, store the first array of the element
       # and increment first array index.
       #Otherwise do the same with second array
        if arrA[i] <= arrB[j]:
           merged_arr[k] = arrA[i]
           i+=1
        else:
            merged_arr[k] = arrB[j]
            j+=1
        k+=1
        # store the remaining elements of first array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i+=1
        k+=1
        # store remaining elements of second array
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j+=1
        k+=1
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1: 
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
