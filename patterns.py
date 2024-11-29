n = 5

def square(n):
    for j in range(n):
        for i in range(n):
             print('*',end=' ')
        print()
square(n)
print('\n')

def inc_triangle(n):
    for j in range(n):
        for i in range(j+1):
             print('*',end=' ')
        print()
inc_triangle(n)
print("\n")

def dec_triangle(n):
    for j in range(n):
        for i in range(j,n):
             print('*',end=' ')
        print()
dec_triangle(n)
print("\n")

def rt_5btm(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end='')
        for k in range(i+1):
            print("*",end='')
        print()
rt_5btm(n)
print("\n")

def topbtm(n):
    for i in range(n):
        for j in range(i+1):
            print('',end='')
        for k in range(i,n):
            print("*",end=' ')
        print()
topbtm(n)
    
