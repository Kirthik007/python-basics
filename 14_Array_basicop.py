"""ARRAY  C,C++ ,Java have built in array in python array is implemented with strings

 -how to use LISTS as ARRAYS, however, to work with arrays in Python
 you will have to import a library, like the NumPy(for very complex operation max not needed )
 go to 1datatypes.py for list syntax and learn list basic operations

"""
arr = [1,3,5,6,7,34,0,6,7,8,1]
#without sort() 
def largsmall(arr):
    l = arr[0]
    s = arr[0]
    for i in arr:
        if l < i :
            l = i
        if s > i :  #using elif causes skip value so only 2 if used
            s = i  
    print(l,s,"largest and smallest")

largsmall(arr)

# find middle element
def mid(arr):
    m = len(arr)-1
    print(m)
mid(arr)
#this gives just the duplicate list values    
def dup(arr):
    a = []
    s = set()
    for i in arr:
        if i in s:
            a.append(i)
        else:
            s.add(i)
    print(f'{a} are duplicate elements ')
dup(arr)
#this code gives value with count for all elements
def dupval(arr):
    d = {}
    
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(f'{d} is th no and count ')
dupval(arr)

#reverse array without reverse() with loop
def rev(arr):
    for i in arr:
        print(f'{i} ')
    print('correct order')
    for i in range(len(arr)-1,-1,-1):
        print(f'{arr[i]}')
    print("the reversed ")
rev(arr)

            

