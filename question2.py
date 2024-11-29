'''Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
4f 4c
fahrenheit=(celsius * 9 / 5) + 32
celcius=(fahrenheit - 32) * 5 / 9
if s == "c":
     c_t = (n * 9/5) + 32 print(f'Temperature is {c_t:.2f}F')
else:
     c_t = (n - 32) * 5/9 print(f'Temperature is {c_t:.2f}C'
'''

temp = input("enter temp ")
num = ""
str1 = ""
c_t =""
for i in temp: 
    if i.isdigit():
        num += i
    else:
        str1 += i 
str1 = str1.upper()  
num = int(num)
if str1 == "C":
    c_t = (num*9/5)+32
    print(f'temp is {c_t:.3f}F ')
elif str1 == "F":
    c_t = (num-32)*5/9
    print(f'temp is {c_t:.3f}C ')
else:
    print("enter f or c to convert ")

    

    





