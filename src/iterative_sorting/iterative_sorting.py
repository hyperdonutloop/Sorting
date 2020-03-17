# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             



        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i +1], arr[i]
                swapped = True
        if swapped == False:
                break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# * line 4 - we are saying -1 because once we have one item in the list we don't need to do a comparison on it. We can assume it is the highest value because it is the last item left.

# * line 5 - we are assigning 'cur_index' = 1 because each time we do an iteration we want the first element on the list to be the default min.