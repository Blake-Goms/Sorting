# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    listA = len( arrA ) 
    listB = len( arrB )
    a = 0
    b = 0

    # this loop will continuously check each index and add them together
    while a < listA and b < listB:
        # If tis index is smaller add [a] first to merge 
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            print(f'arrA: {arrA}')
            a += 1
            # else add [b] first 
        else:
            merged_arr.append(arrB[b])
            b += 1
            print(f'arrB: {arrB}')

    # This loop combines each sub array in ListA, sorts them.
    while a < listA:
        print(a, arrA)
        merged_arr.append((arrA[a]))
        print(f'After merging arrA[a]: {merged_arr}')
        a += 1
    # This loop combines each sub array in ListB, sorts them.
    while b < listB:
        merged_arr.append((arrB[b]))
        print(f'After merging arrB[b]: {merged_arr}')
        b += 1
    # This return, returns either ListA or ListB depending on which was sorted.
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ): # This function is breaks down the lists for the merge method/function
    # TO-DO
    # check to make sure len is > 1, otherwise list is already sorted
    if len(arr) > 1:
        # inside here, the left/right variables are recursively running to break down the list
        #  it will run until left len = 1, then repeat for right until len = 1
        left = merge_sort(arr[:len(arr) // 2])
        print(f'left: {left}')
        right = merge_sort(arr[len(arr) // 2:])
        print(f'Right: {right}')
        arr = merge(left, right)

    return arr


arr1 = [8,7,6,5,4,2,1]
merge_sort(arr1)


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
