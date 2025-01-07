''' Binary search is a simple search algo to find target in an list/arr
    first array must be sorted in ascending
    then followed algo below

'''
def binarysearch(arr,t):
    
    l = 0
    r = len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] == t:
            return m
        elif l < arr[m]:
            l = m+1
        else:
            h = m-1
    return -1
a = [1,2,4,5,6,7,8,9,33,44,56,77]
r = binarysearch(a,33)
print(f'the index of target is {r}  no: {a[r]}')
