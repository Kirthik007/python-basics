''' bubble sort Bubble Sort algorithm, which sorts an array by repeatedly comparing 
 adjacent elements and swapping them if they are in the wrong order. The algorithm iterates
 through the array multiple times, with each pass pushing the largest unsorted element to its 
 correct position at the end.  this has O(nlogn)'''
def bubbler(arr):
    n = len(arr)
    for i in range(n):
        swapp = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapp = True
        if not swapp:
            break
    return arr
ar = [2,4,1,5,3]
print("unsorted array :",ar)
rb = bubbler(ar)
print(f'sorted by bubble sort {rb}')

""" Merge Sort  It divides input array in two halves, calls itself for
 the two halves and then merges the two sorted halves. The merge() function
 is used for merging two halves. The merge(arr, l, m, r) is key process that 
 assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted 
 sub-arrays into one.  this has O(nlogn)                
"""

def mergesort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        l =arr[:m]
        r =arr[m:]

        mergesort(l)
        mergesort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j +=1
            k +=1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    return arr    

s = mergesort(ar)
print("Sorted by merge sort:",s)

""" Quick sort  QuickSort is a divide and conquer algorithm. 
It picks an element as a pivot and partitions the given array 
around the picked pivot. In simple terms:

- **Best and Average Case** for QuickSort: **O(n log n)**
- **Worst Case** for QuickSort: **O(n²)**

This means that QuickSort is usually very efficient (best and average cases),
 but it can become slower (worst case) if the pivot selection is poor.
"""

def quick(arr):

    l = []
    m = []
    r = []
    if len(arr) > 1:
        piv = arr[len(arr)-1]
        for i in arr:
            if i < piv:
                l.append(i)
            elif i == piv:
                m.append(i)
            else:
                r.append(i)
        return quick(l)+m+quick(r)
    else:
        return arr
      

a = [2,4,5,83,2,9,3]
s = quick(ar)
print("Sorted by quick sort: ",s)

    


