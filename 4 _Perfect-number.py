''' A number is a perfect number if is equal to sum of its proper divisors, 
that is, sum of its positive divisors excluding the number itself.
Examples: 

Input: n = 15
Output: false
Divisors of 15 are 1, 3 and 5. Sum of 
divisors is 9 which is not equal to 15.
Input: n = 6
Output: true
Divisors of 6 are 1, 2 and 3. Sum of 
divisors is 6.      the solution here is most optimal works in all coding tests'''

def isPerfectNumber(n):
    l = [1]
    if (n == 1):
        return False
    else:
        s = 1
        for i in range(2,int(n**.5)+1):
            if n % i == 0 :
                s += i + n//i
    if n == s:
        return True 
    else:
        return False

a = int(input("Enter no : "))
print(isPerfectNumber(a))