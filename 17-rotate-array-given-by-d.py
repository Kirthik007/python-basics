def leftrot(arr,d):
    for i in range(d):
        temp = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1]= temp
    return arr
a = [1,2,3,4,5]
s = leftrot(a,2)
print(s)

def rtrot(arr,d):
    for i in range(d):
        temp = arr[len(arr)-1]
        for j in range(len(arr)-1,0,-1):
            arr[j] = arr[j-1]
        arr[0]= temp
    return arr
b = [1,2,3,4,5]
r = rtrot(b,2)
print(r)

''' with slice'''