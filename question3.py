''' Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4'''

def oddoreven(list):
    o_c = 0
    e_c = 0
    
    for i in list:
        if i%2==0:
            e_c +=1
        else:
            o_c +=1
    print("odd count is : ",o_c)
    print("even count is : ",e_c)
    
n = int(input(" enter total num "))
c = list(map(int,input(" enter values :").strip().split()))[:n]
print(c)
oddoreven(c)


    
            
