''' amstrong number no is sum of cube of digits
153 = 1^3 + 5^3 + 3^3 = 153 '''

st = int(input("range starting for amstrong number "))
e = int(input("range ending "))
count = 0

for n in range(st, e + 1):
    s = 0
    temp = n
    while temp > 0:
        a = temp % 10
        s += a ** 3
        temp = temp // 10
    if s == n:
        print(n)
        count += 1
print("Total Armstrong numbers: ", count)

    


