n =int(input("input num for fact : "))
fact = 1
'''while n>0:
    fact = n*fact
    n -= 1
    
print(fact)'''
for i in range(1,n+1):
    fact *= i
print(f' factorial of {n} is {fact} ' )



'''5 5! = 5*4*3*2*1
    5! = 1
'''
