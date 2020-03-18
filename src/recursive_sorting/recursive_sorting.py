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

    # class example for problem
    a = 0
    b = 0

    for k in range(0, elements):
        # compare a and b
        # if a is out of range, push b and iterate
        if a >= len(arrA): #we are done with a, push b
            merged_arr[k] = arrB[b]
            b+=1 #b++
        # if b is out of range, push a and iterate
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a+=1
        # if a is smaller, put it in array and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a+=1
        # if b is smaller, put it in array and iterate both
        else: 
            merged_arr[k] = arrB[b]
            b+=1



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base condition
    # if array size is >=1
    if len(arr) > 1: 
        # finding the middle of arr
        mid = len(arr) // 2
        # sort stuff in left and put it in left
        left = merge_sort(arr[:mid])
        # sort stuff in right and put in right
        right = merge_sort(arr[mid:])
        # merge left and right
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
