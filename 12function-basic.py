'''Function
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''


def sum(a,b):
    
    return a+b

def sub(a,b):
    c = a-b
    return c

def mul(a,b):
    c = a*b
    print(c)
    
c = sum(4,5)
print(c)

mul(4,5)

def fact(n):
    if(n == 1 ):
        return 1
    else:
        return (n * fact(n-1))
'''
5*(4) =20 * 3 =ey* (2) 1...
'''

print(fact(5))

'''  lambda function A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression
lambda arguments : expression
'''
x = lambda a : a + 10
print(x(5))
    

    
