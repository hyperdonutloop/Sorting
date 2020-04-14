# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # we say len(arr) - 1 bc len is ONE based not ZERO based like the index
    for i in range(0, len(arr) - 1):
        # cur_index is holding the min position
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # for every item to the right of our cur_index (cur_index + 1)
        for j in range(cur_index + 1, len(arr)):
            # if the item in position j is smaller than our cur_index
            if arr[j] < arr[smallest_index]:
                # smallest index is now j
                smallest_index = j
        # TO-DO: swap
        # taking current index, and smallest index and swapping them
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # saying -1 bc we can't make a comparison on the last number (there is no # after it)
    indexing_length = len(arr) - 1
    sorted = False
    # as long as the variable sorted is false
    while not sorted:
        sorted = True
        # for every item of the arr
        for i in range(0, indexing_length):
            # if the index is greater than the value to the right --> 
            if arr[i] > arr[i+1]:
                # then, declaring sorted = false (bc the above is true)
                sorted = False
                # swapping values (sorting them)
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # whenever we have sorted all items the if statement will not activate and the sorted variable remains true - line 32
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# * line 4 - we are saying -1 because once we have one item in the list we don't need to do a comparison on it. We can assume it is the highest value because it is the last item left.

# * line 5 - we are assigning 'cur_index' = 1 because each time we do an iteration we want the first element on the list to be the default min.