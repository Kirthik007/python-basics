''' lcm - least common multiple of given all 
gcd - greatest common divisor(largest number devides both )        '''
a,b = map(int,input('enter a,b ').split())
def lcm(a,b):
    if a > b:
        g = a
    else:
        g = b
    while(True):
        if(g%a==0 and g%b == 0):
            lcm = g
            break
        g +=1
    return lcm
print(f'lcm -  {lcm(a,b)}')

def gcd(a,b):
    while(b>0):
        r = a%b
        a = b
        b = r
    return a
print(f'gcd  {gcd(a,b)}')

''' lcm can be found with gcd also  '''
def lcm2(a,b):
    lm = a*b//gcd(a,b)
    return lm
print (f' lcm using gcd {lcm2(a,b)}')

''' without all this in simple we can do find 
by importing math from python'''
 