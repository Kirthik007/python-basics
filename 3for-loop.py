"""A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,
a set, or a string).

This is less like the for keyword in other programming languages, and works more like an
iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

"""

for x in range(1,20,2):
    print("char \n" ,x)

adj =["a","b","c"]
frt =["orange","apple","berry","banana"]

for x in adj:
    for y in frt:
        print(x,y)
        
