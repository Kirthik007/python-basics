""" find prime no or not """

n = int(input("enter no "))
if n < 2:
        print("Not prime ")
else:
        for i in range(2,n):
            if n%i == 0:
                print("not prime")
                break
        else:
            print("prime")
            

    
    
