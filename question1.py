'''Write a Python program to find those numbers which are divisible by 7
and multiples of 5, between 1500 and 2700 (both included)
5,10,.... 35...
'''
count = 0
for i in range(1500,2701,5):
    if i%7==0:
        count += 1
        print(i)
print("count is" ,count)



          
        
    
    
