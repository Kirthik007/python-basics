'''With a given integral number n, write a program to generate
a dictionary that contains (i, i*i)such that is an
integral number between 1 and n (both included). '''

d = dict()
s = int(input("start : "))
e = int(input("end : "))
for i in range(s,e+1):
        d[i]=i*i
print("dictionary ",d)


