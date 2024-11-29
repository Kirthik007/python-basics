''' find vowels in string '''

a = input(' i/p string ')
cv = 0
cc = 0
vk = ['a','A','e','E','i','I','o','O','u','U']
for i in a:
    if i in vk:
        cv += 1
    else:
        cc += 1
print(f'the total number of vowels is {cv} and consnants is {cc} ')

