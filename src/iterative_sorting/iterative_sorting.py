# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                '''
                The above for loop is looping through again
                It's finding the smallest number in index j 
                then if a number is smaller, assign it to smallest_index, to update the smallest number found
                '''
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        '''
        Alternate way, but this is longer
        temp = arr [cur_index]
        arr[cur_index] = arr[smallest_index] 
        arr[smallest_index]  = temp
        '''
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    print(f'\nOirginal List:\n{arr}')
    for i in range(0, len(arr)):
        print(f'\nOuter Loop Counter: {i}\n')
        for j in range(0, len(arr)):
            print(f'{arr}, \nComparing: {arr[j]}, {arr[i]}')
            if arr[j] > arr[i]:
                print(f'Swapping: {arr[j]}, {arr[i]}')
                arr[i], arr[j] = arr[j] , arr[i]
            #elif(arr[j] < arr[i]):
            #    print(f'Pair already sorted: {arr[j], arr[i]}\n')

    return arr

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# bubble_sort(arr1)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr