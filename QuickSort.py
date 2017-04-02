# Python program for implementation of Quicksort Sort
 
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
    print("arr ",arr)
    print("i is ",i)
    print("pivot is ",pivot)
    for j in range(low , high):
        print ("arr[j] pivot and arr[i]",arr[j],pivot,arr[i])
        if   arr[j] <= pivot:
            print("arr[j] <= pivot", arr[j], pivot)
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            print("after swapping ",arr)
    print("before last swap", arr)
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print("after last swap", arr)
    
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
 
        pi = partition(arr,low,high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
print(arr)