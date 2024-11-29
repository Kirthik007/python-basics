''' TO print all prime nos in range given
s = 6 100 - 200
e = 20
7 11 19
count = n
'''
s = int(input("start value for prime range : "))
e = int(input("End value for prime nos in range : "))
count = 0
for i in range(s,e+1):
    if i >1:
        
        for j in range(2,i):
            if i%j == 0: 
                break
        else:
            print("prime",i)
            count +=1
print('total = ',count)
            
            
        
    
    
